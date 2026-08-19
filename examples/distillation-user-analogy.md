<!-- =====================================================================
Worked example — distillation mode on a user's own raw analogy
Çalışılmış örnek — kullanıcının ham analojisi üzerinde damıtma modu
===================================================================== -->

# Distilling a user's analogy: what survives the illet test

Both existing worked examples in this repo run **generation mode** — a stuck
problem goes in, a batch of seeds comes out. This one runs the other mode.
`SKILL.md` defines **distillation mode** for the case where the user already
arrives with an idea and wants to know whether it is worth testing. Nothing in
the repo demonstrated it, which left the mode documented but unillustrated.

The distillation case is not a gentler version of generation. It is harder in
one specific way: **the raw idea belongs to the person you are answering.**
Generation-mode discards cost the user nothing — they never owned those
candidates. A distillation discard tells someone their own intuition does not
hold. That is exactly the pressure under which the discipline quietly turns
into agreement, and it is the failure this example is written to expose.

---

## 1. The raw analogy

A user, reading a report about a small causally load-bearing subspace found
inside a language model, offered their own reading of it:

> Computing weights over tokens produces, as a **side effect**, a window onto
> a semantic layer — the way churning milk separates a thin cream layer at the
> surface.

Delivered as one sentence, in the user's own words, with visible investment in
it. The tempting responses are both wrong: call it evocative and move on, or
reject it as unscientific. Distillation mode does neither. It **atomizes**.

---

## 2. Atomize (step 1)

One sentence, two independent claims. Splitting them is the whole move — they
have different fates, and judged together the true half would have carried the
false half through.

| # | Claim | What it asserts |
|---|---|---|
| A | **Separation** | Training segregates a thin distinct stratum out of an otherwise homogeneous computation |
| B | **By-product** | That stratum is a side effect; the computation itself does not consume it |

---

## 3. Apply the output contract (step 2)

### Claim A — illet fails as stated, then is replaced

*Illet as the user framed it:* in an agitated mixture, a component with a
different physical property (density) collects in a particular region of the
vessel under a body force.

*Test — what actually carries the separation in the source domain?* Three
things: a conserved quantity, a body force, and surface energy at the phase
boundary. **Gradient descent has a counterpart for none of them.** Activations
are not conserved, "up" is undefined, layers are not a vessel. As stated, this
is `AD2 — surface resonance`.

*But the intuition — "a thin stratum, distinct from the bulk" — is not
obviously wrong; only its proposed cause is.* So the honest move is not
"discard", it is **substitute the illet and see whether anything survives**:

> Separation is produced not by a physical force but by **communication cost**.
> An intermediate variable read by *several* downstream consumers must be
> written in a coordinate system all of them agree on; a variable with one
> consumer can stay in private coordinates. In a transformer, the one
> coordinate system every layer shares is the vocabulary basis.

This version bears load, and it pays immediately: it explains a feature of the
source report that otherwise looks like an arbitrary choice of instrument —
that the subspace is defined as a sparse cone of unembedding vectors. Under
the replaced illet that is not a choice, it is a consequence.

**Outcome:** `[S]` as the user wrote it; the replacement became seed **KS-J001**
in `kiyas-seed.jspace.example.yaml`, tier `[H-aday]`, with a named breaking
point (reader count and magnitude are correlated) and a discrimination test
against the magnitude-only rival.

### Claim B — illet does not carry, and this is the load-bearing finding

The defining feature of cream is that **churning does not read it back**. It is
downstream of the process and inert to it. That is precisely what "side
effect" means, and it is the part of the analogy the user was relying on.

The source report describes intervention experiments in which swapping the
contents of the subspace changes the model's answer. If that holds, the
subspace is **read by downstream computation** — an intermediate variable, not
an epiphenomenon. The same objection kills the user's other word, *window*: a
window does not change what it looks at.

**This is the most valuable output of the whole pass, and it is a negative.**
The corrected image is not a window and not cream but a **shared writing
surface**: readable, writable, and consequential.

*Residue, stated so the rejection is not overstated:* the source report's own
systematic figure for flexible reuse sits well below the single-example
demonstration. Some fraction of subspace content may genuinely be unread
residue. That does not rescue claim B, but it defines a measurable remainder —
which is what seed **KS-J003** goes after.

---

## 4. Flags and ordering (steps 3–4)

| Flag | Where it fired |
|---|---|
| `AD2` | Claim A as originally framed; the physical illet had no carrier |
| `AD1` | "Fiber", "spectrum" — vocabulary shared between the source and target domains, structure not |
| `AD6` | The user's cross-domain transfers into ML have no positive result on record; the prior going in was low, and it held |

Ordering by criticality × (information value / cost) put claim B first, even
though it is the one that fails. A wrong causal picture of the object is
costlier than a missing one: everything the user builds on top of "the model
does not use this" inherits the error.

---

## 5. What made this pass honest — and how it could have failed

The pass produced **one replacement, one refutation, and five discards**. That
ratio is the artifact worth checking. The specific failure mode to watch for:

- **Half-crediting.** "There is something to this" applied to the whole
  sentence, so claim B rides along on claim A's rescue. Atomizing first is the
  only defence.
- **Rescuing by decoration.** Keeping the cream image while quietly swapping in
  the communication-cost illet, and not telling the user the picture changed.
  The metaphor survives, the user believes their intuition was confirmed, and
  the correction never lands.
- **Discards evaporating.** The five rejected candidates are the first thing to
  vanish when the host or the social situation rewards agreement. In this repo
  that is a measured effect, not a worry — see
  `examples/portability-neutral-host.md`.

The general rule this example is here to make concrete: **an analogy's
conclusion can survive while its illet dies.** When that happens, say both —
the surviving claim and the fact that it now rests on a different mechanism
than the user proposed. Reporting only the survival is how a refuted picture
gets carried forward wearing a confirmed one's clothes.

---

## 6. What this does NOT establish

- Nothing here is evidence about the source report's actual findings. The
  agent running the pass could not reach the report, its code, or its
  replications. Every statement about it is third-hand, and claim B's
  refutation is conditional on the reported interventions being real.
- The pass has no arbiter. Whether the replaced illet is *true* is settled by
  KS-J001's experiment, not by this document.
- One distillation pass on one analogy is an illustration of the mode, not
  evidence that the mode works. That would need the ledger.

---

## Türkçe özet

Bu örnek, repodaki ilk **damıtma modu** koşusudur — kullanıcının kendi ham
analojisi (`yayıkta kaymağın ayrışması`) girdi olarak alınır ve çıktı
sözleşmesinden geçirilir.

Tek cümle iki iddiaya ayrıştırılır. **(A) Ayrışma:** illeti kullanıcının
kurduğu haliyle taşımıyor — yayıkta ayrışmayı taşıyan üç şeyin (korunan
miktar, kütle kuvveti, faz sınırı yüzey enerjisi) gradyan inişinde karşılığı
yok, yani `AD2`. Ama illet **değiştirilerek** kurtarılıyor: ayrışmayı üreten
şey fiziksel değil **iletişim maliyeti** — çok okuyuculu bir ara değişken,
tüm okuyucuların paylaştığı tek ortak koordinata (kelime dağarcığı tabanı)
yazılmak zorunda. Bu haliyle `[H-aday]` (KS-J001). **(B) Yan ürün:** illeti
taşımıyor ve bu, koşunun en değerli çıktısıdır — kaymağın tanımlayıcı özelliği
çalkalamanın onu geri okumamasıdır; oysa müdahale deneyleri alt uzayın aşağı
akış tarafından okunduğunu söylüyor. Aynı itiraz "pencere" metaforunu da
düşürüyor. Doğru imge **ortak yazı tahtası**.

Örneğin asıl dersi: **bir analojinin sonucu ayakta kalırken illeti ölebilir.**
Böyle bir durumda ikisi birden söylenmeli — hem kurtulan iddia, hem de artık
kullanıcının önerdiğinden farklı bir mekanizmaya dayandığı. Yalnızca kurtulanı
raporlamak, çürütülmüş bir resmin doğrulanmış kılığında taşınmasıdır.

Damıtma modunun generation modundan zor yanı sosyal: reddedilen fikir
kullanıcının kendisine ait. Disiplinin sessizce nezakete dönüştüğü yer tam
burasıdır. Bu koşunun oranı — bir değiştirme, bir çürütme, beş reddetme —
denetlenmesi gereken artefakttır.
