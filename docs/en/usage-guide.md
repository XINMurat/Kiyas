# Kıyas Usage Guide

## 1. When to reach for it

Kıyas is for the moment a line of work stops moving: the obvious experiments
are done, the obvious framings are exhausted, and what is left is either
"try harder" or "try elsewhere". It is not a brainstorming toy — it costs more
per idea than free association, and that cost is the point.

Reach for it when:
- an experiment line has gone several rounds negative and you want to know
  whether the next member of that trace is worth running at all;
- two parallel lines have never been forced through the same apparatus;
- you suspect you are seeing a mechanism where there is only a coincidence;
- you want the argument AGAINST your current thesis stated well.

Do not reach for it to fill a slide with ten ideas. It will refuse to fill a
quota, and it should.

## 2. The two modes

**Generation.** You are stuck. The skill fixes the problem in one sentence,
picks at least three different operators, and returns 3–6 candidates in the
output contract. Diversity comes from operator choice, not from asking for
more analogies.

**Distillation.** You already have a pile of raw ideas. Each is pushed through
the same contract, tiered, flagged, and ordered by criticality ×
(information value / cost).

## 3. Hard rules (summary — G1–G9 in the schema)

1. Illet non-empty. An idea whose illet cannot be named was not generated.
2. Breaking point present before an idea can be a hypothesis candidate.
3. A superiority claim without a prior-art search stays speculative, and the
   strongest relative must be in the comparison set with a discrimination test.
4. A test that adds capacity carries a matched-budget control arm, or its
   positive result cannot be attributed to the targeted mechanism.
5. Every threshold proposal names its arbiter — the judge that returns the
   verdict (`runtime` / `instrument` / `third_party` / `author` / `none`).
   Self-judged stays capped; unjudged stays speculative.
6. The AD1–AD6 sweep is recorded, including explicit "clear". AD1/AD2/AD4
   force a tier; AD5/AD6 require a caveat to travel with the seed.
7. The batch records its **discards** — what was weighed and refused, and why.
   Required even when empty, in which case the batch says what it considered.
   A list of survivors alone cannot show that anything was weighed.
8. A hypothesis candidate carries the **cheapest refutation** that would kill
   it. If no test can be designed, the idea stays speculative.
9. A hypothesis candidate has had its **prior art searched**. "Not searched"
   is honest, but it caps the idea at speculative.

Four further checks **warn without blocking** (`--strict` makes them fail): a
numeric threshold with no judge behind it, a batch where every seed is a
hypothesis candidate, a symmetry check naming no seed, and a scale transfer
with no scope caveat. Each has legitimate exceptions, so the tool says look,
not halt — a single blocking channel teaches you to write around the rules.

## 4. Reading the tiers

| Tag | Means | What to do with it |
|---|---|---|
| `[S]` | Speculative | Keep it, do not act on it. Note what is missing. |
| `[H-aday]` | Hypothesis candidate | Paste into a Mizan registry as a preregistration. |
| `[NK]` | Notation-suspect | Run the unit/basis/instrument change before anything else. |
| `[GB]` | Fed-back | A relative of something already refuted. Check kinship deliberately. |

Nothing except `[H-aday]` should enter a registry.

## 5. Common mistakes

- **Treating the validator as a quality judge.** It checks that fields are
  filled. Filled is not true.
- **Threshold theatre.** Attaching a precise-looking number to a seed whose
  arbiter is the author, because the form of rigor is available even when its
  substance is not. Write "no instrument exists here" instead.
- **Silent sweeps.** Leaving AD fields blank because a flag feels like an
  admission of failure. A flagged seed with a stated scope is worth more than
  a silent one.
- **Quota filling.** Asking for ten ideas. You will get the ones that pass,
  and the count is not the deliverable.
- **Skipping symmetry.** Every candidate flattering the current thesis is a
  finding about the generation, not about the domain.

## 6. Wiring it to Mizan

Kıyas stops at the seed. Mizan locks thresholds, runs the audit, promotes or
refutes, and exports refuted patterns back. Concretely:

```bash
# before generating: know what is already dead
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml

# after generating: check the batch against those constraints
python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml

# after the registry decides: record it, wins and losses
python tools/kiyas_ledger.py ledger/kiyas-ledger.yaml
```

The ledger is where the project's own claim gets tested. Until it has entries
and a control arm, that claim is speculative and the tooling says so.
