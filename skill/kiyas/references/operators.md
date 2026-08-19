# Kıyas — Generative Operators, Anti-Pattern Sweep, Mizan Seed

> **[Revised 2026-07-22 — A1/A3/A4]** The operational half of SKILL.md's A1–A4
> patches lives here: (A1) **Prior art** + **discrimination test** fields in
> the output contract and the seed template; (A3) instrument-specific
> calibration nuance in AD1 (thresholds are not inherited across instruments);
> (A4) the new **AD6 — trace base-rate prior**; plus the **capacity-control
> arm** (A2) and **trace base-rate prediction** (A4) fields in the seed
> template. The seven operators and the analogical core did not change.

> **[Revised 2026-08-19 — G8/G9]** §2's contract is now enforced where it was
> only stated: an `[H-aday]` needs its cheapest refutation and a prior-art
> search, both mandatory in this file since v1.0 and neither checked until
> now. The seven operators are unchanged.

> **[Revised 2026-08-19 — G7]** §2's contract now states that the batch
> carries its discards, and the schema enforces it. The seven operators and
> the analogical core are unchanged.

> **[Revised 2026-07-23 — G1–G6]** §2's contract and §4's template have a
> machine-readable twin in `schemas/kiyas-seed.yaml`, enforced by
> `tools/kiyas_validate.py`. The prose below stays authoritative for *how to
> think*; the schema is what a project commits to a repo. §3's flags are not
> equal in force — AD1/AD2/AD4 force a tier, AD5/AD6 require a caveat to
> travel with the seed. That distinction is deliberate: if every flag blocked
> promotion, authors would learn to leave the sweep silent, which is worse
> than a flagged seed that states its scope.

Contents:
1. The seven generative operators (when / how / worked example)
2. The output contract (every idea leaves in this envelope)
3. The anti-pattern sweep list
4. The Mizan preregistration-seed template

Worked examples are drawn from the user's SpectralLM/GS-SSM project; the goal
is to give the operator a concrete feel, not to re-assert those results.

---

## 1. The seven generative operators

Use **at least three different operators** in a single generation. Diversity
comes from operator choice, not from saying "more analogies".

### O1 — Kıyas (analogy transfer) [core]
- **When:** the target problem's structure resembles that of a known domain.
- **How:** Asl (source domain, structure known) → Far' (target problem). Then
  isolate the **illet**: which *structural* property is being carried over? If
  you cannot name the illet, this is not O1 but surface resonance — discard it.
- **Example (project):** Asl = Kuramoto phase synchronization (physics);
  Far' = "attention" in sequence modeling. Illet = *selective alignment among
  components produces a context-dependent weight*. Breaking point:
  synchronization is periodic/autonomous dynamics, language is aperiodic and
  input-driven → the phase-value part does not transfer (and indeed phase came
  out "largely redundant" in Mizan). The illet survived (selective
  contraction), the surface (phase mysticism) was refuted — this is the
  operator used correctly.

### O2 — Inversion
- **When:** anywhere a direction/causality/sign is treated as obvious.
- **How:** flip the default arrow. "A produces B" → "B selects/constrains A".
- **Example (project):** "the state *carries* past tokens" (the retriever
  image) → inverted, "the past *narrows* the state" (a lossy summarizer). The
  inverted reading turned out consistent with HG31's refutation: the state does
  not carry distant-token identity, it keeps the near horizon readable.
  Inversion usually makes a hidden assumption visible.

### O3 — Constraint relaxation
- **When:** anywhere the sentence "I can't because of X" gets said.
- **How:** temporarily remove that constraint; how does the space open? Then
  write down why the constraint existed and what relaxing it costs.
- **Example (project):** in HG34 the Gershgorin stability constraint pinned
  coupling to |c| ≤ ~0.03 → weak coupling turned out decorative. Relaxation:
  "guarantee stability another way (unitary mixing, ρ ≤ 1 preserved) → open up
  full-strength coupling". Cost: parametrization complexity. This directly
  produced the HG34-refined preregistration.

### O4 — Limit / edge case
- **When:** it is unclear *why* a mechanism works.
- **How:** push a parameter to 0 or ∞. What breaks, what simplifies, what
  degenerates? What remains at the limit is the core mechanism.
- **Example (project):** the HG32 minimal core is exactly this — push
  SiLU/conv/rotation/mode to 0 one at a time, leave only |ā|. If the ceiling
  still breaks at the limit, the irreducible mechanism is selective damping.
  The limit case turns "which component bears load" into an ablation.

### O5 — Scale transfer
- **When:** there is a finding at scale/regime X; what happens in another?
- **How:** take the mechanism, change the scale/context length/dimension, write
  a prediction.
- **Example (project):** at seq256 "there is no knee" (state utility does not
  grow with context) → transfer to seq1024: "does the knee rise in long
  context?" (HG13-d). Scale transfer binds a reduced-scale finding to a
  main-regime preregistration; the scope caveat is mandatory.

### O6 — Combination (collision)
- **When:** two separate lines run in parallel and their combination has not
  been considered.
- **How:** force both frames through the same apparatus. Is the interaction
  additive, sub-additive, or super-additive?
- **Example (project):** input-dependent phase (HG28) + input-dependent
  amplitude (HG28-b) had been measured separately → combine: a 2×2 factorial
  (HG35). Result was sub-additive (phase redundant given amplitude).
  Combination turns "what do both do together" into an interaction term — one
  of the highest information-value moves.

### O7 — Substrate swap
- **When:** a function does not work / is blocked on one substrate.
- **How:** hold the function fixed, change the substrate/instrument.
- **Example (project):** "learning at inference" had died on the phase
  substrate (X1: phases frozen, PPL undisturbed). Substrate swap: move the same
  function (inference-time adaptation) from phase to the *state + readout
  layer* substrate → HG12, the first positive evidence (+4.45%). A substrate
  change is the most common way to revive a dead idea.

---

## 2. The output contract (every idea leaves in this envelope)

```
IDEA: <one sentence, refutable claim>
Operator: <O1..O7>
Illet: <the structural equivalence CARRYING the analogy/relation — NOT surface
  resemblance>
Breaking point: <where the analogy/relation stops holding — MANDATORY>
Cheapest refutation: <the smallest test that kills it; a Mizan preregistration
  seed. [A2] if the test adds capacity/parameters, a MATCHED-BUDGET control arm
  is MANDATORY>
Arbiter: <who returns the verdict: runtime / instrument / third_party / author
  / none, plus the concrete judge. author or none caps the seed — say so>
Prior art: <closest literature lineage, name+year; if a SUPERIORITY claim is
  made, name the strongest relative — if that rival is not in the comparison
  set, the tier stays [S]>
Tier: [S] / [H-aday] / [NK] / [GB]
```

If the Illet line is empty the idea was not generated — discard it, do not even
call it "decorative". If the Prior art line says "not searched", a
superiority/originality claim CANNOT be `[H-aday]` [A1].

The machine-readable form of this envelope is `schemas/kiyas-seed.yaml`; the
checker is `tools/kiyas_validate.py` (G1–G9, plus non-blocking W1–W4). It verifies that the fields are
filled, never that they are true — see SKILL.md §"The runtime arbiter".

**The batch also carries its discards [G7].** Alongside the seeds, record what
was weighed and refused, each entry naming the idea and the reason it was
refused — the anti-pattern that caught it (AD1..AD6) or the prior art that
already occupies it. The block is required even when nothing was discarded, in
which case say so and name what was considered. A batch listing only survivors
is indistinguishable from one where nothing was ever weighed.

---

## 3. The anti-pattern sweep list

Run every generated idea through this; take whatever flag catches.

### AD1 — Notation coincidence → `[NK]`
- **What:** a numeric/symbolic equivalence that holds only in an arbitrary
  unit/basis/representation.
- **Test:** *change the unit/basis/representation/**instrument**; does the
  equivalence survive?*
- **Example (project):** golden angle 137.5° ≈ 1/α 137.036 → a 5600% gap in
  radians. A unit-dependent coincidence, not structure. Such an equivalence
  never becomes `[H-aday]` without an `[NK]` flag.
- **Instrument-specific calibration [A3]:** a threshold/margin/NULL is derived
  from the OWN null distribution of the instrument in use; it is NOT INHERITED
  across instruments (MI-nat ≠ probe-R² ≠ AUC ≠ pseudospectral abscissa). A
  seed carrying a threshold from a different instrument takes an `[NK]` flag
  and cannot be `[H-aday]` until corrected.

### AD2 — Surface resonance → discard or `[S]`
- **What:** an analogy that sounds deep but whose illet cannot be named.
- **Test:** *can I say, in one sentence, what maps to what and why it bears
  load?* If not, it is ornament.
- **Example (project):** "Kuramoto = meaning synchronization" — poetic but
  illet-less; the load-bearing version was "selective alignment =
  context-dependent weight" (the O1 example).

### AD3 — Confirmation bias → add symmetry
- **What:** every candidate generated flatters the current thesis.
- **Test:** does at least one candidate *break* the current thesis? If not,
  generate one.

### AD4 — Relative of a past refutation → `[GB]`
- **What:** the idea is a relative of a pattern already marked `[R]` in Mizan.
- **Test:** scan the project's refuted-patterns list — export it from a
  registry with `mizan_export_refuted.py`, then run
  `kiyas_validate.py --refuted refuted-patterns.yaml`. If there is kinship,
  generate with a `[GB]` warning or drop the idea. A match is a prompt to look,
  not a verdict.

### AD5 — Scale/regime leak → scope caveat
- **What:** turning an idea from one regime (reduced scale) into a claim about
  another.
- **Test:** at which scale will the prediction be verified? Write the caveat
  into the seed (`scope_caveat`). This flag does not block promotion; a missing
  caveat does.

### AD6 — Trace base-rate prior → write the base rate into the prediction [A4]
- **What:** generating a new member of a many-negatives research trace (e.g.
  "the geometry line is 7/7 negative") without writing that trace's base rate
  into the preregistration.
- **Test:** if a trace has ≥N consistent negatives, the **honest base rate**
  (≈ hits/N) is written EXPLICITLY into the preregistered prediction; the new
  seed's prior is anchored to that base.
- **Out-of-distribution nuance (critical):** the base rate is valid only for
  the cell the trace actually SAMPLED. If the new seed sits in a regime the
  trace never entered (e.g. the 7 negatives were norm-preserving/weak-coupling
  while the seed is norm-BREAKING/non-normal), the base is
  **out-of-distribution** for that seed — a low base does NOT guarantee a
  strong null prior. Write this two-sided: "base ≈0/N but the trace never
  sampled this cell".

---

## 4. The Mizan preregistration-seed template

Turn `[H-aday]` ideas into seeds that paste straight into a Mizan Registry
Entry (Kıyas stops here; the tier is Mizan's/the user's business):

```markdown
### HX — <idea name> `[H]` `[preregistration seed — Kıyas O# generation, YYYY-MM-DD]`
*(Origin: Kıyas, operator O#, <problem sentence>. Illet: <...>)*
- Formal: <refutable claim>
- Metric: <what, with which instrument — file/script/data>
- Arbiter: <runtime / instrument / third_party / author / none + the concrete
  judge + verdict latency. Mizan R8 will demand this field; a seed that carries
  it arrives complete>
- Capacity-control arm [A2]: <symmetric arm giving the extra budget to a
  generic channel (amplitude/diagonal/hidden dim); promotion rule:
  Δ(target) − Δ(generic capacity) ≥ threshold. If the test adds NO capacity,
  write "not needed">
- Threshold (proposal, Mizan locks it): <numeric decision rule; from the
  instrument's OWN null — not inherited [A3]>
- Refutation: <which result kills it; two-sided informativeness>
- Prior art (named): <closest lineage, name+year>
- Discrimination test [A1]: <the strongest relative; is it in the comparison
  set; how the claimed distinction gets tested against that rival>
- Trace base-rate prediction [A4]: <if a relevant trace exists, the base rate
  plus the in-/out-of-distribution caveat>
- Breaking point (carried from Kıyas): <the analogy's limit>
- Anti-pattern flag: [NK]/[GB]/AD5/AD6/none
- Cost: <rough effort>
- STATUS: ⏳ Kıyas seed — awaiting Mizan preregistration
```
