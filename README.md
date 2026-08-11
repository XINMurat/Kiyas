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
| `skill/kiyas/schemas/kiyas-seed.yaml` | The output contract as data (rules G1–G6) |
| `kiyas.skill` | One-file package for installing the skill |
| `tools/kiyas_validate.py` | LLM-free G1–G6 checker |
| `tools/kiyas_ledger.py` | Survival-rate reporter for generated seeds |
| `examples/` | A worked batch that CI validates, plus a sample refuted-patterns export |
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
```

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

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) — the ground rules are the ones the
tool enforces on everyone.

## Licensing

Dual, deliberately: **code and schemas → MIT** ([`LICENSE`](LICENSE)); **prose
and methodology text → CC-BY-4.0** ([`LICENSE-docs.md`](LICENSE-docs.md)).

### Version

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
| `skill/kiyas/schemas/kiyas-seed.yaml` | Çıktı sözleşmesinin veri hâli (G1–G6 kuralları) |
| `kiyas.skill` | Skill'i kurmak için tek-dosya paket |
| `tools/kiyas_validate.py` | LLM'siz G1–G6 denetleyici |
| `tools/kiyas_ledger.py` | Üretilen tohumların sağ-kalım oranı raporlayıcısı |
| `examples/` | CI'ın doğruladığı çalışılmış parti + örnek çürütülmüş-desen dosyası |
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
```

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

### Sürüm

**v1.0** — yedi operatör + AD1–AD6 taraması + A1–A4 önkayıt hijyeni + G1–G6
tohum şeması ve doğrulayıcısı + sağ-kalım defteri + Mizan geri-besleme döngüsü.
