# Contributing to Kıyas / Kıyas'a Katkı

## English

Kıyas is a methodology project, so it holds itself to its own discipline.
Contributions are welcome but must respect the rules the tool applies to
everyone.

### Ground rules (the same G1–G7 the tool enforces)

1. **Name the illet.** Any claim about why a change helps states the
   structural reason it bears load — not that it "feels cleaner". A PR whose
   rationale is surface resonance gets the same treatment a seed does:
   discarded, not softened.
2. **Ship the breaking point.** Where does your change stop working? A change
   with no stated limit has not been thought through, it has been advocated.
3. **Name the arbiter.** If you claim an improvement with a number, say who
   returns the verdict on it. If the answer is "the author", the claim is
   capped at `[KKE]`; if there is no judge at all, drop the number rather than
   let it imply an oracle that does not exist.
4. **Tier every claim.** In docs, PRs, and issues, tag non-obvious factual
   claims with `[S]/[H-aday]/[NK]/[GB]` (or Mizan's `[K]/[H]/[R]/[KKE]/[Y]`
   when discussing audited results). An untagged strong claim is a review
   comment waiting to happen.
5. **Negative results stay.** A refuted idea, a rejected operator, a failed
   experiment: recorded, never deleted. That is what makes a hit rate honest.
6. **Bilingual parity is required.** Every user-facing doc change must land in
   **both** `docs/en/` and `docs/tr/` (and both halves of `README.md`,
   `CONTRIBUTING.md`, `docs/QUICKSTART.md`). A PR that updates only one
   language is incomplete. Keep the tier tags identical across languages.

### Before opening a PR

```bash
# 1. seed batches must pass G1–G7 (English or Turkish messages):
python tools/kiyas_validate.py examples/kiyas-seed.example.yaml
python tools/kiyas_validate.py --lang tr examples/kiyas-seed.example.yaml
python tools/kiyas_validate.py examples/kiyas-seed.jspace.example.yaml
python tools/kiyas_validate.py --lang tr examples/kiyas-seed.jspace.example.yaml

# 2. the unfilled template must still FAIL (this is a real check, not a joke):
python tools/kiyas_validate.py skill/kiyas/schemas/kiyas-seed.yaml && echo "BROKEN"

# 3. the ledger reporter must run:
python tools/kiyas_ledger.py ledger/kiyas-ledger.yaml

# 4. the packaged skill must match its source:
python - <<'PY'
import zipfile, os, sys
n = lambda b: b.replace(b"\r\n", b"\n"); z = zipfile.ZipFile("kiyas.skill")
bad = [k for k in z.namelist()
       if not os.path.exists(os.path.join("skill", k))
       or n(z.read(k)) != n(open(os.path.join("skill", k), "rb").read())]
print("skill in sync" if not bad else "OUT OF SYNC: " + ", ".join(bad))
sys.exit(1 if bad else 0)
PY
```

Install the pre-commit hook so staged seed batches are checked automatically:

```bash
git config core.hooksPath tools/hooks
```

### Rebuilding the packaged skill

If you change **any** file under `skill/kiyas/`, rebuild the one-file package
so it stays in sync (the shipped `kiyas.skill` embeds those files):

```bash
python - <<'PY'
import zipfile, os
with zipfile.ZipFile("kiyas.skill", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("skill/kiyas"):
        for f in files:
            p = os.path.join(root, f)
            z.write(p, os.path.relpath(p, "skill").replace(os.sep, "/"))
PY
```

CI checks this. A stale package is not a cosmetic problem: users install the
package, not the source, so a drifted `kiyas.skill` means the documented
behaviour and the shipped behaviour disagree.

### What lives where

- `skill/kiyas/` — the skill (CC-BY-4.0 for prose, MIT for the schema).
- `tools/` — the G1–G7 validator, the ledger reporter, the git hook (MIT).
- `examples/`, `templates/`, `ledger/` — worked material and starting points.
- `docs/` — bilingual guides (CC-BY-4.0).

### Scope discipline

Kıyas generates; it does not adjudicate. Proposals that move tier promotion,
result recording, or evidence weighing into this repo belong in
[Mizan](https://github.com/XINMurat/Mizan) instead; proposals about project
scaffolding — roadmaps, backlogs, trackers, progress reporting — belong in
[İskele](https://github.com/XINMurat/Iskele). Keeping the generator, the judge,
and the builder in separate tools is not an accident of packaging — it is the
producer/auditor separation the methodology requires.

---

## Türkçe

Kıyas bir metodoloji projesidir; bu yüzden kendi disiplinine kendisi de uyar.
Katkılar memnuniyetle karşılanır ama aracın herkese uyguladığı kurallara saygı
göstermek zorundadır.

### Temel kurallar (aracın uyguladığı G1–G7'nin aynısı)

1. **İlleti isimlendir.** Bir değişikliğin neden işe yaradığına dair her iddia,
   yükü taşıyan yapısal sebebi yazar — "daha temiz duruyor" değil. Gerekçesi
   yüzey rezonansı olan PR, bir tohumla aynı muameleyi görür: yumuşatılmaz,
   atılır.
2. **Kırılma noktasını da getir.** Değişikliğin nerede çalışmayı bırakıyor?
   Sınırı yazılmamış değişiklik düşünülmemiş, savunulmuştur.
3. **Hakemi isimlendir.** Sayıyla bir iyileştirme iddia ediyorsan, o sayı
   üzerinde hükmü kimin verdiğini yaz. Cevap "yazar" ise iddia `[KKE]`
   tavanındadır; hiç hakem yoksa, var olmayan bir oracle'ı ima etmesin diye
   sayıyı tamamen kaldır.
4. **Her iddiayı katmanla.** Dokümanlarda, PR'larda, issue'larda apaçık olmayan
   olgusal iddiaları `[S]/[H-aday]/[NK]/[GB]` (denetlenmiş sonuç tartışılıyorsa
   Mizan'ın `[K]/[H]/[R]/[KKE]/[Y]`'si) ile etiketle. Etiketsiz güçlü iddia,
   gelmeyi bekleyen bir inceleme yorumudur.
5. **Negatif sonuçlar kalır.** Çürütülmüş fikir, reddedilmiş operatör, başarısız
   deney: kaydedilir, silinmez. Bir isabet oranını dürüst yapan şey budur.
6. **İki dillilik zorunlu.** Kullanıcıya dönük her doküman değişikliği **hem**
   `docs/en/` **hem** `docs/tr/` içine (ve `README.md`, `CONTRIBUTING.md`,
   `docs/QUICKSTART.md`'in her iki yarısına) girmeli. Tek dili güncelleyen PR
   eksiktir. Katman etiketlerini iki dilde birebir aynı tut.

### PR açmadan önce

Yukarıdaki İngilizce bölümdeki dört komutu çalıştır (`--lang tr` ile Türkçe
mesaj alırsın). Kancayı kur:

```bash
git config core.hooksPath tools/hooks
```

`skill/kiyas/` altında **herhangi bir** dosyayı değiştirdiysen tek-dosya paketi
yeniden üret (İngilizce bölümdeki script). CI bunu kontrol eder. Bayat paket
kozmetik bir sorun değildir: kullanıcı kaynağı değil paketi kurar, yani kaymış
bir `kiyas.skill` belgelenen davranışla dağıtılan davranışın çelişmesi demektir.

### Kapsam disiplini

Kıyas üretir, hüküm vermez. Tier terfisini, sonuç kaydını veya kanıt tartmayı bu
depoya taşıyan öneriler [Mizan](https://github.com/XINMurat/Mizan)'a; proje
iskelesiyle ilgili öneriler — yol haritası, backlog, çizelge, ilerleme raporu —
[İskele](https://github.com/XINMurat/Iskele)'ye aittir. Üreticiyi, hakemi ve
kurucuyu ayrı araçlarda tutmak paketleme kazası değil, metodolojinin
gerektirdiği üretici/denetçi ayrımıdır.
