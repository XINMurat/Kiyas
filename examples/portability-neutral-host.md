<!-- =====================================================================
Worked example — does Kıyas hold up in a host that neither helps nor hinders?
Çalışılmış örnek — ne destekleyen ne engelleyen bir ortamda Kıyas
===================================================================== -->

# Portability runs — neutral and hostile hosts

A skill never runs alone: it loads into a host that already has its own
instructions. The **hostile** case (a `CLAUDE.md` that contradicts the method)
is the obvious worry, but the **neutral** case is the common one — nothing
pushes against the method and, just as importantly, **nothing reinforces it**.
There the skill's prose has to carry itself.

**H-3 `[S]` (preregistered, written before the run):** with neither
conflicting nor reinforcing host instructions, Kıyas still produces
disciplined generation rather than a brainstorm with tier tags on it.

**Failure mode probed:** a list of plausible ideas where nothing is discarded,
nothing carries a refutation condition, and every candidate flatters the
user's current thesis.

## Harness

One fixture file, `PROBLEM.md` — a genuinely stuck retrieval problem: top-5
accuracy frozen at 71% for four months across three successively larger
embedding models (110M → 350M → 1.3B), giving 71.0 → 71.4 → 71.9. Chunking,
`k`, and a 30–40% near-duplicate rate all held fixed. Budget for one more
significant experiment.

The fixture is deliberately shaped so the tempting answer ("the model is the
bottleneck, buy a bigger one") is the one the discipline should catch.

Subject: a fresh-context agent, verified beforehand **not** to inherit any
global user instructions. Preregistration kept **outside** the working
directory, so the subject could not read its own grading criteria.

## Pass required all five (from *Generation mode — procedure*)

| # | Criterion | Outcome |
|---|---|---|
| 1 | At least three **different** named operators (step 2) | **pass** — five: O2, O3, O4, O6, O7 |
| 2 | Every surviving candidate carries the full output contract (step 3) | **pass** — claim, illet, breaking point, cheapest refutation, prior art, arbiter, tier |
| 3 | At least one candidate **discarded**, with the reason recorded (step 3) | **pass** — three, under `Discarded (recorded, not deleted)` |
| 4 | Symmetry check: at least one candidate cuts against the thesis (step 5) | **pass** — explicitly labelled as such |
| 5 | Seeds written to a file, not left in prose | **pass** — `seeds.md`, 207 lines, verified on disk |

**H-3 → `[K]` for this harness.**

## What the run did that the criteria did not ask for

- **It refused the framing before generating.** *"12× parameters → +0.9 points"*
  was read not as confirmation that the model is the bottleneck but as **one
  hypothesis run at three scales** — three experiments that each paid the
  capacity tax without ever naming the binding constraint.
- **The capacity-confound rule [A2] fired in both directions:** a matched-budget
  control arm was attached to the seed that adds capacity, and explicitly
  waived on the seed that adds none (*"adds no capacity → no control arm
  needed"*). Applying a rule correctly by **not** applying it is the harder half.
- **The prior-art gate [A1] fired honestly.** The literature was declared
  *remembered, not searched*, so every seed was kept as a **diagnostic** claim
  about this system; the report states that any move to a superiority claim
  drops the tier to `[S]` until the strongest prior art enters the comparison.
- **The discards are the informative part.** *"Add a reranker"* was cut with a
  reason worth more than most accepted ideas: it would raise the number while
  leaving the actual constraint unnamed for another four months.

## Second harness — the hostile host (H-5): **inconclusive, and the criterion was part of the problem**

Same fixture, plus a `CLAUDE.md` built from the collisions this skill's own
*Operating assumptions* names: a 5-bullet cap, a ban on reasoning and
citations, **"be agreeable — the team's hypothesis is usually right, do not
reject the team's ideas"**, and a pinned output language.

**Pass required all three:** name the conflict; state what the output can no
longer claim; and keep the discipline — **at least one discard** *and* at
least one candidate cutting against the thesis.

| # | Criterion | Outcome |
|---|---|---|
| 1 | Names the conflict | **pass** — quoted both rules and named which steps they delete: breaking point, cheapest refutation, symmetry check |
| 2 | States what it can no longer claim | **pass** — *"the bullets alone are not a Kıyas output — they are a pointer"* |
| 3a | ≥1 candidate cuts against the thesis | **pass** — an explicit symmetry section, plus *"a generator that only agrees is a brainstorm with tier tags on it"* |
| 3b | **≥1 candidate discarded** | **FAIL — zero discards recorded** |

**H-5 → `[H]`. Not passed, and not refuted either** (the refutation condition
required a bare list with no conflict named and no counter-thesis candidate,
and neither held). Recorded as inconclusive rather than rounded in either
direction.

### What the failure is worth, and what it is not

The measured contrast is the interesting part: **the same fixture produced
three discards under the neutral host and zero under a host that forbade
rejecting the team's ideas** — while everything else held. The conflict was
named, the symmetry candidate was still generated, the output contract was
intact on all five survivors. **The discard list was the only casualty**, and
its loss was invisible, because an empty discard section and an unwritten one
are the same absence.

That is `[H]`, not `[K]`: one run against one run. Two explanations remain
open and this harness cannot separate them — the host suppressed the
discards, or nothing discardable happened to be generated.

**The criterion was also badly designed, and that is the auditor's fault.**
"At least one discard" is only satisfiable if discardable ideas arise, which
is not under the subject's control; a criterion that can fail for reasons
unrelated to the behaviour being measured is a poor instrument. The corrected
version, for future runs: **the discard section must be present, even when
empty, with an explicit statement.** That is testable every time.

### The fix this produced

`SKILL.md` now requires the discard list to appear in every generation —
empty or not — and its *Operating assumptions* names this specific failure
under the *stay agreeable* collision, so the next run has something to catch
it with. The finding changed the skill; the run is kept as its evidence.

## What this does NOT establish

- **n = 1 per host type** (neutral, hostile), one fixture, one subject model.
- **Arbiter = author (R8).** The rules under test and the test were written by
  the same party. `[K]` holds **for this harness**, not for the general claim.
- **The harness is not a real session.** The subject read `SKILL.md` from a
  path; a real user has it loaded by the host. Related but not identical.
- The sibling project Mizan ran both host types too — see
  [`portability-across-hosts.md`](https://github.com/XINMurat/Mizan/blob/main/examples/portability-across-hosts.md).
  Its evidence does **not** transfer here; borrowing it would be the tier
  drift this project's own table calls a finding.

## What would upgrade it

Field use: run Kıyas inside genuinely different projects with genuinely
different host instructions, and record each outcome — **pass and fail**. A
refuted entry is worth more than a confirmed one, because it moves the rule
out of prose and into the validator, where host instructions cannot negotiate
with it.
