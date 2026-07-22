#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kıyas seed validator — LLM-free static enforcement of hard rules G1–G6.

SCOPE, stated plainly because the methodology demands it: this tool is a
`runtime` arbiter for CONTRACT COMPLETENESS only. It checks that the illet
field is filled; it cannot check that the illet is true. Idea quality stays
with a human or a frontier model. Presenting this validator as a judge of
idea quality would be exactly the "threshold theatre" that Mizan R8 exists
to prevent — an arbiter-less domain wearing an arbiter-ed domain's clothes.

Bilingual: messages are emitted in the requested language (--lang tr|en).

Usage:
    python tools/kiyas_validate.py path/to/kiyas-seed.yaml
    python tools/kiyas_validate.py --lang tr seeds.yaml
    python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml

Exit code 0 = clean, 1 = violations found, 2 = usage/parse error.

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
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
    "clean": (
        "OK — {n} seed(s) checked, no G1–G6 violations.",
        "OK — {n} tohum kontrol edildi, G1–G6 ihlali yok.",
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


def check(data: dict, lang: str, refuted: list[dict] | None = None) -> list[str]:
    errs: list[str] = []
    batch = data.get("batch") or {}
    seeds = [s for s in (data.get("seeds") or []) if isinstance(s, dict)]

    # --- batch-level -----------------------------------------------------
    if not _s(batch.get("problem")):
        errs.append(m("batch_no_problem", lang))
    if not _s(batch.get("symmetry_check")):
        errs.append(m("batch_no_symmetry", lang))

    ops = {_s(s.get("operator")).upper() for s in seeds if _s(s.get("operator"))}
    declared = {_s(o).upper() for o in (batch.get("operators_used") or [])}
    all_ops = ops | declared
    if seeds and len(all_ops) < 3:
        errs.append(m("batch_few_operators", lang, n=len(all_ops),
                      ops=", ".join(sorted(all_ops)) or "-"))

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

        errs += _check_prior_art(s, sid, tier, lang)
        errs += _check_refutation(s, sid, lang)
        errs += _check_arbiter(s, sid, tier, lang)
        errs += _check_sweep(s, sid, tier, lang)
        errs += _check_refuted_relatives(s, sid, tier, refuted or [], lang)

    check.n_seeds = len(seeds)  # type: ignore[attr-defined]
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
    ap = argparse.ArgumentParser(description="Kıyas seed G1–G6 validator")
    ap.add_argument("seeds", help="path to a kiyas-seed.yaml")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    ap.add_argument("--refuted", metavar="PATH",
                    help="refuted-patterns.yaml exported from a Mizan registry (AD4 check)")
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

    errs = check(data, args.lang, load_refuted(args.refuted))
    n = getattr(check, "n_seeds", 0)

    if errs:
        for e in errs:
            print("  ✗ " + e)
        print(m("found", args.lang, n=len(errs)))
        return 1
    print(m("clean", args.lang, n=n))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
