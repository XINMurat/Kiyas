#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kıyas ledger — survival rate of generated seeds, computed instead of claimed.

SKILL.md states the honest success metric for Kıyas: the survival rate of
Kıyas-generated [H-aday] seeds inside a Mizan registry, compared against
free brainstorming. Nothing in this repo recorded that, which left the
skill's own central claim at [S] with no path off it. This tool closes the
loop mechanically: it reads a ledger of seeds and their final Mizan tiers
and prints the rate.

What it does NOT establish, stated up front because the methodology
requires it: without a control arm (the same problems attacked by free
brainstorming, scored by the same registry), a survival rate is a
descriptive number, not evidence that the Kıyas discipline caused it. Every
report below therefore carries a permanent [KKE] until such an arm exists.
An arm marked `control: true` in the ledger activates the comparison.

Usage:
    python tools/kiyas_ledger.py ledger/kiyas-ledger.yaml
    python tools/kiyas_ledger.py --lang tr ledger/kiyas-ledger.yaml

Exit code 0 always (this is a reporter, not a gate) unless the file cannot
be parsed (2).

Dependency: PyYAML  (pip install pyyaml)
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML is required. Install it with: pip install pyyaml\n")
    sys.exit(2)

# A seed "survived" if the Mizan registry it entered promoted it to K, or it
# still stands as a live H. Refuted (R) is a first-class outcome, not a
# failure of the generator — but it does not count as survival either.
SURVIVED = {"K", "H"}
CLOSED = {"R", "KKE", "Y"}

TXT = {
    "header": ("Kıyas survival ledger — {path}", "Kıyas sağ-kalım defteri — {path}"),
    "arm": ("Arm: {name} ({n} seeds registered)", "Kol: {name} ({n} tohum kayıtlı)"),
    "rate": ("  survival: {s}/{n} = {pct:.0%}  (K:{k} H:{h} R:{r} other:{o})",
             "  sağ-kalım: {s}/{n} = {pct:.0%}  (K:{k} H:{h} R:{r} diğer:{o})"),
    "pending": ("  pending (not yet registered or undecided): {n}",
                "  bekleyen (henüz kaydedilmemiş veya karara bağlanmamış): {n}"),
    "nocontrol": (
        "\n[KKE] No control arm in this ledger. A survival rate without a\n"
        "      free-brainstorm arm scored by the same registry describes the\n"
        "      record; it does not show the discipline caused it. Add entries\n"
        "      with `control: true` to activate the comparison.",
        "\n[KKE] Bu defterde kontrol kolu yok. Aynı registry tarafından puanlanan\n"
        "      serbest-brainstorm kolu olmadan sağ-kalım oranı kaydı betimler;\n"
        "      disiplinin bunu SAĞLADIĞINI göstermez. Karşılaştırmayı açmak için\n"
        "      `control: true` girdileri ekle.",
    ),
    "compare": ("\nKıyas {a:.0%} vs control {b:.0%} over {na}/{nb} registered seeds.\n"
                "Still [H], not [K]: assignment was not randomized and n is small.",
                "\nKıyas {a:.0%} — kontrol {b:.0%} ({na}/{nb} kayıtlı tohum).\n"
                "Yine de [K] değil [H]: atama rastgelelenmedi ve n küçük."),
    "empty": ("Ledger has no entries yet. Record seeds as they enter a registry.",
              "Defter henüz boş. Tohumları bir registry'ye girdikçe kaydet."),
    "underpowered": (
        "\n[S] n < {min} in at least one arm — reporting a rate here would be\n"
        "    the curated-anecdote failure the methodology forbids.",
        "\n[S] En az bir kolda n < {min} — burada oran raporlamak, metodolojinin\n"
        "    yasakladığı seçilmiş-örnek hatasıdır.",
    ),
}
MIN_N = 5


def t(key: str, lang: str, **kw: Any) -> str:
    en, tr = TXT[key]
    return (tr if lang == "tr" else en).format(**kw)


def _tier(e: dict) -> str:
    return str(e.get("final_tier") or "").strip().upper()


def summarize(entries: list[dict]) -> dict:
    decided = [e for e in entries if _tier(e) in SURVIVED | CLOSED]
    counts = Counter(_tier(e) for e in decided)
    n = len(decided)
    survived = sum(counts[k] for k in SURVIVED)
    return {
        "n": n,
        "survived": survived,
        "rate": (survived / n) if n else 0.0,
        "counts": counts,
        "pending": len(entries) - n,
    }


def report(data: dict, lang: str) -> None:
    entries = [e for e in (data.get("seeds") or []) if isinstance(e, dict)]
    if not entries:
        print(t("empty", lang))
        return

    kiyas = [e for e in entries if not e.get("control")]
    control = [e for e in entries if e.get("control")]

    for name, arm in (("kiyas", kiyas), ("control", control)):
        if not arm:
            continue
        s = summarize(arm)
        print(t("arm", lang, name=name, n=s["n"]))
        if s["n"]:
            c = s["counts"]
            other = s["n"] - c["K"] - c["H"] - c["R"]
            print(t("rate", lang, s=s["survived"], n=s["n"], pct=s["rate"],
                    k=c["K"], h=c["H"], r=c["R"], o=other))
        if s["pending"]:
            print(t("pending", lang, n=s["pending"]))

    if not control:
        print(t("nocontrol", lang))
        return

    a, b = summarize(kiyas), summarize(control)
    if min(a["n"], b["n"]) < MIN_N:
        print(t("underpowered", lang, min=MIN_N))
        return
    print(t("compare", lang, a=a["rate"], b=b["rate"], na=a["n"], nb=b["n"]))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Kıyas seed survival-rate reporter")
    ap.add_argument("ledger", help="path to kiyas-ledger.yaml")
    ap.add_argument("--lang", choices=["en", "tr"], default="en")
    args = ap.parse_args(argv)

    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            pass

    try:
        data = yaml.safe_load(open(args.ledger, "r", encoding="utf-8")) or {}
    except Exception as exc:
        sys.stderr.write(f"parse error: {exc}\n")
        return 2

    print(t("header", args.lang, path=args.ledger))
    report(data, args.lang)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
