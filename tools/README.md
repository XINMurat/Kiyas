# Kıyas tools

LLM-free static checks. They are a `runtime` arbiter for **contract
completeness**, never for idea quality — see `skill/kiyas/SKILL.md`
§"The runtime arbiter".

| Tool | What it does |
|---|---|
| `kiyas_validate.py` | Enforces G1–G13 on a seed batch. `--lang tr\|en`, `--refuted <file>` for the AD4 negative-constraint check. Exit 0 clean / 1 violations / 2 usage. |
| `kiyas_ledger.py` | Reports the survival rate of generated seeds from `ledger/kiyas-ledger.yaml`. Prints a permanent `[KKE]` while no control arm exists. |
| `hooks/pre-commit` | Runs the validator on staged `*kiyas-seed*.yaml`. Install with `git config core.hooksPath tools/hooks`. |

Install dependencies with `pip install -r requirements.txt` (PyYAML only).

The Mizan side of the loop lives in the Mizan repo:
`tools/mizan_export_refuted.py` turns a registry's refuted entries into the
`refuted-patterns.yaml` this validator consumes.

---

# Kıyas araçları

LLM'siz statik denetimler. **Sözleşme bütünlüğü** için `runtime` hakemidirler,
fikir kalitesi için değil — bkz. `skill/kiyas/SKILL.md`.

| Araç | Ne yapar |
|---|---|
| `kiyas_validate.py` | Bir tohum partisinde G1–G13'yı uygular. `--lang tr\|en`, AD4 negatif-kısıt kontrolü için `--refuted <dosya>`. Çıkış 0 temiz / 1 ihlal / 2 kullanım. |
| `kiyas_ledger.py` | `ledger/kiyas-ledger.yaml`'dan üretilen tohumların sağ-kalım oranını raporlar. Kontrol kolu yokken kalıcı `[KKE]` basar. |
| `hooks/pre-commit` | Hazırlanmış `*kiyas-seed*.yaml` dosyalarında doğrulayıcıyı koşar. `git config core.hooksPath tools/hooks` ile kur. |

Bağımlılık: `pip install -r requirements.txt` (yalnız PyYAML).

Döngünün Mizan tarafı Mizan deposunda: `tools/mizan_export_refuted.py` bir
registry'nin çürütülmüş girdilerini bu doğrulayıcının okuduğu
`refuted-patterns.yaml`'a çevirir.

## `token_budget.py` — the context budget, checked

A skill costs tokens the way a dependency costs bytes: to everyone who installs
it, on every cold start, forever. This one was designed to be cheap and that
intention lived only in prose — so between two releases the SKILL.md body grew
and the per-run load grew with it, and nothing failed, because **a budget nobody
checks is a preference**.

```bash
python tools/token_budget.py              # measure and compare to the ceilings
python tools/token_budget.py --json       # machine-readable
python tools/token_budget.py --update     # rewrite the ceilings AS THEY ARE NOW
```

Three tiers, because they are not paid at the same rate:

| tier | what it is | when it is paid |
|---|---|---|
| **T0** | the frontmatter `description` | every session where the skill is installed, used or not |
| **T1** | the SKILL.md body | whenever the skill triggers, and again on every cold start |
| **T2** | references and schemas | only when the procedure sends the model to that file |

Scripts and assets are not counted: they are executed or handed over as files,
not read into context. Counting tokens nobody pays is the fastest way to get a
budget ignored.

`runs` in `tools/token-budget.json` names what ONE mode actually loads —
SKILL.md plus whatever the procedure mandates — and gives that set its own
ceiling. That is the operational number; the tier totals are the structural one.

**The ceilings are preregistered.** Raising one is a deliberate commit with a
reason in the message, exactly as this skill demands of every other threshold.
`--update` exists for that commit and for no other purpose: running it to turn a
red build green, without reading the diff, is threshold shopping.

**The instrument, stated:** no tokenizer vocabulary is reachable offline, so
tokens are estimated from characters at the ratio in the config. The absolute
numbers are `[H]`; the drift the gate catches is `[K]`, because both sides are
measured with one instrument.

---

## `token_budget.py` — bağlam bütçesi, kontrol edilerek

Bir skill, bir bağımlılığın bayt harcadığı gibi token harcar: kuran herkese,
her soğuk başlangıçta, sürekli. Bu skill ucuz olacak şekilde tasarlandı ve o
niyet yalnızca düzyazıda yaşadı — iki release arasında SKILL.md gövdesi büyüdü,
koşu başına yük onunla büyüdü ve hiçbir şey kırılmadı, çünkü **kimsenin kontrol
etmediği bütçe, bütçe değil tercihtir.**

```bash
python tools/token_budget.py              # ölç, tavanlarla karşılaştır
python tools/token_budget.py --json       # makine okunur
python tools/token_budget.py --update     # tavanları ŞU ANKİ hâliyle yaz
```

Üç katman, çünkü aynı fiyattan ödenmiyorlar:

| katman | nedir | ne zaman ödenir |
|---|---|---|
| **T0** | frontmatter'daki `description` | skill kurulu olan her oturumda, kullanılsa da kullanılmasa da |
| **T1** | SKILL.md gövdesi | skill tetiklendiğinde ve her soğuk başlangıçta yeniden |
| **T2** | referanslar ve şemalar | yalnız prosedür modeli o dosyaya gönderdiğinde |

Script'ler ve varlıklar sayılmaz: onlar çalıştırılır ya da dosya olarak
devredilir, bağlama okunmaz. Kimsenin ödemediği token'ı saymak, bir bütçeyi
görmezden getirtmenin en hızlı yoludur.

`tools/token-budget.json` içindeki `runs`, TEK bir modun fiilen ne yüklediğini
adlandırır — SKILL.md artı prosedürün zorunlu kıldıkları — ve o kümeye kendi
tavanını verir. Operasyonel sayı budur; katman toplamları yapısal olandır.

**Tavanlar önkayıtlıdır.** Bir tavanı yükseltmek, mesajında gerekçesi olan
bilinçli bir commit'tir — bu skill'in diğer her eşikten istediğinin aynısı.
`--update` o commit için vardır, başka hiçbir şey için değil: kırmızı bir
build'i diff'i okumadan yeşile çevirmek için koşturmak, eşik alışverişidir.

**Alet, beyanıyla:** çevrimdışı erişilebilir bir tokenizer sözlüğü yok, bu yüzden
token sayısı config'teki orandan karakterle tahmin edilir. Mutlak sayılar `[H]`;
kapının yakaladığı kayma `[K]`, çünkü iki taraf da tek aletle ölçülür.
