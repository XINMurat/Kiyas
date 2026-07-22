---
name: kiyas
description: Disciplined ideation and analogical inference for research that is stuck. Use whenever the user wants to generate ideas, break through a blocked problem, find analogies or cross-domain relationships, reframe a question, brainstorm hypotheses, or explore "what else could explain this / what am I not seeing." Also use to open new experimental directions from a dead end, connect two unrelated fields, or turn a vague intuition into a testable hypothesis. Triggers include "fikir üret", "tıkandım", "analoji kur", "başka nasıl bakabilirim", "yeni yön", "bağlantı kur", "brainstorm", "ideate", "reframe", "what am I missing". The generative upstream partner of Mizan (mizan audits/refutes; kiyas generates candidates shaped for that audit). Every idea it produces ships ready to enter a Mizan registry as a preregistered [S]/[H] hypothesis.
---

# Kıyas — Disciplined Ideation and Analogical Inference

> **[Revised 2026-07-22 — A1–A4]** A 4-scenario test → 3 seeds → Mizan audit →
> prior-art lit-check cycle exposed and fixed three preregistration-hygiene
> gaps: (A1) prior-art declaration is mandatory and gates `[H-aday]`;
> (A2) capacity-confound control arm; (A3) instrument-specific calibration;
> (A4) trace base-rate prior (AD6). The analogical core did not change; what
> changed is the hygiene a candidate passes before entering Mizan.

> **[Revised 2026-07-23 — G1–G6]** The output contract became data. Seeds can
> now be written to `schemas/kiyas-seed.yaml` and checked mechanically by
> `tools/kiyas_validate.py`; the arbiter block is shared with Mizan's R8, so a
> seed leaves Kıyas already carrying the judge its registry will demand. See
> "The runtime arbiter" below for what that tool can and cannot judge.

Kıyas (Arabic/Turkish: analogical reasoning — the discipline of carrying a
ruling to a new case through a shared *illet*) is not free association. It aims
at **auditable idea generation**. Mizan weighs and refutes; Kıyas produces what
gets weighed — but produces every candidate Mizan-ready: with its illet, its
breaking point, its cheapest refutation, and its **named prior art**.

Write in the user's language. Keep the tier tags bilingual, exactly as in the
table below.

## Why discipline is needed (the reason this skill exists)

A language model is already a fluent analogy generator; telling it to "be
creative" adds nothing. The only thing Kıyas adds is **constraint**:

1. **Every idea names its illet.** Not surface resemblance, but the structural
   equivalence that *carries* the analogy. If it cannot be named, the idea is
   decorative — it does not count as generated.
2. **Every idea carries its breaking point.** Where the analogy stops holding.
   An analogy with no stated limit is ornament (see anti-pattern: surface
   resonance).
3. **Every idea ships with its cheapest refutation.** The smallest test that
   would kill it — which is directly a Mizan preregistration seed. If no test
   can be designed, the idea stays `[S]`.
4. **Every idea ships with named prior art.** The idea's closest literature
   lineage, declared with name + year. "Not searched" is a legal answer, but
   then the idea cannot be `[H-aday]` (see §"Generation mode — procedure",
   step 4). A superiority/originality claim that has not been tested against
   the *strongest* member of its prior art is decorative.
5. **Every idea is born `[S]`.** Kıyas presents nothing as evidence or finding.
   Promotion is Mizan's job.
6. **Symmetric generation.** An analogy that *breaks* the current hypothesis is
   sought as hard as one that flatters it (against confirmation bias).

If an idea cannot pass these constraints, it has not been generated — weak
ideas are not added to fill a quota (the generative counterpart of Mizan's
"three examples are selection bias" rule).

## Generative tiers (aligned with the Mizan table, bilingual)

| Tag | TR | EN | Meaning |
|---|---|---|---|
| `[S]` | Spekülatif | Speculative | Generated; has an illet but no test was designed/is designable, OR prior art was not searched |
| `[H-aday]` | Hipotez adayı | Hypothesis candidate | Illet + breaking point + cheapest refutation + **prior-art declaration** complete → ready for Mizan preregistration |
| `[NK]` | Notasyon-kuşkulu | Notation-suspect | The equivalence may depend on units/basis/representation/instrument — anti-pattern sweep is mandatory |
| `[GB]` | Geri-beslenen | Fed-back | A relative of a pattern/trace already marked `[R]` in Mizan — negative-constraint warning |

Nothing except `[H-aday]` passes into a Mizan registry as a preregistration.

## Two modes — decide which applies

**Generation mode (main).** The user is stuck and wants a new direction,
analogy, or frame. Apply the move menu (`references/operators.md`), produce 3–6
candidates under the output contract, tier them, run the anti-pattern sweep.
Output: `[H-aday]` ideas plus preregistration seeds that paste straight into
Mizan.

**Distillation mode.** The user already has a pile of raw ideas/analogies and
does not know which are worth testing. Push each through the output contract
(illet + breaking point + cheapest refutation + prior art), tier them, raise
`[NK]`/`[GB]`/AD6 flags, and order by criticality × (information value / cost).

If both are asked for ("generate, then tell me which is worth it"): generate
first, then distill.

## Generation mode — procedure

Read `references/operators.md` before the first generation (move menu + worked
examples + anti-pattern sweep). Then:

1. **Fix the problem in one sentence.** Name what is blocked and which
   constraint hurts. If unclear, ask one question, then generate.
2. **Pick at least three different operators** (`operators.md`). One operator
   gives one kind of idea; diversity comes from operator diversity, not from
   saying "ten analogies".
3. **Run each operator through the output contract:** Claim → Illet → Breaking
   point → Cheapest refutation → **Prior art** → Tier. If the illet cannot be
   named, DISCARD the idea; do not even call it decorative.
   - **Capacity-confound rule [A2]:** if the test adds parameters/capacity to a
     model, the cheapest refutation MUST include a **matched-budget control
     arm** — a symmetric arm giving the same extra budget to a generic channel
     (amplitude / diagonal / hidden dimension). Without it, a generic-capacity
     gain cannot be attributed to the targeted mechanism, and a positive result
     cannot be promoted to `[H]`. (Project lesson: HG28 input-dependent phase
     gained +6.75%, while the same extra projection spent on amplitude gained
     +16.4%; the gain was generic.)
4. **Anti-pattern sweep** (`operators.md` §3): notation coincidence (`[NK]`,
   with **instrument-specific calibration** — thresholds are not inherited
   across instruments [A3]); the illet test; kinship with a past `[R]`
   (`[GB]`); and the **trace base-rate prior** (AD6 [A4]: if a trace has ≥N
   consistent negatives, the honest base rate goes into the preregistered
   prediction).
   - **Prior-art gate [A1]:** a superiority/originality claim cannot be
     `[H-aday]` without a prior-art search — it stays `[S]`. The claimed
     distinction must be tested against the *strongest* member of the prior
     art; if that member is not in the comparison set, the seed is incomplete.
5. **Symmetry check:** do all your candidates flatter the current thesis? At
   least one must cut against it; otherwise this is confirmation bias —
   generate one.
6. **Hand off to Mizan:** present `[H-aday]` ideas as seeds that paste straight
   into the Mizan Registry Entry template (formal claim + metric + arbiter +
   capacity-control arm + threshold proposal + refutation + prior art +
   discrimination test + trace base-rate prediction). Kıyas stops here; tier
   promotion is Mizan's job and the user's.

## Distillation mode — procedure

1. Atomize the raw ideas (if one sentence holds two ideas, split it).
2. Apply the output contract to each; anything missing its illet OR its prior
   art stays `[S]`, with a note saying what is missing to make it
   testable/original.
3. Raise `[NK]`, `[GB]` and trace-base-rate (AD6) flags; if there is a
   superiority claim, apply the prior-art gate (A1).
4. Order by criticality × (information value / cost); cheapest-and-sharpest
   first.
5. Convert the top 1–3 candidates into Mizan preregistration seeds.

## The runtime arbiter — what the validator does and does not judge

The output contract has a machine-readable form (`schemas/kiyas-seed.yaml`)
and a checker (`tools/kiyas_validate.py`, rules G1–G6). Write seeds as YAML
when the batch is going into a project; prose is fine for a chat reply.

What it enforces: illet non-empty (G1); breaking point present for `[H-aday]`
(G2); the prior-art gate on superiority claims, including a named strongest
relative and a discrimination test (G3); the matched-budget control arm
whenever the test adds capacity (G4); an arbiter block using Mizan's five R8
classes (G5); and a recorded AD1–AD6 sweep, where AD1/AD2/AD4 force a tier
while AD5/AD6 demand that a caveat travel with the seed (G6).

What it cannot do, and what must be said whenever the tool is described: it
checks that the illet field is **filled**, never that the illet is **true**.
Contract completeness is machine-checkable; idea quality is not. Presenting
this validator as a judge of idea quality would be exactly the failure Mizan's
R8 exists to prevent — an arbiter-less domain wearing an arbiter-ed domain's
clothes.

**The arbiter block is the handoff.** Each seed names who returns the verdict
on its proposed threshold: `runtime` (deterministic executor) / `instrument`
(measurement independent of the author) / `third_party` (a judge other than
the author) / `author` (self-judged) / `none`. A seed whose only judge is its
own author will never be promoted to `[K]` by any honest registry; with
`none`, proposing a numeric threshold at all is theatre. Say so and leave the
seed at `[S]` — an honest `[S]` beats a number implying an oracle that does
not exist.

## The loop with Mizan (what binds the two skills into a system)

Kıyas generates → Mizan audits/preregisters/refutes → **refuted patterns come
back to Kıyas as negative constraints.** In practice:

- The project keeps a refuted-patterns list. Export it from a Mizan registry
  with `mizan_export_refuted.py` and consult it before generating:
  `kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml` flags seeds
  that resemble something already killed. A match is a prompt to check
  relatedness, never an automatic rejection — regenerate the idea with a
  `[GB]` flag, or drop it deliberately.
- The honest success metric: the survival rate of Kıyas-generated `[H-aday]`
  seeds in a registry, compared to free brainstorming. Record it in
  `ledger/kiyas-ledger.yaml` and read it with `tools/kiyas_ledger.py`. Note
  what that number is and is not: without a control arm it describes the
  record, it does not show the discipline caused it — the ledger prints a
  permanent `[KKE]` saying so until such an arm exists. This claim about Kıyas
  is itself `[S]` until the ledger has entries, and should be reported that way.

## Tone and framing rules

- Never present a generated idea as a finding. "This might be interesting" ≠
  "this is true".
- If the illet cannot be named, say so honestly: "this is surface resonance, I
  could not construct its illet" — better than manufacturing an ornate analogy.
- If prior art was not searched, write "not searched" and keep the tier at
  `[S]` — better than manufacturing a false originality claim.
- Few load-bearing ideas beat many decorative ones. Do not fill a quota.
- Metaphor is a source of intuition, not evidence (same principle as the
  project culture).
- Write in the user's language; keep tier tags bilingual.
- Treat an equivalence that looks unexpectedly deep with the same suspicion as
  an unexpectedly good experimental result (the generative counterpart of Mizan
  commitment 5): exhaust the notation-coincidence and surface-resonance
  alternatives first.

## Anti-patterns (refuse these politely)

- Generating an idea with no illet to fill a quota.
- Making an equivalence `[H-aday]` without running the notation-coincidence
  sweep.
- Inheriting a threshold/margin across instruments (MI-nat ≠ probe-R² ≠ AUC)
  [A3].
- Proposing a test that adds capacity/parameters without a matched-budget
  control arm — the gain may be generic (the HG28-b lesson) [A2].
- Making a superiority/originality claim `[H-aday]` without a prior-art search;
  leaving the real competitor (the strongest relative) out of the comparison
  set [A1].
- Generating a trace hypothesis without writing the base rate of a
  many-negatives research trace into the preregistered prediction [A4/AD6].
- Producing only analogies that confirm the current thesis and skipping the
  symmetry check.
- Presenting a generated `[S]` idea as "finding/direction proven" (a Mizan
  leak).
- Re-proposing a pattern that was already `[R]` without a `[GB]` flag.
- Attaching a precise-looking threshold to a seed whose arbiter is the author
  or nonexistent. The form of a verification loop without its judge is not
  rigor.

## References

- `references/operators.md` — each of the seven generative operators: when,
  how, and a worked example from the project; then the output contract
  (including prior art), the anti-pattern sweep list (AD1–AD6), and the Mizan
  preregistration-seed template. Read before the first generation.
- `schemas/kiyas-seed.yaml` — the output contract as data (rules G1–G6), with
  the arbiter block shared with Mizan R8.
