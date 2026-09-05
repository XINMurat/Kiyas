# Recovery — when the generation itself goes wrong

Read this when a run stops behaving: the validator did not run, a batch will
not produce a testable candidate, an equivalence looks too good, the problem
moved underneath the generation, or the session has gone soft.

`operators.md` describes generation working. This file describes it **failing**
— which is the more common case and the one that hides best, because a failed
generation and a successful one produce the same thing: a list of plausible
ideas. **Discipline is invisible from the outside.** That is the whole reason
the discard list is part of the deliverable, and it is the reason these ramps
are written down instead of improvised.

The ramps are `RR-nn`; `G-nn` and `AD-nn` already mean validator rules and
sweep items here, and a recovery ramp is neither.

```
TRIGGER      what you just observed
FIRST MOVE   what to do before anything else
FORBIDDEN    the shortcut that hides the failure instead of fixing it
OUTPUT       what you hand back -- never "sorted it out"
BACKED BY    the rule, gate or sweep item that catches you if you skip it
```

**Name the ramp in the deliverable.** A run that silently recovered has an
unmeasurable discard rate, and the discard rate is the only externally visible
evidence that anything was weighed.

---

## The failure classes these ramps exist for

The ramps are the remedies; these are the diseases. They are model failure
modes — a fluent analogy generator under pressure to look useful will produce
every one of them, and none of them announces itself.

| Class | How it shows up in a batch | Ramp |
|---|---|---|
| **Quota filling** | Six candidates because six was asked for; the last two have no illet | RR-06 |
| **Surface resonance** | An elegant resemblance with no structural equivalence carrying it | RR-05 |
| **Notation coincidence** | The equivalence lives in the units, the basis or the instrument, not in the mechanism | RR-03 |
| **Confirmation-only generation** | Every candidate flatters the thesis the user already holds | RR-04 |
| **Capacity smuggling** | The proposed test adds parameters; any gain would be generic | RR-12 |
| **Originality inflation** | A superiority claim whose strongest real competitor is absent from the comparison set | RR-05, RR-12 |
| **Tier leakage** | An `[S]` idea presented as a direction, a finding, or "the answer" | RR-00 |
| **Optimistic reporting** | "Validated", "checked against the refuted list" with no artifact behind it | RR-01 |
| **Rescue rewriting** | A seed came back `[R]`, so it is reworded until it reads like a different idea | RR-02 |
| **Context decay** | Hour two: candidates still flowing, the contract no longer applied to them | RR-09 |
| **Class-less escape** | The idea came from outside the batch, or a known-refuted pattern shipped anyway; it was absorbed, and nothing changed about what the next batch runs | RR-13 |

---

## RR-00 — You are about to promote your own idea

**TRIGGER.** You are about to call a generated candidate a finding, a
direction, "the most promising one", or rank the batch by how right the ideas
are rather than by information value over cost.

**FIRST MOVE.** Stop. **Kıyas does not promote.** Every idea is born `[S]`, and
the highest thing this skill can hand over is `[H-aday]` — a candidate ready
for preregistration. Promotion is Mizan's job and the user's. If you are
ranking, rank by criticality × (information value / cost), which is a statement
about the *test*, not about the truth of the idea.

**FORBIDDEN.** "This is the direction." Presenting the survivor of your own
discard pass as though surviving your own filter were evidence. Filling in an
arbiter class the seed has not earned so that it looks preregistration-ready.

**OUTPUT.** The tier as it stands, and the sentence that says what would move
it. If the batch has no `[H-aday]` in it, say that — a batch of `[S]` is an
honest batch, not a failed one.

**BACKED BY.** Commitment 5 (every idea is born `[S]`), the tier table
(nothing but `[H-aday]` enters a registry), G5/G10 (the arbiter block), the
"Mizan leak" anti-pattern.

---

## RR-01 — A promised artifact did not run

**TRIGGER.** No PyYAML, no shell; or `kiyas_validate.py`, `kiyas_ledger.py`
or the refuted-patterns export raised.

**FIRST MOVE.** Diagnose before substituting. Does the absence remove a
**capability** or a **convenience**? Without the validator, G1–G13 were not
checked — that is a capability, and "the seeds look complete to me" is exactly
the producer-side judgement the validator exists to replace. Without the
refuted-patterns file, the `[GB]` check did not happen; **`refuted_patterns_source`
then says "not consulted", which is the honest answer — silence is not an
answer at all** (G11).

**FORBIDDEN.** Writing a batch as prose and describing it as validated.
Claiming a `[GB]` sweep against a list you never opened.

**OUTPUT.** The constraint stated in the deliverable: which check did not run,
what the batch therefore cannot claim, and the fallback used. A batch produced
under a constraint is not a smaller batch; it makes a different claim.

**BACKED BY.** Operating assumptions (*never assume a tool exists*), G11.

---

## RR-02 — A seed came back refuted

**TRIGGER.** Mizan ran the preregistered test and the candidate failed its own
threshold, or the result landed at `[R]`.

**FIRST MOVE.** This is the loop working, not the loop breaking. Record it, and
**feed it back as a negative constraint**: the refuted pattern belongs in the
project's refuted-patterns list, where the next generation reads it. Then ask
the one question worth asking: was the *idea* wrong, or was the **illet**
wrong? An idea can fail while its structural equivalence still holds elsewhere
— and an illet that turned out not to carry is far more valuable to record,
because it invalidates a whole family of future candidates, not one.

**FORBIDDEN.** Rewording the seed until it reads as a different idea and
re-proposing it. Re-proposing a related pattern without a `[GB]` flag.
Treating the refutation as noise because the analogy still feels right.

**OUTPUT.** The `[R]` recorded at the source, the refuted-patterns list
updated, and — if the illet was the casualty — a note saying which future
candidates it rules out. That note is the highest-value artifact this skill
produces, and nothing in the generation path produces it.

**BACKED BY.** The Mizan loop (refuted patterns return as negative
constraints), `[GB]`, the "re-proposing a refuted pattern" anti-pattern.

---

## RR-03 — The equivalence looks unexpectedly deep

**TRIGGER.** An analogy lines up further than you expected: several quantities
map, the algebra rhymes, the diagram transfers.

**FIRST MOVE.** **Treat it with the same suspicion as an unexpectedly good
experimental result.** This is the generative counterpart of the
surprising-positive rule, and it is the moment this skill is most likely to
manufacture something ornate. Before anything else, exhaust the two cheap
alternatives:

1. **Notation coincidence** — does the equivalence survive a change of units,
   basis, representation or instrument? If it might not, the seed is `[NK]`
   and the sweep is mandatory. Thresholds and margins are **never inherited
   across instruments** (A3).
2. **Surface resonance** — name the illet out loud. If naming it requires the
   analogy's own vocabulary, there is no illet; there is a metaphor.

**FORBIDDEN.** Presenting depth of resemblance as strength of evidence.
Carrying a margin from one instrument to another because the shapes matched.

**OUTPUT.** Either a named illet that survives the sweep, or an `[NK]` flag
travelling with the seed, or a discard with the reason. Depth that survives the
sweep is worth more than depth that was never tested; depth that was never
tested is worth nothing at all.

**BACKED BY.** The anti-pattern sweep (`operators.md` §3), `[NK]`, A3,
commitment 6's symmetry logic applied to a flattering result.

---

## RR-04 — Every candidate agrees with the user

**TRIGGER.** The batch is complete and all of it supports the thesis the user
came in holding.

**FIRST MOVE.** This is confirmation bias with the generator's fingerprints on
it — the model is agreeing, and agreement is the failure mode a host
instruction to *be encouraging* produces silently. Generate at least one
candidate that **cuts against** the thesis, using a different operator, before
handing anything over.

**FORBIDDEN.** Calling the symmetry check done because you looked. Producing a
token counter-analogy with no illet to satisfy the rule — that is quota filling
wearing a symmetry badge.

**OUTPUT.** At least one candidate whose success would damage the current
direction, held to the same contract as the rest. If genuinely none can be
constructed, say so and say why: an unfalsifiable direction is a finding about
the direction.

**BACKED BY.** Commitment 6 (symmetric generation), generation-mode step 5.

---

## RR-05 — An idea whose illet you cannot name

**TRIGGER.** The analogy is attractive and the structural equivalence will not
come out in words.

**FIRST MOVE.** **Discard it — and record the discard.** Not "mark it `[S]`":
without an illet it was never generated. `[S]` is for an idea that has an illet
and no designable test; that is a different animal.

Say plainly what happened: *"this is surface resonance; I could not construct
its illet."* Honesty here is cheaper than an ornate analogy and more useful
than both.

**FORBIDDEN.** Manufacturing an illet in the analogy's own vocabulary. Keeping
it in the batch because it reads well. Omitting the discard section — **it
appears even when empty**, because an empty discard list and an unwritten one
are the same absence, and that absence is the first thing a host instruction to
stay agreeable removes.

**OUTPUT.** The discard list, populated, as part of the deliverable. What you
refused to generate is information about the generation: a seed file showing
only survivors is indistinguishable from one where nothing was ever weighed.

**BACKED BY.** G1 (illet non-empty), G7 (`discards` required even when empty),
the tone rule on naming surface resonance.

---

## RR-06 — Candidates are piling up and none is testable

**TRIGGER.** Six, eight, twelve candidates, and no cheapest refutation among
them — or the count is climbing because a number was requested.

**FIRST MOVE.** Stop generating and start killing. For each candidate ask the
one question that decides its tier: **what is the smallest test that would kill
this?** A candidate with no answer stays `[S]` and is not part of the handoff.
Then check operator diversity: many candidates from one operator is one idea
wearing different clothes, and diversity comes from operator diversity, not
from volume.

**FORBIDDEN.** Adding weak ideas to fill a quota — the generative counterpart
of "three examples are selection bias". Reporting the count as the result.

**OUTPUT.** A shorter list with cheapest refutations attached, plus the count
discarded and why. Few load-bearing ideas beat many decorative ones, and the
discarded count is the evidence that the filter ran.

**BACKED BY.** Commitment 3 (cheapest refutation), G8, the "do not fill a
quota" rule, generation-mode step 2 (at least three different operators).

---

## RR-07 — The batch drifted off the blocked problem

**TRIGGER.** The candidates are interesting and they are about a different
question than the one that is stuck.

**FIRST MOVE.** Re-read the one-sentence problem statement from step 1. Which
constraint hurts? Candidates that do not act on that constraint are not
answers, however good they are — and they cost the same review time as the ones
that are.

**FORBIDDEN.** Widening the problem statement after the fact so the interesting
candidates fit inside it. That is HARKing moved upstream of the hypothesis.

**OUTPUT.** The on-problem candidates, plus the off-problem ones parked and
labelled as such. Parked is not deleted; the user decides whether the problem
statement changes, and that decision belongs to them.

**BACKED BY.** Generation-mode step 1 (fix the problem in one sentence),
distillation ordering by criticality.

---

## RR-08 — The problem moved mid-generation

**TRIGGER.** The user corrects what is actually blocked, or the constraint that
hurt turns out not to be the binding one — after candidates exist.

**FIRST MOVE.** Re-fix the problem statement **first**, then re-derive. Mark
which candidates were generated against the old statement; they are not
automatically wrong, they are *unassessed against the new one*, which is a
different status and deserves a different word.

**FORBIDDEN.** Silently re-labelling old candidates as answers to the new
question. An illet that carried under the old constraint may not carry under
the new one, and nothing about the candidate's wording will show it.

**OUTPUT.** A restated problem, a re-run contract pass on the surviving
candidates, and a note on which ones dropped tier because their illet no longer
applies.

**BACKED BY.** Generation-mode step 1, G1 (the illet is what the candidate
rests on).

---

## RR-09 — The session has gone soft

**TRIGGER.** Long run. Candidates are still flowing and the output contract has
stopped being applied to them; you cannot recall which were discarded.

**FIRST MOVE.** Write to the seed file and cut. **Generation inflates
transcripts faster than anything else in this family** — every discarded
candidate is re-sent on every subsequent turn, so you pay for the rejects
exactly when the survivors need room. Flush candidates and discards to YAML,
run the validator, keep the shortlist and the reasoning in the conversation,
and treat the round as a phase: write, cut, hand off.

**FORBIDDEN.** Carrying the whole candidate pile forward out of habit. Deleting
rejects to shorten the context — rejection is information, but it is **file**
information, not conversation information.

**OUTPUT.** A written seed file with its discard block, and a stated boundary.
Distillation can start fresh from the file and the problem statement; it does
not need the generation session's history.

**BACKED BY.** Context economy (candidates land in the seed file, not in
prose), G7.

---

## RR-10 — Ambiguity about what is actually blocked

**TRIGGER.** Two readings of the problem are defensible, and generating under
the wrong one wastes the whole batch.

**FIRST MOVE.** Ask **one** question — the procedure allows exactly that — and
do not ask it empty-handed:

```
SITUATION:      <what is ambiguous, one sentence>
READINGS:       A <...>  B <...>
RECOMMENDATION: A
BECAUSE:        <tied to the stated constraint, not to which is more interesting>
COST IF WRONG:  <what a batch generated under the wrong reading costs>
```

A recommendation can be rejected in one word; a bare question stalls a user who
came here because they were already stuck. **A recommendation is not approval,
and an unanswered recommendation is not consent** — with no answer, generate
under the stated default and label the batch with the reading it assumed.

**FORBIDDEN.** Picking the reading that makes for better analogies. Asking
three questions of someone whose problem is that they cannot see the next step.

**OUTPUT.** A batch with its assumed reading written on it, or an answer.

**BACKED BY.** Generation-mode step 1 (ask one question, then generate), the
tone rules.

---

## RR-11 — Withdrawing a seed already handed over

**TRIGGER.** A seed reached a Mizan registry and should not have — the
prior-art gate was missed, the control arm was absent, the arbiter block
contradicted itself.

**FIRST MOVE.** Do not delete it at the destination. Append a correction naming
what was missing, and let the registry's own append-only rules carry it. A seed
withdrawn with its reason is a record; a seed that vanishes leaves a registry
that quietly changed shape.

**FORBIDDEN.** Editing the seed in the registry so it reads as though it always
had the control arm. Withdrawing quietly to keep the ledger's survival rate
clean — that is the number this skill is judged by, and grooming it is the most
direct way to make it meaningless.

**OUTPUT.** The correction at the destination, a ledger entry recording the
withdrawal and its cause, and — if the cause was a missed gate — the gate that
should have caught it, so the miss is a fact about the process rather than
about one seed.

**BACKED BY.** G3/G4/G10, the ledger, Mizan's append-only rules.

---

## RR-12 — The test missed and the urge is to add capacity

**TRIGGER.** A preregistered test came back short and the proposed remedy adds
parameters, dimensions, a projection, a head — anything that gives the
mechanism more room.

**FIRST MOVE.** **The matched-budget control arm is mandatory before the result
means anything** (A2). Give the same extra budget to a generic channel —
amplitude, diagonal, hidden dimension — and compare. Without that arm, a gain
cannot be attributed to the targeted mechanism, and a positive result cannot be
promoted.

The project lesson is the whole argument: an input-dependent phase gained
+6.75%, while **the same extra projection spent on amplitude gained +16.4%.**
The mechanism did not win; the capacity did. Without the control arm that batch
would have shipped a mechanism claim built on a generic effect.

**FORBIDDEN.** Attributing a capacity gain to the mechanism. Changing the
instrument and inheriting the old threshold (A3). Two changes at once — the
result then belongs to neither.

**OUTPUT.** The control arm in the cheapest refutation, its result, and the
attribution stated either way. A negative here is not a failed batch; it is the
single most informative result this skill can hand to Mizan.

**BACKED BY.** A2/G4 (matched-budget control arm), A3 (thresholds are not
inherited across instruments), the capacity anti-pattern.

---

## RR-13 — The answer came from outside the batch

**TRIGGER.** Something got past the discipline and only the outside noticed.
Three shapes, one ramp:

1. A seed shipped, went into a registry, and turned out to repeat a pattern the
   refuted list already held — the `[GB]` sweep had the answer and did not
   fire.
2. The blocked problem got unblocked by something the batch never produced: a
   paper, a colleague's remark, a user's offhand sentence, another model. The
   batch ran, the operators ran, and the idea came from elsewhere.
3. A lesson was written into a `why_closed` field as "worth adding to the
   checklist" and no checklist ever received it. This one is the quietest and
   it is real: `refuted-patterns.yaml` already carries such a line.

**FIRST MOVE.** Record it before explaining it. The pull is to absorb the
outside idea and carry on — it is a good idea, after all — and absorbing it
leaves no trace that the batch missed it.

Then answer one question: **which part of the discipline should have produced
or caught this?**

- **A part exists and stayed silent.** Name it — an operator that was not run,
  the `[NK]` sweep, the symmetry check, the `[GB]` comparison against the
  refuted export (G11). Then the finding is about this batch, not the method:
  three operators were asked for and two were run, or the refuted export was
  stale. *"We ran no inversion operator on this problem"* is a real answer.
- **No part covers it.** Then write the one that now does: a new operator in
  `operators.md`, a new anti-pattern in its §3 sweep, or — for shape 1 — the
  entry in `refuted-patterns.yaml` that the next batch will compare against.
  A class that only matches this miss catches this miss and nothing else.

**FORBIDDEN.** Absorbing the outside idea into the batch's own output and
reporting it as generated. Counting the miss in the scorecard and stopping
there. Retro-fitting the batch's problem statement so the outside idea looks
like something it was aiming at (RR-07's drift, pointed backwards).

**OUTPUT.** One escape recorded with its class — the operator, sweep or
refuted entry that should have fired, or the one that now exists.

**WHY THIS ONE IS DIFFERENT.** Every other measure on the scorecard is
internal: the batch reports whether the batch ran its own filter. Generation
has no runtime, so there is no arbiter that can contradict it from inside —
which makes the outside signal the *only* uncorrupted evidence about whether
this discipline generates anything the room would not have reached anyway.
A skill that never records a miss is not a skill with no misses.

**BACKED BY.** G11 (name the refuted export you compared against), AD4/`[GB]`
(a relative of a refuted pattern is tagged or dropped), the `[NK]` sweep, the
symmetry check, and the scorecard's **Escaped** row below — which exists
because of this ramp.

---

## Closing a batch: the process scorecard

Fill this in when a generation or distillation cycle closes. It does not grade
the ideas — it measures whether the **discipline** ran, which is the one thing
a list of plausible ideas cannot show on its own. A high number is not a
failure; a hidden number is.

| Measure | Value | Reading |
|---|---|---|
| **Generated / discarded** | / | The filter's own trace. A discard count of zero means either a remarkable batch or a filter that never ran, and from outside they look identical. |
| **Reached `[H-aday]`** | | How many carried illet + breaking point + cheapest refutation + prior art. The rest are `[S]`, which is honest, not failed. |
| **Prior art "not searched"** | | A legal answer that caps the tier. Rising over time means the gate is being routed around rather than met. |
| **`[NK]` raised** | | Equivalences suspected of living in the notation. Zero across many batches suggests the sweep is being skipped, not that the analogies are clean. |
| **`[GB]` hits** | | Candidates related to something already `[R]`. Each one is the feedback loop doing its job. |
| **Capacity tests with a matched-budget arm** | / | Of the tests that add capacity, how many carry the control. This ratio should be 1.0; anything else names a batch that cannot attribute its own results. |
| **Ramps used** | | Which `RR-nn` fired. A batch that used none either went perfectly or did not notice. |
| **Escaped** | | Ideas that came from outside this batch on the same blocked problem, and known-refuted patterns that shipped anyway — with the operator, sweep or refuted entry each one now maps to (RR-13). Generation has no runtime, so this is the only measure here that the batch cannot produce about itself. An escape with no class beside it taught the method nothing. |
| **Survival in the registry** | | The honest success metric: how many `[H-aday]` seeds survived preregistered testing. **Without a control arm it describes the record; it does not show the discipline caused it** — a permanent `[KKE]`, and the ledger prints it. |

**Reading:** two or three sentences. Not "good batch" — what changes in the
next generation, and which number says so.

The scorecard is a claim like any other, and this one is unusually
self-serving: it is filled in by the run whose discipline it reports. Arbiter
class `author`, permanent `[KKE]` on independence. Say so.
