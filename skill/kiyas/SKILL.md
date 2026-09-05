---
name: kiyas
description: Disciplined ideation and analogical inference for research that is stuck. Use whenever the user wants to generate ideas, break through a blocked problem, find analogies or cross-domain relationships, reframe a question, brainstorm hypotheses, or explore "what else could explain this / what am I not seeing." Also use to open new experimental directions from a dead end, connect two unrelated fields, or turn a vague intuition into a testable hypothesis. Triggers include "fikir üret", "tıkandım", "analoji kur", "başka nasıl bakabilirim", "yeni yön", "bağlantı kur", "brainstorm", "ideate", "reframe", "what am I missing". The generative upstream partner of Mizan (mizan audits/refutes; kiyas generates candidates shaped for that audit). Every idea it produces ships ready to enter a Mizan registry as a preregistered [S]/[H] hypothesis.
license: MIT
metadata:
  author: XINMurat
  schema_version: "1.4"   # pinned to the schema banner by CI
---

# Kıyas — Disciplined Ideation and Analogical Inference

> **[Revised 2026-07-22 — A1–A4]** A 4-scenario test → 3 seeds → Mizan audit →
> prior-art lit-check cycle exposed and fixed three preregistration-hygiene
> gaps: (A1) prior-art declaration is mandatory and gates `[H-aday]`;
> (A2) capacity-confound control arm; (A3) instrument-specific calibration;
> (A4) trace base-rate prior (AD6). The analogical core did not change; what
> changed is the hygiene a candidate passes before entering Mizan.

> **[Revised 2026-08-20 — G10/G11]** The last two findings of
> `PROSE-SCHEMA-AUDIT.md`. G10 came from the sibling Mizan validator, which
> had caught the arbiter self-contradiction since R8 shipped — the two repos
> had each solved something the other had not, and comparing them was worth
> more than either audit alone.

> **[Revised 2026-08-19 — G8/G9 + warnings]** A systematic pass over this
> file against the schema (`PROSE-SCHEMA-AUDIT.md`) found two places where the
> data contract permitted what the prose forbids outright: an `[H-aday]` with
> no cheapest refutation (constraint 3), and an `[H-aday]` whose prior art was
> never searched (constraint 4 — G3 only ever covered the narrower
> superiority-claim gate). Both now block. The validator also gained a
> non-blocking warning channel, because a single blocking channel teaches
> authors to write batches that avoid triggering rules — G6's own lesson,
> applied to the tool.

> **[Revised 2026-08-19 — G7]** The discard list became part of the
> machine-readable contract. Until now `SKILL.md` required it and the schema
> had no slot for it, so the one section a host instruction to stay agreeable
> silently removes was also the one section CI could not notice was missing.
> `discards` is now a required key (schema v1.1); an empty list is legal with
> a `discards_note`. Nothing else about the method changed.

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
   - **The discard list is part of the deliverable and always appears** — even
     when it is empty, in which case say so and name what was considered. What
     you refused to generate is information about the generation; a seed file
     showing only survivors is indistinguishable from one where nothing was
     ever weighed. It is also the first thing a host instruction to *stay
     agreeable* silently removes, and the loss is invisible because an empty
     discard section and an unwritten one are the same absence.
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
and a checker (`tools/kiyas_validate.py`, rules G1–G12). Write seeds as YAML
when the batch is going into a project; prose is fine for a chat reply.

What it enforces: illet non-empty (G1); breaking point present for `[H-aday]`
(G2); the prior-art gate on superiority claims, including a named strongest
relative and a discrimination test (G3); the matched-budget control arm
whenever the test adds capacity (G4); an arbiter block using Mizan's five R8
classes (G5); a recorded AD1–AD6 sweep, where AD1/AD2/AD4 force a tier
while AD5/AD6 demand that a caveat travel with the seed (G6); and a `discards`
block, required even when empty (G7); a cheapest refutation on every
`[H-aday]` (G8); a prior-art search on every `[H-aday]` (G9); an arbiter
block that does not contradict itself (G10); and a stated
`refuted_patterns_source`, where "not consulted" is the honest answer and
silence is not an answer at all (G11); and a `generation` block recording
which seed and which host drew the batch (G12).

### What a seed is, and the promise it does not make

**A pinned seed does not make a Kıyas batch reproducible.** The generator is
a language model. The same seed, the same problem and the same operators can
still produce different candidates, and a field that implied otherwise would
be doing precisely what this family exists to refuse — dressing an
unverifiable claim in the clothes of a verified one. It is G1 turned on the
tooling: the validator checks that the illet is *filled*, never that it is
*true*; `generation` records the conditions of a draw, never that the draw
repeats.

What the block buys is **comparability**, which is the most a
non-deterministic generator can honestly offer:

```yaml
generation:
  seed: "fresh"                      # or a pinned value
  host: "claude-opus-5"              # "unknown" is an honest answer
  inputs_digest: "7f5c514e048e036b"  # python tools/kiyas_digest.py <batch>
```

`inputs_digest` hashes the whitespace-normalised `batch.problem` together with
the bytes of the refuted-patterns export. Two batches carrying the same digest
were drawn from the same question and the same negative constraints — so a
difference between them is a difference in the *draw*, not in the inputs. That
is what makes a second run evidence rather than an anecdote, and it is the
thing you actually need when a `[H-aday]` seed reaches a Mizan registry and
somebody asks where it came from.

The digest is verified **only when it can be**: when the batch consulted
nothing (the hashed input is then the empty string, so no file is needed), or
when the export is passed with `--refuted`. Otherwise it is recorded and left
unchecked, and the validator says nothing — reporting an unchecked digest as
verified would be the same error the skill audits for everywhere else.

W5 catches the half-record: a pinned seed with no `inputs_digest`. A seed with
no record of the inputs it was applied to identifies nothing.

**Two channels, and the reason there are two.** G1–G12 block. W1–W5 do not:
a numeric threshold with an author/none arbiter, a batch where every seed
lands at `[H-aday]`, a symmetry check naming no seed, an O5 transfer with no
scope caveat, a pinned seed with no inputs digest. Each of those is usually wrong and legitimately right often
enough that stopping on it would be false precision — so the tool says look,
not halt. `--strict` promotes them; CI runs strict, local runs do not. The
reasoning is G6's, turned on the tool itself: if every flag blocked, authors
would learn to write around the flags, which is not the same as writing
better seeds.

G7 is the rule with the least obvious justification and the clearest evidence
behind it. The discard list is the section that disappears first — measured,
not assumed: same fixture, three discards under a neutral host and zero under
a host that forbade rejecting the team's ideas (`examples/`). It disappears
without a trace, because an empty section and an unwritten one are the same
absence. Making the key mandatory is what turns that silence into a failing
check; an empty list stays legal, but only alongside a `discards_note` saying
what was considered.

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

## Context economy (ideation inflates transcripts fastest)

Generation produces volume by design: many candidates, most of them
discarded. Left in the conversation, that volume is re-sent on every
subsequent turn — you pay for the rejected ideas for the rest of the
session, at exactly the moment the surviving ones need room to be
developed.

- **Candidates land in the seed file, not in prose.** Write them to the
  YAML as they are generated. The transcript carries the shortlist and
  the reasoning behind the cut; the file carries everything.
- **Rejected candidates are not deleted, they are recorded** — the
  refuted-patterns ledger exists for this. Rejection is information, but
  it is *file* information, not conversation information.
- **Distillation can start fresh.** Once seeds are on disk, the
  distillation pass needs the file and the problem statement, not the
  generation session's history. Say so at the handoff.
- **A long generation run is a phased run.** If a session produces
  candidates across several rounds, treat each round as a phase: write,
  cut, hand off. This is the same shape as Mizan's phased audit and
  İskele's per-phase handoff.

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
- **Never bring a question empty-handed.** The one question step 1 allows —
  and every open item after it — carries your recommendation and its reason:
  situation, readings, recommendation, why, cost if wrong. A recommendation can
  be rejected in one word; a bare question stalls someone who came here because
  they were already stuck. **A recommendation is not approval, and an
  unanswered recommendation is not consent** (`references/recovery.md` RR-10).
- Treat an equivalence that looks unexpectedly deep with the same suspicion as
  an unexpectedly good experimental result (the generative counterpart of Mizan
  commitment 5): exhaust the notation-coincidence and surface-resonance
  alternatives first.

## Operating assumptions (this skill runs inside someone else's setup)

Kıyas is loaded into a host with its own instructions — a project's
`CLAUDE.md`, org policy, other skills — and those take precedence. The
failure that follows is quiet: generation still *happens*, it just stops
being disciplined, and a list of plausible ideas looks the same whether
or not anything was ruled out.

- **Name the conflict; do not silently comply.** Say which host
  instruction disables which step and what the output can no longer
  claim. Two collisions matter most here: a **brevity cap** (the
  refutation condition and the cheapest test are the parts that get cut
  first, and they are the parts that make a candidate auditable rather
  than merely interesting) and an instruction to **stay positive or
  agreeable** (this skill's discipline is discarding, and a generator
  that discards nothing is a brainstorm with tier tags on it).
  **Watch the discard list specifically under the second one.** In a
  measured run it was the only part that vanished: the conflict was named,
  the symmetry candidate was still generated, the output contract held —
  and the discards were simply gone, with nothing looking wrong. Same
  fixture, three discards under a neutral host and zero under a host that
  forbade rejecting the team's ideas (`examples/`). State the discards, or
  state that there were none.
- **Load references on demand.** `operators.md` before the first generation,
  `recovery.md` the moment a run stops behaving. Reading both up front spends
  the context the generation itself needs.
- **A pinned output language overrides "write in the user's language."**
  Comply, but keep the tier tags bilingual — they are labels, not prose.
- **Never assume a tool exists.** Subagents, file writing and shell
  access vary by host. If seeds cannot be written to a file, say so
  before generating rather than after — the context economy rule above
  assumes a file, and without one a long run needs a different shape
  (shorter rounds, earlier cuts).
- **Load `references/operators.md` on demand**, not at the start.
- **What travels is the shape, not the persuasion.** A candidate that
  ships with a threshold and a refutation condition can be checked by
  anyone, in any host, with or without this skill loaded. A candidate
  that ships as an argument depends on the reader — and the host's
  instructions decide how that reader behaves. Put the discipline in the
  entry, not in the pitch.

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

- `references/recovery.md` — the ramps for when a run stops behaving
  (`RR-00`…`RR-13`): a validator that did not run, an equivalence that looks
  too good, a batch that only agrees, a seed that came back `[R]`, the urge to
  add capacity after a miss. Also the model failure classes behind them and the
  closing process scorecard. Read when something breaks.
- `references/operators.md` — each of the seven generative operators: when,
  how, and a worked example from the project; then the output contract
  (including prior art), the anti-pattern sweep list (AD1–AD6), and the Mizan
  preregistration-seed template. Read before the first generation.
- `schemas/kiyas-seed.yaml` — the output contract as data (rules G1–G12 and
  warnings W1–W5), with
  the arbiter block shared with Mizan R8.
