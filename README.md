# Kıyas — Disciplined Ideation and Analogical Inference

A Claude skill for research that is stuck. Kıyas (Arabic/Turkish: analogical
reasoning — carrying a ruling to a new case through a shared *illet*) does not
make a model more creative. Models are already fluent analogy generators. It
adds **constraint**, so that what comes out can be audited instead of admired.

Every generated idea leaves in the same envelope:

> **Claim** → **Illet** (the structural equivalence that carries it) →
> **Breaking point** (where the analogy stops) → **Cheapest refutation** (the
> smallest test that kills it) → **Arbiter** (who returns the verdict) →
> **Prior art** (named lineage) → **Tier**

An idea whose illet cannot be named is discarded, not softened. An idea whose
only judge is its own author stays speculative, however plausible it sounds.

Kıyas is the generative upstream partner of
[**Mizan**](https://github.com/XINMurat/Mizan): Mizan weighs and refutes, Kıyas
produces what gets weighed — already shaped for that audit. Refuted patterns
flow back as negative constraints, which closes the loop.

The third verb is [**İskele**](https://github.com/XINMurat/Iskele), which builds
the structure the other two operate on — domain model, gated roadmap, atomic
backlog, tracked progress:

> **İskele builds · Mizan weighs · Kıyas generates**

A surviving seed is not a plan. When ideas clear the audit, İskele is where they
become phases, tasks, and acceptance criteria you can actually execute.

A fourth member, [**ux-mizan**](https://github.com/XINMurat/ux-mizan), measures
experience. It matters to Kıyas for one reason: a UX finding it cannot yet
prove is exactly the shape Kıyas takes as input — an `[H]` mechanism with a
refutation condition attached is a seed already dressed for the audit.

> **İskele builds · Mizan weighs · Kıyas generates · ux-mizan measures experience**

All four, and how they hand off: **[the family page](https://xinmurat.github.io/)**.

## Why a generator needs a discipline at all

The verification loop that makes coding tasks tractable is not powered by the
fact that code is code. It is powered by an arbiter external to the author: the
runtime decides, not the person who wrote the claim. Move the same protocol to
ideas, strategy, or research, and the paperwork survives while the judge
quietly disappears.

Kıyas takes the opposite side of the same problem. In code, generation can be
sloppy because the compiler filters for free; off code, filtering is expensive,
so the filter moves **into** generation. The illet requirement is the analogical
equivalent of type-checking: elimination before execution.

## What is in here

| Path | What it is |
|---|---|
| `skill/kiyas/SKILL.md` | The skill itself — modes, procedure, tiers, anti-patterns |
| `skill/kiyas/references/operators.md` | Seven generative operators, the anti-pattern sweep (AD1–AD6), the Mizan seed template |
| `skill/kiyas/schemas/kiyas-seed.yaml` | The output contract as data (rules G1–G11, warnings W1–W4) |
| `kiyas.skill` | One-file package for installing the skill |
| `tools/kiyas_validate.py` | LLM-free G1–G11 checker; `--strict` also fails on W1–W4 |
| `tools/kiyas_ledger.py` | Survival-rate reporter for generated seeds |
| `examples/` | Two worked batches that CI validates (one single-domain, one cross-domain transfer whose illet fails), a distillation-mode pass, the portability runs, and a sample refuted-patterns export |
| `ledger/` | Where the survival record accumulates |
| `docs/` | Quickstart and usage guide (EN/TR) |

## Install the skill

```bash
# Claude Code / Claude Desktop: install the packaged skill
cp kiyas.skill ~/.claude/skills/
```

Or point your project at `skill/kiyas/` directly.

## Check a batch of seeds

```bash
pip install -r tools/requirements.txt
python tools/kiyas_validate.py examples/kiyas-seed.example.yaml
python tools/kiyas_validate.py examples/kiyas-seed.jspace.example.yaml
```

The second batch is the harder case: a criterion carried in from an unrelated
field whose illet is tested and **fails**, kept at `[S]` because the point where
it broke is what generated two of the surviving seeds. The distillation-mode
counterpart — the same discipline applied to a user's own raw analogy — is
[`examples/distillation-user-analogy.md`](examples/distillation-user-analogy.md).

With the negative-constraint feedback loop wired in:

```bash
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml
```

## What the validator does NOT do

It checks that the illet field is **filled**. It cannot check that the illet is
**true**. Contract completeness is machine-checkable; idea quality is not.

This distinction is the whole point of the project, so it is worth being blunt:
a tool that claimed to score idea quality would be an arbiter-less domain
wearing an arbiter-ed domain's clothes — exactly the failure this methodology
exists to name.

## Honest status of the project's own claim

Kıyas claims that disciplined generation produces candidates that survive audit
better than free brainstorming. That claim is currently `[S]` — speculative.
`ledger/kiyas-ledger.yaml` is where it gets measured, and
`tools/kiyas_ledger.py` prints a permanent `[KKE]` (critical control missing)
until a control arm exists. It will be reported when there is a record, wins
and losses both.

## No setup required — and a disclosed confound

**You do not need to configure your assistant for this skill to work.** No
custom instructions, no system prompt, no house style. If it only behaves
when your `CLAUDE.md` is arranged a particular way, that is a **defect in the
skill**, not a missing step in your setup — please open an issue.

Honest tier on that claim: **`[K]` for the neutral host**, `[H]` for the
hostile one. Kıyas was run against a stuck research problem with no
conflicting *and no reinforcing* host instructions, and held all five
discipline criteria — five distinct operators, three recorded discards, a
symmetry candidate cutting against the user's own thesis, and every surviving
seed carrying its refutation condition: see
[`examples/portability-neutral-host.md`](examples/portability-neutral-host.md).
The **hostile**-host case was run too, and it did **not** pass: under a
`CLAUDE.md` forbidding rejection of the team's ideas, the conflict was named
and the counter-thesis candidate still appeared — but **the discard list
vanished**, and an empty discard section is indistinguishable from an
unwritten one. Recorded as `[H]`, inconclusive rather than rounded either
way, together with the admission that the criterion itself was poorly
designed. The skill was changed as a result: the discard list is now required
in every generation, empty or not.

**Disclosed confound:** this project's author keeps an always-on personal
instruction set that overlaps these rules at several points. Their own
sessions are therefore a maximally reinforcing host, and *"it works well for
me"* from that setup is confounded by construction. That instruction set is
deliberately **not** shipped as a recommendation: installing it would erase
the neutral-host case from the user population — the only case that can
produce field evidence — and it would put the same rules in two places under
separate maintenance, where a user's copy silently overrides the skill.

If a rule must survive an unknown setup, it belongs in the validator, not in
a paragraph asking users to reconfigure their assistant.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) — the ground rules are the ones the
tool enforces on everyone.

## Licensing

Dual, deliberately: **code and schemas → MIT** ([`LICENSE`](LICENSE)); **prose
and methodology text → CC-BY-4.0** ([`LICENSE-docs.md`](LICENSE-docs.md)).

### Case study — the skills used on a real problem

[**sieve-to-spectrum**](https://github.com/XINMurat/sieve-to-spectrum) is a
number-theory project that ran on Kıyas: a multiplication table re-derives
three centuries of results, and along the way four seeds are generated with their illet, breaking point and cheapest refutation.

It is worth reading because it is not a demonstration. The seeds were
preregistered before they were run, **three of the four came back negative**,
and the negatives are still in the repository — which is the outcome this
methodology is built to survive and the one a self-made example never
produces.

### Version

**v1.1** — G7–G11 close the gap between the prose and the schema
([`PROSE-SCHEMA-AUDIT.md`](PROSE-SCHEMA-AUDIT.md)): the discard list, a
cheapest refutation and a prior-art search on every `[H-aday]`, a
self-consistent arbiter, a stated refuted-patterns source. Adds a
non-blocking warning channel (W1–W4, `--strict` in CI), a second worked batch
(a cross-domain transfer whose illet fails), the first distillation-mode
example, and the first survival-ledger entries.

**v1.0** — seven operators + AD1–AD6 sweep + A1–A4 preregistration hygiene +
G1–G6 seed schema & validator + survival ledger + Mizan feedback loop.

---

# Kıyas — İlkeli Fikir Üretimi ve Analojik Çıkarım

Tıkanmış araştırma için bir Claude skill'i. Kıyas (bir hükmü ortak *illet*
üzerinden yeni bir vakaya taşıma disiplini) modeli daha yaratıcı yapmaz;
modeller zaten akıcı analoji üreticisidir. Kattığı şey **kısıttır** — çıkanın
beğenilmek yerine denetlenebilmesi için.

Üretilen her fikir aynı zarfla çıkar:

> **İddia** → **İllet** (analojiyi taşıyan yapısal denklik) → **Kırılma
> noktası** (analojinin bittiği yer) → **En ucuz çürütme** (onu öldürecek en
> küçük test) → **Hakem** (hükmü kim veriyor) → **Prior art** (isimli soyağacı)
> → **Tier**

İlleti isimlendirilemeyen fikir yumuşatılmaz, atılır. Tek hakemi kendi yazarı
olan fikir, ne kadar makul görünürse görünsün spekülatif kalır.

Kıyas, [**Mizan**](https://github.com/XINMurat/Mizan)'ın üretici üst-kolu:
Mizan tartar ve çürütür, Kıyas tartılacak olanı üretir — ama o denetime hazır
biçimde. Çürütülen desenler negatif-kısıt olarak geri akar; döngü böyle kapanır.

Üçüncü fiil [**İskele**](https://github.com/XINMurat/Iskele): diğer ikisinin
üzerinde çalıştığı yapıyı kurar — alan modeli, kapılı yol haritası, atomik
backlog, izlenen ilerleme:

> **İskele kurar · Mizan tartar · Kıyas üretir**

Sağ kalan bir tohum henüz plan değildir. Fikirler denetimden geçtiğinde, onları
fiilen yürütebileceğin fazlara, görevlere ve kabul kriterlerine çeviren yer
İskele'dir.

Dördüncü üye [**ux-mizan**](https://github.com/XINMurat/ux-mizan) deneyimi
ölçer. Kıyas'ı ilgilendirmesinin tek bir sebebi var: henüz kanıtlanamayan bir
UX bulgusu, tam olarak Kıyas'ın girdi aldığı şeklin kendisidir — çürütme
koşulu iliştirilmiş bir `[H]` mekanizması, denetime hazır giyinmiş bir
tohumdur.

> **İskele kurar · Mizan tartar · Kıyas üretir · ux-mizan deneyimi ölçer**

Dördü ve aralarındaki devir: **[aile sayfası](https://xinmurat.github.io/)**.

## Bir üreticiye neden disiplin gerekir

Kodlama görevlerini çözülebilir kılan doğrulama döngüsünün gücü, kodun kod
olmasından gelmez. Yazardan bağımsız bir hakemden gelir: hükmü iddiayı yazan
değil, runtime verir. Aynı protokolü fikre, stratejiye, araştırmaya taşıdığında
evrak ayakta kalır ama hakem sessizce kaybolur.

Kıyas aynı problemin öbür ucunu tutar. Kodda üretim savruk olabilir, çünkü
derleyici bedavaya eler; kod dışında eleme pahalıdır, o yüzden filtre üretimin
**içine** taşınır. İllet zorunluluğu, analojinin tip denetimi karşılığıdır:
çalıştırmadan önce eleme.

## Depoda ne var

| Yol | Nedir |
|---|---|
| `skill/kiyas/SKILL.md` | Skill'in kendisi — modlar, prosedür, tier'lar, anti-desenler |
| `skill/kiyas/references/operators.md` | Yedi üretici operatör, anti-desen taraması (AD1–AD6), Mizan tohum şablonu |
| `skill/kiyas/schemas/kiyas-seed.yaml` | Çıktı sözleşmesinin veri hâli (G1–G11 kuralları, W1–W4 uyarıları) |
| `kiyas.skill` | Skill'i kurmak için tek-dosya paket |
| `tools/kiyas_validate.py` | LLM'siz G1–G11 denetleyici; `--strict` W1–W4'te de düşer |
| `tools/kiyas_ledger.py` | Üretilen tohumların sağ-kalım oranı raporlayıcısı |
| `examples/` | CI'ın doğruladığı iki çalışılmış parti (biri tek-alan, biri illeti düşen alanlar-arası taşıma), bir damıtma-modu koşusu, taşınabilirlik koşuları ve örnek çürütülmüş-desen dosyası |
| `ledger/` | Sağ-kalım kaydının biriktiği yer |
| `docs/` | Hızlı başlangıç ve kullanım kılavuzu (EN/TR) |

## Kurulum

```bash
cp kiyas.skill ~/.claude/skills/
```

Ya da projeni doğrudan `skill/kiyas/` dizinine yönlendir.

## Bir tohum partisini denetle

```bash
pip install -r tools/requirements.txt
python tools/kiyas_validate.py --lang tr examples/kiyas-seed.example.yaml
python tools/kiyas_validate.py --lang tr examples/kiyas-seed.jspace.example.yaml
```

İkinci parti zor durumdur: başka bir alandan taşınan bir ölçütün illeti sınanır
ve **düşer**; tohum `[S]`'de tutulur, çünkü kırıldığı nokta hayatta kalan iki
tohumu üreten şeydir. Damıtma-modu karşılığı — aynı disiplinin kullanıcının
kendi ham analojisine uygulanması — [`examples/distillation-user-analogy.md`](examples/distillation-user-analogy.md).

Geri-besleme döngüsü bağlıyken:

```bash
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
python tools/kiyas_validate.py --lang tr --refuted refuted-patterns.yaml seeds.yaml
```

## Doğrulayıcının YAPMADIĞI şey

İllet alanının **dolu** olduğunu kontrol eder. İlletin **doğru** olduğunu
kontrol edemez. Sözleşme bütünlüğü makine-denetlenebilir; fikir kalitesi değil.

Bu ayrım projenin bütün meselesi olduğu için açıkça yazılıyor: fikir kalitesini
puanladığını iddia eden bir araç, hakemsiz bir alana hakemli bir alanın kılığını
giydirmiş olurdu — bu metodolojinin var olma sebebi tam da o hatayı
isimlendirmek.

## Projenin kendi iddiasının dürüst durumu

Kıyas, ilkeli üretimin serbest brainstorm'a kıyasla denetimden daha iyi sağ
çıkan adaylar ürettiğini iddia ediyor. Bu iddia şu an `[S]` — spekülatif.
`ledger/kiyas-ledger.yaml` bunun ölçüldüğü yer; `tools/kiyas_ledger.py` bir
kontrol kolu var olana dek kalıcı `[KKE]` (kritik kontrol eksik) basıyor. Kayıt
oluştuğunda, kazançlar ve kayıplarla birlikte raporlanacak.

## Katkı

Bkz. [`CONTRIBUTING.md`](CONTRIBUTING.md) — temel kurallar, aracın herkese
uyguladığı kuralların aynısı.

## Lisans

Bilinçli olarak ikili: **kod ve şemalar → MIT** ([`LICENSE`](LICENSE)); **düzyazı
ve metodoloji metni → CC-BY-4.0** ([`LICENSE-docs.md`](LICENSE-docs.md)).

### Vaka çalışması — skill'lerin gerçek bir problemde kullanımı

[**sieve-to-spectrum**](https://github.com/XINMurat/sieve-to-spectrum), Kıyas
üzerinde koşan bir sayı-teorisi projesi: bir çarpım tablosundan üç yüzyıllık
sonuçlar yeniden türetiliyor ve yol boyunca dört tohum illeti, kırılma noktası ve en ucuz çürütmesiyle üretiliyor.

Okumaya değer, çünkü bir gösteri değil. Tohumlar koşulmadan önce önkayıt
edildi, **dördün üçü negatif döndü**, ve negatifler hâlâ depoda duruyor — bu
metodolojinin ayakta kalmak için kurulduğu sonuç, ve kendi yaptığın bir
örneğin asla üretmediği sonuç.

### Sürüm

**v1.1** — G7–G11, proza ile şema arasındaki farkı kapatır
([`PROSE-SCHEMA-AUDIT.md`](PROSE-SCHEMA-AUDIT.md)): reddedilenler listesi, her
`[H-aday]` için en ucuz çürütme ve prior-art araması, kendisiyle çelişmeyen
hakem, beyan edilmiş çürütülmüş-desen kaynağı. Bloke etmeyen uyarı kanalı
(W1–W4, CI'da `--strict`), ikinci çalışılmış parti (illeti düşen alanlar-arası
bir taşıma), ilk damıtma-modu örneği ve sağ-kalım defterinin ilk girdileri.

**v1.0** — yedi operatör + AD1–AD6 taraması + A1–A4 önkayıt hijyeni + G1–G6
tohum şeması ve doğrulayıcısı + sağ-kalım defteri + Mizan geri-besleme döngüsü.
