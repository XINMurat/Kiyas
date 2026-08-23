#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kıyas seed validator — LLM-free static enforcement of hard rules G1–G12.

SCOPE, stated plainly because the methodology demands it: this tool is a
`runtime` arbiter for CONTRACT COMPLETENESS only. It checks that the illet
field is filled; it cannot check that the illet is true. Idea quality stays
with a human or a frontier model. Presenting this validator as a judge of
idea quality would be exactly the "threshold theatre" that Mizan R8 exists
to prevent — an arbiter-less domain wearing an arbiter-ed domain's clothes.

Bilingual: messages are emitted in the requested language (--lang tr|en).

TWO CHANNELS, and the reason there are two: G6's own design note says that if
every flag blocked promotion, authors would learn to leave the sweep silent —
a flagged seed that states its scope beats a clean-looking one that dodged the
question. The same logic applies to this tool. A single blocking channel
pushes authors to write batches that do not trigger rules, which is not the
same as writing better batches. So:

  * VIOLATIONS (G1–G12) block. They mark a contract that is incomplete in a way
    the prose forbids outright.
  * WARNINGS (W1–W5) do not block by default. They mark shapes that are
    usually wrong but have legitimate exceptions, so the right response is to
    look, not to be stopped. `--strict` promotes them to violations; CI runs
    strict, local runs do not.

Usage:
    python tools/kiyas_validate.py path/to/kiyas-seed.yaml
    python tools/kiyas_validate.py --lang tr seeds.yaml
    python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml
    python tools/kiyas_validate.py --strict seeds.yaml     # warnings fail too

Exit code 0 = clean, 1 = violations found, 2 = usage/parse error.

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "ERROR: PyYAML is required. Install it with: pip install pyyaml\n"
        "HATA: PyYAML gerekli. Kurulum: pip install pyyaml\n"
    )
    sys.exit(2)

# W1 — "a precise-looking threshold" in the anti-pattern list. Deliberately
# conservative: a comparison operator or a percentage next to a number. Prose
# that merely says "none, a number here would be decorative" contains no
# digits and is not flagged.
NUMERIC_THRESHOLD = re.compile(
    r"(>=|<=|[<>]|±)\s*\.?\d|\d+(?:[.,]\d+)?\s*%"
)

VALID_TIERS = {"S", "H-aday", "NK", "GB"}
ARBITER_CLASSES = {"runtime", "instrument", "third_party", "author", "none"}
VALID_OPERATORS = {"O1", "O2", "O3", "O4", "O5", "O6", "O7"}
SWEEP_KEYS = [
    "AD1_notation_coincidence",
    "AD2_surface_resonance",
    "AD3_confirmation_bias",
    "AD4_refuted_relative",
    "AD5_scale_leak",
    "AD6_trace_base_rate",
]

# Placeholder text from the schema template. A seed that still carries the
# instructions instead of an answer has not been filled in — the most common
# way a contract passes structurally while being empty in substance.
PLACEHOLDER_MARKERS = (
    "the structural equivalence that carries",
    "one sentence, refutable",
    "where the analogy/relation breaks down",
    "the smallest experiment that kills",
    "the concrete judge —",
    "the real competitor.",
    "the idea that was weighed and refused",
    "why it was refused: which anti-pattern",
)

# Bilingual message catalog: key -> (en, tr)
MSG = {
    "G1_no_illet": (
        "G1: seed {id} has no illet — an idea whose illet cannot be named was not generated; discard it.",
        "G1: {id} tohumunun illeti yok — illeti isimlendirilemeyen fikir üretilmiş sayılmaz; at.",
    ),
    "G2_no_breaking_point": (
        "G2: seed {id} is tier H-aday with no breaking_point — an analogy with no stated limit is ornament.",
        "G2: {id} tohumu H-aday ama kırılma noktası yok — sınırı yazılmamış analoji süstür.",
    ),
    "G3_superiority_without_prior_art": (
        "G3: seed {id} claims superiority but prior_art.searched is false — tier is forced to S, found '{tier}'.",
        "G3: {id} tohumu üstünlük iddia ediyor ama prior_art.searched false — tier zorunlu olarak S, bulunan '{tier}'.",
    ),
    "G3_no_strongest_relative": (
        "G3: seed {id} claims superiority but names no strongest_relative — the real competitor is missing from the comparison set.",
        "G3: {id} tohumu üstünlük iddia ediyor ama strongest_relative yok — asıl rakip karşılaştırma setinde değil.",
    ),
    "G3_no_discrimination_test": (
        "G3: seed {id} names a strongest_relative but no discrimination_test — an untested distinction is decorative.",
        "G3: {id} tohumu strongest_relative veriyor ama ayrım testi yok — test edilmemiş ayrım dekoratiftir.",
    ),
    "G4_capacity_no_control": (
        "G4: seed {id} adds capacity but has no matched_budget_control — a generic-capacity gain cannot be attributed to the targeted mechanism.",
        "G4: {id} tohumu kapasite ekliyor ama eşleşik-bütçe kontrol kolu yok — jenerik kapasite kazancı hedeflenen mekanizmaya atfedilemez.",
    ),
    "G5_no_arbiter": (
        "G5: seed {id} has no arbiter block — a threshold proposal with no named judge is self-report.",
        "G5: {id} tohumunda hakem bloğu yok — hakemi isimlendirilmemiş eşik önerisi öz-beyandır.",
    ),
    "G5_bad_class": (
        "G5: seed {id} has invalid arbiter.class '{cls}' (allowed: runtime instrument third_party author none).",
        "G5: {id} tohumunda geçersiz arbiter.class '{cls}' (izinli: runtime instrument third_party author none).",
    ),
    "G5_no_who": (
        "G5: seed {id} names arbiter.class '{cls}' but not arbiter.who — the concrete judge is missing.",
        "G5: {id} tohumu arbiter.class '{cls}' diyor ama arbiter.who boş — somut hakem yok.",
    ),
    "G5_none_leaves_S": (
        "G5: seed {id} has arbiter.class 'none' but tier '{tier}' — with no judge the threshold proposal is decorative; tier stays S.",
        "G5: {id} tohumunun arbiter.class'ı 'none' ama tier '{tier}' — hakemsiz eşik önerisi dekoratiftir; tier S'de kalır.",
    ),
    "G5_no_calibration": (
        "G5: seed {id} uses arbiter.class '{cls}' without calibration — thresholds are not inherited across instruments (write 'unknown' if that is the truth).",
        "G5: {id} tohumu '{cls}' hakem sınıfını kalibrasyonsuz kullanıyor — eşikler enstrümanlar arası miras alınmaz ('unknown' yazmak da geçerli cevaptır).",
    ),
    "G6_sweep_missing": (
        "G6: seed {id} has no antipattern_sweep — silence is not a clean sweep.",
        "G6: {id} tohumunda anti-desen taraması yok — sessizlik temiz tarama değildir.",
    ),
    "G6_sweep_incomplete": (
        "G6: seed {id} antipattern_sweep is missing {keys} — record 'clear' explicitly.",
        "G6: {id} tohumunun anti-desen taramasında {keys} eksik — 'clear' açıkça yazılmalı.",
    ),
    "G6_AD1_requires_NK": (
        "G6/AD1: seed {id} has a notation-coincidence flag but tier '{tier}' — a unit/basis/instrument-dependent equivalence is tiered NK until the sweep clears it.",
        "G6/AD1: {id} tohumunda notasyon-tesadüfü bayrağı var ama tier '{tier}' — birim/baz/enstrüman bağımlı denklik, tarama temizlenene dek NK'dir.",
    ),
    "G6_AD2_requires_S": (
        "G6/AD2: seed {id} has a surface-resonance flag but tier '{tier}' — an analogy whose illet cannot be named is discarded or kept at S.",
        "G6/AD2: {id} tohumunda yüzeysel-rezonans bayrağı var ama tier '{tier}' — illeti isimlendirilemeyen analoji atılır veya S'de tutulur.",
    ),
    "G6_AD4_requires_GB": (
        "G6/AD4: seed {id} is a relative of a refuted pattern but tier '{tier}' — generate it with the fed-back warning (GB) or drop it.",
        "G6/AD4: {id} tohumu çürütülmüş bir desenin akrabası ama tier '{tier}' — geri-besleme uyarısıyla (GB) üret ya da ele.",
    ),
    "G6_AD5_no_scope": (
        "G6/AD5: seed {id} flags a scale/regime leak but writes no scope_caveat — the regime the prediction holds in must be stated in the seed.",
        "G6/AD5: {id} tohumu ölçek/rejim sızıntısı bayrağı çakıyor ama scope_caveat yazmamış — öngörünün geçerli olduğu rejim tohuma yazılmalı.",
    ),
    "AD6_no_base_rate": (
        "G6/AD6: seed {id} flags a trace base rate but writes no trace_base_rate into the preregistered prediction.",
        "G6/AD6: {id} tohumu iz-tabanı bayrağı çakıyor ama önkayıtlı öngörüye trace_base_rate yazmamış.",
    ),
    "GB_known_refuted": (
        "AD4: seed {id} resembles refuted pattern '{pat}' but is not tagged GB — regenerate with the fed-back warning or drop it.",
        "AD4: {id} tohumu çürütülmüş '{pat}' desenine benziyor ama GB etiketli değil — geri-besleme uyarısıyla yeniden üret ya da ele.",
    ),
    "batch_few_operators": (
        "BATCH: only {n} distinct operator(s) used ({ops}) — diversity comes from operator choice; use at least 3.",
        "PARTİ: yalnız {n} farklı operatör kullanılmış ({ops}) — çeşitlilik operatör seçiminden gelir; en az 3 kullan.",
    ),
    "batch_no_symmetry": (
        "BATCH: symmetry_check is empty — a batch where every seed flatters the current thesis is confirmation bias (AD3).",
        "PARTİ: symmetry_check boş — her tohumu mevcut tezi okşayan parti doğrulama yanlılığıdır (AD3).",
    ),
    "batch_no_problem": (
        "BATCH: batch.problem is empty — every seed answers one named blocked problem.",
        "PARTİ: batch.problem boş — her tohum isimlendirilmiş tek bir tıkanma problemini yanıtlar.",
    ),
    "bad_tier": (
        "SCHEMA: seed '{id}' has invalid tier '{tier}' (allowed: S H-aday NK GB).",
        "ŞEMA: '{id}' tohumu geçersiz tier '{tier}' taşıyor (izinli: S H-aday NK GB).",
    ),
    "bad_operator": (
        "SCHEMA: seed '{id}' has invalid operator '{op}' (allowed: O1..O7).",
        "ŞEMA: '{id}' tohumu geçersiz operatör '{op}' taşıyor (izinli: O1..O7).",
    ),
    "placeholder": (
        "TEMPLATE: seed '{id}' field '{field}' still contains schema placeholder text — the contract is formatted, not filled.",
        "ŞABLON: '{id}' tohumunun '{field}' alanı hâlâ şema yer-tutucu metnini taşıyor — sözleşme doldurulmamış, sadece biçimlenmiş.",
    ),
    "G7_no_discards": (
        "G7: batch has no `discards` block — what you refused is part of the generation; "
        "an unwritten discard list and an empty one are the same absence. Write `discards: []` "
        "plus batch.discards_note if nothing was refused.",
        "G7: partide `discards` bloğu yok — neyi reddettiğin üretimin parçasıdır; "
        "yazılmamış bir reddedilenler listesi ile boş bir liste aynı yokluktur. Hiçbir şey "
        "reddedilmediyse `discards: []` ve batch.discards_note yaz.",
    ),
    "G7_empty_without_note": (
        "G7: batch declares `discards: []` but no batch.discards_note — an empty list is legal "
        "only when it says what was considered and refused nothing.",
        "G7: parti `discards: []` diyor ama batch.discards_note yok — boş liste ancak neyin "
        "değerlendirilip hiçbirinin reddedilmediğini söylediğinde geçerlidir.",
    ),
    "G7_discard_incomplete": (
        "G7: discard #{i} is missing {field} — a discard needs both what was refused and why "
        "(name the anti-pattern or the prior art that saturates it).",
        "G7: {i}. reddedilen girdide {field} eksik — bir reddetme hem neyin reddedildiğini hem "
        "nedenini ister (anti-deseni ya da onu doyuran prior art'ı adlandır).",
    ),
    "G8_no_test": (
        "G8: seed {id} is tier H-aday with no cheapest_refutation.test — an idea for which no "
        "test could be designed stays S. The refutation condition is what makes a candidate "
        "auditable rather than merely interesting.",
        "G8: {id} tohumu H-aday ama cheapest_refutation.test yok — tasarlanabilir bir testi "
        "olmayan fikir S'de kalır. Bir adayı sadece ilginç olmaktan çıkarıp denetlenebilir "
        "yapan şey çürütme koşuludur.",
    ),
    "G9_no_prior_art_search": (
        "G9: seed {id} is tier H-aday with prior_art.searched false — \"not searched\" is an "
        "honest answer, but then the idea cannot be H-aday.",
        "G9: {id} tohumu H-aday ama prior_art.searched false — \"aranmadı\" dürüst bir cevaptır, "
        "ama o zaman fikir H-aday olamaz.",
    ),
    "G10_independence_contradiction": (
        "G10: seed {id} declares arbiter.class '{cls}' with independent_of_author: true — that "
        "class is by definition not independent, and a contradiction inside the arbiter block "
        "undoes the one field the whole handoff rests on.",
        "G10: {id} tohumu arbiter.class '{cls}' ile independent_of_author: true beyan ediyor — bu "
        "sınıf tanımı gereği bağımsız değildir; hakem bloğunun içindeki çelişki, tüm devrin "
        "dayandığı tek alanı geçersiz kılar.",
    ),
    "G11_no_refuted_source": (
        "G11: batch has no refuted_patterns_source — say which negative-constraint export was "
        "consulted, or write \"not consulted\". Silence is not a clean sweep, and it makes every "
        "AD4 line in the batch unverifiable.",
        "G11: partide refuted_patterns_source yok — hangi çürütülmüş-desen ihracına bakıldığını "
        "yaz ya da \"not consulted\" de. Sessizlik temiz tarama değildir ve partideki her AD4 "
        "satırını doğrulanamaz kılar.",
    ),
    "G12_no_generation": (
        "G12: batch has no `generation` block — a batch that cannot say which seed and which "
        "host drew it cannot be compared with a second run. Write generation.seed (\"fresh\" is "
        "an honest answer) and generation.host.",
        "G12: partide `generation` bloğu yok — hangi tohum ve hangi host tarafından çekildiğini "
        "söyleyemeyen bir parti ikinci bir koşuyla karşılaştırılamaz. generation.seed (\"fresh\" "
        "dürüst bir cevaptır) ve generation.host yaz.",
    ),
    "G12_no_field": (
        "G12: batch.generation has no {field} — silence is not a value. Write \"fresh\" for an "
        "unpinned draw or \"unknown\" for a host you cannot name; an absent field is not an answer.",
        "G12: batch.generation içinde {field} yok — sessizlik bir değer değildir. Sabitlenmemiş "
        "bir çekiliş için \"fresh\", adlandıramadığın bir host için \"unknown\" yaz; olmayan bir "
        "alan cevap değildir.",
    ),
    "G12_digest_mismatch": (
        "G12: batch.generation.inputs_digest is {claimed} but the inputs hash to {actual} — the "
        "batch was drawn from different inputs than the ones it names, so comparing it with "
        "another run would compare two different questions.",
        "G12: batch.generation.inputs_digest {claimed} diyor ama girdilerin özeti {actual} — parti "
        "adlandırdığı girdilerden değil başka girdilerden çekilmiş; başka bir koşuyla "
        "karşılaştırmak iki farklı soruyu karşılaştırmak olurdu.",
    ),
    "W5_pinned_seed_no_digest": (
        "W5: batch.generation.seed is pinned to '{seed}' but there is no inputs_digest — a seed "
        "with no record of the inputs it was applied to identifies nothing. Run "
        "tools/kiyas_digest.py and record it.",
        "W5: batch.generation.seed '{seed}' olarak sabitlenmiş ama inputs_digest yok — hangi "
        "girdilere uygulandığı kayıtlı olmayan bir tohum hiçbir şeyi tanımlamaz. "
        "tools/kiyas_digest.py çalıştırıp kaydet.",
    ),
    "W1_threshold_without_judge": (
        "W1: seed {id} proposes a numeric threshold but its arbiter class is '{cls}' — the form "
        "of a verification loop without its judge is not rigor. Drop the number or name a judge.",
        "W1: {id} tohumu sayısal eşik öneriyor ama hakem sınıfı '{cls}' — hakemi olmayan bir "
        "doğrulama döngüsünün biçimi titizlik değildir. Sayıyı kaldır ya da hakem adlandır.",
    ),
    "W2_all_haday": (
        "W2: all {n} seeds in this batch are H-aday — a batch where everything lands at H-aday "
        "is usually a batch that skipped the sweep. Legitimate, but worth a second look.",
        "W2: bu partideki {n} tohumun hepsi H-aday — her tohumu H-aday'e inen parti genellikle "
        "taramayı atlamış partidir. Meşru olabilir, ama bir kez daha bakmaya değer.",
    ),
    "W3_symmetry_id_unknown": (
        "W3: batch.symmetry_check names no seed id from this batch — the schema asks it to name "
        "the seed that breaks the current thesis, so the claim can be checked against a seed.",
        "W3: batch.symmetry_check bu partideki hiçbir tohum id'sini anmıyor — şema, mevcut tezi "
        "kesen tohumun adlandırılmasını ister ki iddia bir tohuma karşı kontrol edilebilsin.",
    ),
    "W4_O5_no_scope": (
        "W4: seed {id} uses operator O5 (scale transfer) without a scope_caveat — a finding at "
        "one regime does not become a claim about another by being restated.",
        "W4: {id} tohumu O5 (ölçek transferi) kullanıyor ama scope_caveat yok — bir rejimdeki "
        "bulgu, yeniden ifade edilerek başka bir rejim hakkında iddiaya dönüşmez.",
    ),
    "clean": (
        "OK — {n} seed(s) checked, no G1–G12 violations.",
        "OK — {n} tohum kontrol edildi, G1–G12 ihlali yok.",
    ),
    "warn_header": (
        "{n} warning(s) — not blocking; re-run with --strict to treat them as failures.",
        "{n} uyarı — bloke etmiyor; hata saymak için --strict ile yeniden koş.",
    ),
    "warn_strict": (
        "{n} warning(s) promoted to violations by --strict.",
        "{n} uyarı --strict ile ihlale yükseltildi.",
    ),
    "found": (
        "{n} violation(s) found.",
        "{n} ihlal bulundu.",
    ),
}


def m(key: str, lang: str, **kw: Any) -> str:
    en, tr = MSG[key]
    return (tr if lang == "tr" else en).format(**kw)


def _s(v: Any) -> str:
    return (v or "").strip() if isinstance(v, str) else ("" if v is None else str(v).strip())


def load(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError("top-level YAML is not a mapping")
    return data


NOT_CONSULTED = {"not consulted", "none", "-"}


def normalise_problem(text: str) -> str:
    """Collapse whitespace so reflowing the YAML block cannot move the digest."""
    return re.sub(r"\s+", " ", (text or "").strip())


def inputs_digest(problem: str, refuted_bytes: bytes) -> str:
    """Must stay identical to tools/kiyas_digest.py; a self-test pins them together."""
    h = hashlib.sha256()
    h.update(normalise_problem(problem).encode("utf-8"))
    h.update(b"\x00")
    h.update(refuted_bytes)
    return h.hexdigest()[:16]


def _consulted_nothing(source: str) -> bool:
    """True when the batch declares it consulted no refuted-patterns export.

    A prefix test, not equality: the honest form in practice is "not consulted
    -- <why>", and treating that as "an export we were not handed" would stop
    the digest being verified on exactly the batches where it can be.
    """
    low = _s(source).lower()
    return low in NOT_CONSULTED or low.startswith("not consulted")


def refuted_blob(path: str | None, source: str) -> bytes | None:
    """The bytes inputs_digest is computed over, or None when unavailable.

    None is not an error: the batch names an export we were not handed, so the
    digest is recorded but unchecked. Reporting an unchecked digest as verified
    would be the exact failure this repo audits for.
    """
    if _consulted_nothing(source):
        return b""
    if not path:
        return None
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError:
        return None


def load_refuted(path: str | None) -> list[dict]:
    """Negative constraints exported from a Mizan registry (AD4 feedback loop)."""
    if not path:
        return []
    try:
        data = yaml.safe_load(open(path, "r", encoding="utf-8"))
    except Exception:
        return []
    pats = (data or {}).get("refuted_patterns") or []
    return [p for p in pats if isinstance(p, dict)]


def _is_placeholder(text: str) -> bool:
    low = text.lower()
    return any(mark in low for mark in PLACEHOLDER_MARKERS)


def _flagged(value: str) -> bool:
    return _s(value).lower().startswith("flagged")


def check(data: dict, lang: str,
          refuted: list[dict] | None = None,
          refuted_bytes: bytes | None = None) -> tuple[list[str], list[str]]:
    """Return (violations, warnings). See the module docstring for why two."""
    errs: list[str] = []
    warns: list[str] = []
    batch = data.get("batch") or {}
    seeds = [s for s in (data.get("seeds") or []) if isinstance(s, dict)]

    # --- batch-level -----------------------------------------------------
    if not _s(batch.get("problem")):
        errs.append(m("batch_no_problem", lang))
    if not _s(batch.get("symmetry_check")):
        errs.append(m("batch_no_symmetry", lang))

    # G11 — the schema describes this field as required and the validator
    # never read it, so a batch could claim AD4 "clear" on every seed with
    # nothing behind it. Same shape as G6: an explicit "not consulted" is an
    # honest answer, an absent field is not an answer at all.
    if not _s(batch.get("refuted_patterns_source")):
        errs.append(m("G11_no_refuted_source", lang))

    # G12 — generation conditions. A pinned seed does NOT make an LLM draw
    # reproducible, and this rule deliberately does not pretend otherwise: it
    # only demands that the conditions be RECORDED, so two runs can be shown
    # to have seen the same problem and the same refuted export. Same shape as
    # G6 and G11 — "fresh" and "unknown" are answers, absence is not.
    errs += _check_generation(batch, refuted_bytes, lang)
    warns += _check_generation_warnings(batch, lang)

    ops = {_s(s.get("operator")).upper() for s in seeds if _s(s.get("operator"))}
    declared = {_s(o).upper() for o in (batch.get("operators_used") or [])}
    all_ops = ops | declared
    if seeds and len(all_ops) < 3:
        errs.append(m("batch_few_operators", lang, n=len(all_ops),
                      ops=", ".join(sorted(all_ops)) or "-"))

    # W3 — the schema asks symmetry_check to NAME the seed that breaks the
    # thesis. A non-empty field satisfies the letter of that; naming a seed
    # that exists is what makes the claim checkable against something.
    sym = _s(batch.get("symmetry_check"))
    ids = [_s(s0.get("id")) for s0 in seeds if _s(s0.get("id"))]
    if sym and ids and not any(i in sym for i in ids):
        warns.append(m("W3_symmetry_id_unknown", lang))

    # W2 — not an error: a one-seed batch, or a genuinely clean sweep, can
    # legitimately be all H-aday. It is a shape worth a second look.
    tiers = [_s(s0.get("tier")) for s0 in seeds]
    if len(seeds) >= 2 and all(t == "H-aday" for t in tiers):
        warns.append(m("W2_all_haday", lang, n=len(seeds)))

    # --- seed-level ------------------------------------------------------
    for s in seeds:
        sid = s.get("id")
        tier = _s(s.get("tier"))
        if tier and tier not in VALID_TIERS:
            errs.append(m("bad_tier", lang, id=sid, tier=tier))
        op = _s(s.get("operator")).upper()
        if op and op not in VALID_OPERATORS:
            errs.append(m("bad_operator", lang, id=sid, op=op))

        # unfilled template detection
        for field in ("claim", "illet", "breaking_point"):
            if _is_placeholder(_s(s.get(field))):
                errs.append(m("placeholder", lang, id=sid, field=field))

        # G1
        if not _s(s.get("illet")):
            errs.append(m("G1_no_illet", lang, id=sid))

        # G2
        if tier == "H-aday" and not _s(s.get("breaking_point")):
            errs.append(m("G2_no_breaking_point", lang, id=sid))

        # G8 — the refutation condition. Constraint 3 of SKILL.md: "if no test
        # can be designed, the idea stays [S]". Until now the schema required
        # the breaking point but not the test that kills the idea.
        test = _s((s.get("cheapest_refutation") or {}).get("test"))
        if tier == "H-aday" and (not test or _is_placeholder(test)):
            errs.append(m("G8_no_test", lang, id=sid))

        # G9 — constraint 4 is UNCONDITIONAL: "not searched" is honest, but
        # then the idea cannot be H-aday. G3 covers only the narrower
        # superiority-claim gate, which left this open.
        if tier == "H-aday" and not (s.get("prior_art") or {}).get("searched"):
            errs.append(m("G9_no_prior_art_search", lang, id=sid))

        # W1 — a precise-looking threshold with no judge behind it.
        arb_cls = _s(((s.get("arbiter") or {}) if isinstance(s.get("arbiter"), dict)
                      else {}).get("class")).lower()
        if arb_cls in {"author", "none"} and NUMERIC_THRESHOLD.search(
                _s(s.get("threshold_proposal"))):
            warns.append(m("W1_threshold_without_judge", lang, id=sid, cls=arb_cls))

        # W4 — O5 changes regime by definition; the scope caveat is the part
        # that stops a reduced-scale finding becoming a main-regime claim.
        if op == "O5" and not _s(s.get("scope_caveat")):
            warns.append(m("W4_O5_no_scope", lang, id=sid))

        errs += _check_prior_art(s, sid, tier, lang)
        errs += _check_refutation(s, sid, lang)
        errs += _check_arbiter(s, sid, tier, lang)
        errs += _check_sweep(s, sid, tier, lang)
        errs += _check_refuted_relatives(s, sid, tier, refuted or [], lang)

    errs += _check_discards(data, batch, lang)

    check.n_seeds = len(seeds)  # type: ignore[attr-defined]
    return errs, warns


def _check_discards(data: dict, batch: dict, lang: str) -> list[str]:
    """G7 — the discard list is part of the deliverable, present even when empty.

    Deliberately required rather than optional. SKILL.md's own measured
    finding is that this section is what disappears first under a host that
    rewards agreement, and it disappears without leaving a trace: an empty
    section and an unwritten one look identical. A key that must be there
    turns that invisible absence into a failing check.

    What it cannot do, stated for the same reason the rest of this tool
    states it: it verifies that discards were RECORDED, never that the
    right ideas were discarded.
    """
    if "discards" not in data:
        return [m("G7_no_discards", lang)]
    discards = data.get("discards")
    if discards is None:
        discards = []
    if not isinstance(discards, list):
        return [m("G7_no_discards", lang)]

    if not discards:
        if not _s(batch.get("discards_note")):
            return [m("G7_empty_without_note", lang)]
        return []

    errs: list[str] = []
    for i, d in enumerate(discards, 1):
        if not isinstance(d, dict):
            errs.append(m("G7_discard_incomplete", lang, i=i, field="claim, reason"))
            continue
        missing = [f for f in ("claim", "reason")
                   if not _s(d.get(f)) or _is_placeholder(_s(d.get(f)))]
        if missing:
            errs.append(m("G7_discard_incomplete", lang, i=i, field=", ".join(missing)))
    return errs


def _check_prior_art(s: dict, sid: Any, tier: str, lang: str) -> list[str]:
    """G3 — the prior-art gate on any superiority/originality claim."""
    errs: list[str] = []
    if not s.get("claims_superiority"):
        return errs
    pa = s.get("prior_art") or {}
    if not pa.get("searched") and tier != "S":
        errs.append(m("G3_superiority_without_prior_art", lang, id=sid, tier=tier or "-"))
    strongest = _s(pa.get("strongest_relative"))
    if not strongest or _is_placeholder(strongest):
        errs.append(m("G3_no_strongest_relative", lang, id=sid))
    elif not _s(pa.get("discrimination_test")):
        errs.append(m("G3_no_discrimination_test", lang, id=sid))
    return errs


def _check_refutation(s: dict, sid: Any, lang: str) -> list[str]:
    """G4 — capacity-confound control arm."""
    cr = s.get("cheapest_refutation") or {}
    if not cr.get("adds_capacity"):
        return []
    ctrl = _s(cr.get("matched_budget_control"))
    if not ctrl or ctrl.lower().startswith("not applicable"):
        return [m("G4_capacity_no_control", lang, id=sid)]
    return []


def _check_arbiter(s: dict, sid: Any, tier: str, lang: str) -> list[str]:
    """G5 — the judge behind the proposed threshold. Mirrors Mizan R8."""
    errs: list[str] = []
    arb = s.get("arbiter")
    if not isinstance(arb, dict) or not _s(arb.get("class")):
        return [m("G5_no_arbiter", lang, id=sid)]
    cls = _s(arb.get("class")).lower()
    if cls not in ARBITER_CLASSES:
        return [m("G5_bad_class", lang, id=sid, cls=cls)]
    who = _s(arb.get("who"))
    if not who or _is_placeholder(who):
        errs.append(m("G5_no_who", lang, id=sid, cls=cls))
    if cls == "none" and tier not in {"", "S"}:
        errs.append(m("G5_none_leaves_S", lang, id=sid, tier=tier))
    if cls in {"instrument", "third_party"} and not _s(arb.get("calibration")):
        errs.append(m("G5_no_calibration", lang, id=sid, cls=cls))
    # G10 — ported from the sibling Mizan validator, which has caught this
    # since R8 shipped. The two repos had each solved something the other
    # had not; this was Kiyas' side of that gap.
    if cls in {"author", "none"} and arb.get("independent_of_author") is True:
        errs.append(m("G10_independence_contradiction", lang, id=sid, cls=cls))
    return errs


def _check_sweep(s: dict, sid: Any, tier: str, lang: str) -> list[str]:
    """G6 — the AD1..AD6 sweep is recorded, and a flag blocks H-aday."""
    errs: list[str] = []
    sweep = s.get("antipattern_sweep")
    if not isinstance(sweep, dict) or not sweep:
        return [m("G6_sweep_missing", lang, id=sid)]
    missing = [k for k in SWEEP_KEYS if not _s(sweep.get(k))]
    if missing:
        errs.append(m("G6_sweep_incomplete", lang, id=sid, keys=", ".join(missing)))

    # Flags do not all mean the same thing. AD1 and AD4 FORCE a tier; AD2
    # forces discard-or-S; AD5 and AD6 do not block promotion at all — they
    # demand that a caveat be carried WITH the seed. Treating every flag as a
    # blocker would push authors to leave the sweep silent, which is worse
    # than a flagged seed that states its scope.
    if _flagged(sweep.get("AD1_notation_coincidence")) and tier not in {"NK", "S"}:
        errs.append(m("G6_AD1_requires_NK", lang, id=sid, tier=tier or "-"))
    if _flagged(sweep.get("AD2_surface_resonance")) and tier != "S":
        errs.append(m("G6_AD2_requires_S", lang, id=sid, tier=tier or "-"))
    if _flagged(sweep.get("AD4_refuted_relative")) and tier != "GB":
        errs.append(m("G6_AD4_requires_GB", lang, id=sid, tier=tier or "-"))
    if _flagged(sweep.get("AD5_scale_leak")) and not _s(s.get("scope_caveat")):
        errs.append(m("G6_AD5_no_scope", lang, id=sid))
    if _flagged(sweep.get("AD6_trace_base_rate")) and not _s(s.get("trace_base_rate")):
        errs.append(m("AD6_no_base_rate", lang, id=sid))
    return errs


def _check_generation(batch: dict, refuted_bytes: bytes | None, lang: str) -> list[str]:
    """G12 — the batch records how it was drawn, and the record is consistent."""
    gen = batch.get("generation")
    if not isinstance(gen, dict) or not gen:
        return [m("G12_no_generation", lang)]

    errs = []
    for field in ("seed", "host"):
        if not _s(gen.get(field)):
            errs.append(m("G12_no_field", lang, field=field))

    claimed = _s(gen.get("inputs_digest"))
    # Verifiable in exactly two situations: the batch consulted nothing (the
    # empty input hashes without any file), or the export was passed with
    # --refuted. Otherwise the digest is recorded but unchecked, and saying so
    # is better than implying it was verified.
    if claimed and refuted_bytes is not None:
        actual = inputs_digest(_s(batch.get("problem")), refuted_bytes)
        if claimed != actual:
            errs.append(m("G12_digest_mismatch", lang, claimed=claimed, actual=actual))
    return errs


def _check_generation_warnings(batch: dict, lang: str) -> list[str]:
    gen = batch.get("generation")
    if not isinstance(gen, dict):
        return []
    seed = _s(gen.get("seed"))
    if seed and seed.lower() != "fresh" and not _s(gen.get("inputs_digest")):
        return [m("W5_pinned_seed_no_digest", lang, seed=seed)]
    return []


def _check_refuted_relatives(s: dict, sid: Any, tier: str,
                             refuted: list[dict], lang: str) -> list[str]:
    """AD4 — the negative-constraint feedback loop, when an export is supplied.

    Deliberately crude: keyword overlap against exported refuted patterns.
    It is a prompt to look, not a verdict; false positives are cheap and a
    missed relative is the expensive error.
    """
    if not refuted or tier == "GB":
        return []
    # Only the idea itself — claim, illet, and the test. Methodological
    # boilerplate (the control arm, the calibration note) names mechanisms it
    # is controlling FOR, and matching on that produces false positives on
    # every well-specified seed.
    text = " ".join([
        _s(s.get("claim")),
        _s(s.get("illet")),
        _s((s.get("cheapest_refutation") or {}).get("test")),
    ]).lower()
    errs: list[str] = []
    for pat in refuted:
        keys = [_s(k).lower() for k in (pat.get("keywords") or []) if _s(k)]
        if keys and sum(1 for k in keys if k in text) >= 2:
            errs.append(m("GB_known_refuted", lang, id=sid,
                          pat=pat.get("id") or pat.get("title") or "?"))
    return errs


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Kıyas seed G1–G7 validator")
    ap.add_argument("seeds", help="path to a kiyas-seed.yaml")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--refuted", metavar="PATH",
                    help="refuted-patterns.yaml exported from a Mizan registry (AD4 check)")
    ap.add_argument("--strict", action="store_true",
                    help="treat W1-W5 warnings as violations (CI runs strict; local runs do not)")
    args = ap.parse_args(argv)

    # The catalog carries Turkish text and a ✗ glyph; ensure UTF-8 output even
    # on legacy Windows code pages (cp1254 etc.).
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            pass

    try:
        data = load(args.seeds)
    except Exception as exc:
        sys.stderr.write(f"parse error: {exc}\n")
        return 2

    errs, warns = check(
        data, args.lang, load_refuted(args.refuted),
        refuted_blob(args.refuted, (data.get("batch") or {}).get("refuted_patterns_source") or ""))
    n = getattr(check, "n_seeds", 0)

    if args.strict and warns:
        errs = errs + warns

    if errs:
        for e in errs:
            print("  ✗ " + e)
        # Warnings are shown next to violations too. Hiding them until the
        # blocking problems are fixed would make a second run reveal issues
        # that were already known, which is how a warning gets ignored.
        if not args.strict:
            for w in warns:
                print("  ! " + w)
        print(m("found", args.lang, n=len(errs)))
        if args.strict and warns:
            print(m("warn_strict", args.lang, n=len(warns)))
        return 1

    print(m("clean", args.lang, n=n))
    if warns:
        for w in warns:
            print("  ! " + w)
        print(m("warn_header", args.lang, n=len(warns)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
