#!/usr/bin/env python3
"""Compute batch.generation.inputs_digest for a Kıyas batch.

WHAT A SEED IS AND IS NOT
-------------------------
A pinned seed does NOT make a Kıyas batch reproducible. The generator is a
language model; the same seed, the same problem and the same operators can
still produce different seeds, and a tool that promised otherwise would be
doing precisely what this family exists to refuse -- dressing an unverifiable
claim in the clothes of a verified one.

What `batch.generation` records is the CONDITIONS a batch was drawn under:
which seed value (or the honest "fresh"), which host drew it, and a digest of
the inputs it was drawn from. That makes two batches comparable -- you can
show that two runs saw the same problem and the same refuted-patterns export,
so a difference between them is a difference in the draw and not in the
inputs. It does not make the draw repeatable.

THE DIGEST
----------
    sha256(normalised problem + NUL + refuted-export bytes)[:16]

The problem is whitespace-normalised so that a reflow of the YAML block does
not change the digest. The refuted export is hashed as raw bytes; a batch that
consulted nothing hashes the empty string, which is why "not consulted"
batches stay verifiable with no file on hand.

    python tools/kiyas_digest.py batch.yaml
    python tools/kiyas_digest.py batch.yaml --refuted refuted-patterns.yaml
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - same guard as kiyas_validate.py
    print("PyYAML is required: pip install -r tools/requirements.txt", file=sys.stderr)
    raise SystemExit(2)

NOT_CONSULTED = {"not consulted", "none", "-"}


def normalise_problem(text: str) -> str:
    """Collapse whitespace so reflowing the YAML block cannot move the digest."""
    return re.sub(r"\s+", " ", (text or "").strip())


def inputs_digest(problem: str, refuted_bytes: bytes) -> str:
    h = hashlib.sha256()
    h.update(normalise_problem(problem).encode("utf-8"))
    h.update(b"\x00")
    h.update(refuted_bytes)
    return h.hexdigest()[:16]


def consulted_nothing(source: str) -> bool:
    """Must stay identical to kiyas_validate._consulted_nothing."""
    low = (source or "").strip().lower()
    return low in NOT_CONSULTED or low.startswith("not consulted")


def refuted_bytes_for(source: str, refuted_path: str | None) -> tuple[bytes, str]:
    """Return (bytes, how) or raise SystemExit with an actionable message."""
    if consulted_nothing(source):
        return b"", 'refuted_patterns_source starts with "not consulted" -> empty input'
    if refuted_path:
        with open(refuted_path, "rb") as f:
            return f.read(), f"refuted export {refuted_path}"
    raise SystemExit(
        "batch.refuted_patterns_source names an export, so the digest needs it:\n"
        f"  python tools/kiyas_digest.py <batch> --refuted {source.strip() or '<path>'}"
    )


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("batch", help="Kıyas batch YAML")
    ap.add_argument("--refuted", help="the refuted-patterns export the batch names")
    args = ap.parse_args(argv)

    with open(args.batch, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    batch = data.get("batch") or {}
    problem = batch.get("problem") or ""
    if not problem.strip():
        print("batch.problem is empty; the digest would not identify anything.", file=sys.stderr)
        return 1

    blob, how = refuted_bytes_for(batch.get("refuted_patterns_source") or "", args.refuted)
    digest = inputs_digest(problem, blob)
    print(f"inputs_digest: {digest}")
    print(f"  over: normalised batch.problem + {how}")
    print("  seed pinning records conditions, not reproducibility -- see the module docstring.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
