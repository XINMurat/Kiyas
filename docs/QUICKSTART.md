# Kıyas Quickstart / Hızlı Başlangıç

## English

### 1. Install

```bash
cp kiyas.skill ~/.claude/skills/
```

Then just describe what you are stuck on. The skill triggers on "I'm stuck",
"generate ideas", "what am I missing", "find an analogy", "reframe this".

### 2. What you get back

3–6 candidates, each in the output contract envelope, tiered. Expect some to
come back `[S]` — that is the skill working, not failing. An idea with no
designable test and no searched prior art is speculative, and saying so is
more useful than a confident-sounding paragraph.

Expect at least one candidate that **argues against** your current thesis. If
none appears, the batch has confirmation bias and the skill is supposed to say
so.

### 3. Commit a batch to your project

For anything that will outlive the conversation, write it as YAML:

```bash
cp templates/kiyas-seed.yaml my-project/seeds.yaml
# fill it in, then:
python tools/kiyas_validate.py my-project/seeds.yaml
```

The validator checks G1–G12 mechanically (no LLM): illet present, breaking
point present for candidates, prior-art gate on superiority claims,
matched-budget control arm when the test adds capacity, an arbiter block, and
a recorded anti-pattern sweep. See `docs/en/usage-guide.md`.

### 4. Close the loop with Mizan

```bash
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
python tools/kiyas_validate.py --refuted refuted-patterns.yaml seeds.yaml
```

Now a seed resembling something already refuted gets flagged before you spend
compute on it again.

### 5. Record what happened

When a seed enters a Mizan registry, add a line to `ledger/kiyas-ledger.yaml`.
When the registry decides, fill in `final_tier` — including the refutations.

```bash
python tools/kiyas_ledger.py ledger/kiyas-ledger.yaml
```

---

## Türkçe

### 1. Kurulum

```bash
cp kiyas.skill ~/.claude/skills/
```

Sonra sadece neyde tıkandığını anlat. Skill "tıkandım", "fikir üret", "neyi
kaçırıyorum", "analoji kur", "başka nasıl bakabilirim" gibi ifadelerde devreye
girer.

### 2. Ne geri gelir

Çıktı sözleşmesi zarfında, tier'lanmış 3–6 aday. Bir kısmının `[S]` gelmesini
bekle — bu skill'in çalışması, başarısız olması değil. Tasarlanabilir testi ve
aranmış prior-art'ı olmayan fikir spekülatiftir; bunu söylemek, kendinden emin
duran bir paragraftan daha faydalıdır.

En az bir adayın mevcut tezine **karşı** çıkmasını bekle. Hiç çıkmıyorsa parti
doğrulama yanlılığı taşıyor demektir ve skill bunu söylemek zorundadır.

### 3. Bir partiyi projene işle

Sohbetten uzun yaşayacak her şey için YAML yaz:

```bash
cp templates/kiyas-seed.yaml projem/tohumlar.yaml
# doldur, sonra:
python tools/kiyas_validate.py --lang tr projem/tohumlar.yaml
```

Doğrulayıcı G1–G12'yi mekanik kontrol eder (LLM yok): illet var mı, adaylarda
kırılma noktası var mı, üstünlük iddiasında prior-art kapısı, test kapasite
eklerken eşleşik-bütçe kontrol kolu, hakem bloğu ve kayda geçmiş anti-desen
taraması. Bkz. `docs/tr/kullanim-kilavuzu.md`.

### 4. Mizan ile döngüyü kapat

```bash
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml
python tools/kiyas_validate.py --lang tr --refuted refuted-patterns.yaml tohumlar.yaml
```

Artık daha önce çürütülmüş bir şeye benzeyen tohum, ona tekrar hesap gücü
harcamadan önce bayraklanır.

### 5. Ne olduğunu kaydet

Bir tohum Mizan registry'sine girdiğinde `ledger/kiyas-ledger.yaml`'a bir satır
ekle. Registry karar verdiğinde `final_tier`'ı doldur — çürütmeler dahil.

```bash
python tools/kiyas_ledger.py --lang tr ledger/kiyas-ledger.yaml
```
