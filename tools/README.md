# Kıyas tools

LLM-free static checks. They are a `runtime` arbiter for **contract
completeness**, never for idea quality — see `skill/kiyas/SKILL.md`
§"The runtime arbiter".

| Tool | What it does |
|---|---|
| `kiyas_validate.py` | Enforces G1–G6 on a seed batch. `--lang tr\|en`, `--refuted <file>` for the AD4 negative-constraint check. Exit 0 clean / 1 violations / 2 usage. |
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
| `kiyas_validate.py` | Bir tohum partisinde G1–G6'yı uygular. `--lang tr\|en`, AD4 negatif-kısıt kontrolü için `--refuted <dosya>`. Çıkış 0 temiz / 1 ihlal / 2 kullanım. |
| `kiyas_ledger.py` | `ledger/kiyas-ledger.yaml`'dan üretilen tohumların sağ-kalım oranını raporlar. Kontrol kolu yokken kalıcı `[KKE]` basar. |
| `hooks/pre-commit` | Hazırlanmış `*kiyas-seed*.yaml` dosyalarında doğrulayıcıyı koşar. `git config core.hooksPath tools/hooks` ile kur. |

Bağımlılık: `pip install -r requirements.txt` (yalnız PyYAML).

Döngünün Mizan tarafı Mizan deposunda: `tools/mizan_export_refuted.py` bir
registry'nin çürütülmüş girdilerini bu doğrulayıcının okuduğu
`refuted-patterns.yaml`'a çevirir.
