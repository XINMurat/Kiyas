# Proza ↔ şema denetimi: hangi zorunluluk yazılı ama uygulanmıyor?

*Tarih: 2026-08-19. Kapsam: `skill/kiyas/SKILL.md` (316 satır) ve
`skill/kiyas/references/operators.md` (241 satır) içindeki her zorunluluk,
`skill/kiyas/schemas/kiyas-seed.yaml` (o an v1.1) ve `tools/kiyas_validate.py`
(o an G1–G7) tarafından fiilen uygulananlarla karşılaştırıldı. Şema o günden
beri v1.2'ye çıktı — bkz. DURUM.*

*Kural eklemek yöntem değişikliğidir ve karar bakımındır — G7'de izlenen yolun
aynısı.*

---

## DURUM (2026-08-20) — hangileri kapatıldı

| # | Bulgu | Durum |
|---|---|---|
| 1 | `[H-aday]` çürütme testi olmadan geçiyor | **KAPATILDI** — G8, bloke eden |
| 2 | Prior-art kapısı yalnızca üstünlük iddiasında | **KAPATILDI** — G9, bloke eden |
| 3 | Uyarı kanalı yok | **KAPATILDI** — `warnings` + `--strict`, CI strict koşuyor |
| 6 | Hakemsiz sayısal eşik | **KAPATILDI** — W1 (uyarı) |
| 7 | Hepsi `[H-aday]` olan parti | **KAPATILDI** — W2 (uyarı) |
| 8 | `symmetry_check` var olmayan id | **KAPATILDI** — W3 (uyarı) |
| 9 | O5 ⇒ scope_caveat | **KAPATILDI** — W4 (uyarı) |
| 4 | `class` ↔ `independent_of_author` çelişkisi | **KAPATILDI** — G10 (Mizan'dan taşındı) |
| 5 | `refuted_patterns_source` hiç okunmuyor | **KAPATILDI** — G11 |
| 10 | `seeds[S]` ↔ `discards` sınırı | AÇIK — kural değil, karar bekliyor |

§1'deki içi boş parti artık **iki ihlalle düşüyor** (G8 + G9) ve dört uyarı
üretiyor. Her ikisi için CI'ya self-test eklendi; birisi bir gün geçmeye
başlarsa, sözleşme yine yazılı hâlinin altına düşmüş demektir.

**10 numara dışında hepsi kapandı**; o bir eksik kural değil, verilmemiş bir
karar (illeti düşen fikir `seeds[S]`'e mi `discards`'a mı yazılır).

**Tarama sırasında çıkan ek bulgu — kontrolleri koşan dosyanın kendisi bozuktu.**
G7 commit'inde CI workflow'una eklediğim bir `printf 'discards: []
'`,
üreteç tarafından escape'i yutulduğu için tırnak içine gerçek bir satır sonu
koydu ve **workflow YAML'ı geçersiz hâle geldi** — yani `main`'de bir süre
GitHub Actions dosyayı hiç ayrıştıramadı. Düzeltildi, ve CONTRIBUTING'in
pre-PR listesine 0. adım olarak workflow'un kendi ayrıştırma kontrolü eklendi.
Ders, denetimin kendi temasının aynısı: **kontrolleri koşan şeyi kimse
kontrol etmiyordu.**
Kapsam sınırları (§6) **değişmedi** — `docs/` taranmadı, Mizan taranmadı.

---

## 0. Neden bu tarama yapıldı

G7, prozada bir gün önce yazılmış bir kuralın (`a41fcfc`: *"the discard section
must be PRESENT, empty or not"*) şemaya inmemiş olduğunu kapattı. Kapatırken
ortaya çıkan asıl soru şuydu: **bu tek bir kaçak mıydı, yoksa proza ile şema
arasında sistematik bir fark mı var?**

Cevap: sistematik. Ve kaçanlar, kaçmayanlardan daha merkezî.

---

## 1. Kanıt: G1–G7'den temiz geçen içi boş parti

Aşağıdaki dosya doğrulayıcıdan **hatasız** geçiyor (`OK — 1 seed(s) checked, no
G1–G7 violations`):

```yaml
batch:
  problem: "p"
  discards_note: "nothing refused"
  symmetry_check: "KS-999 breaks the thesis."     # var olmayan bir id
  operators_used: [O1, O2, O3]                    # beyan edilmiş, sadece O1 kullanılmış
seeds:
  - id: KS-1
    tier: H-aday
    operator: O1
    claim: "a claim"
    illet: "a structural equivalence"
    breaking_point: "here"
    cheapest_refutation: {test: "", adds_capacity: false}   # HİÇ TEST YOK
    arbiter:
      class: author
      who: "me"
      independent_of_author: true                 # class: author ile çelişiyor
      latency: "never"
    prior_art: {searched: false}                  # hiç aranmamış
    claims_superiority: false
    threshold_proposal: "p < 0.05"                # hakemi yazarken sayısal eşik
    antipattern_sweep:
      AD1_notation_coincidence: clear
      AD2_surface_resonance: clear
      AD3_confirmation_bias: clear
      AD4_refuted_relative: clear
      AD5_scale_leak: clear
      AD6_trace_base_rate: clear
discards: []
```

Bu parti, SKILL.md'nin **beş** açık zorunluluğunu çiğniyor ve doğrulayıcı hiçbirini
görmüyor. Aşağısı bunların dökümü.

---

## 2. Bulgular — sınıflandırılmış

Üç sınıf ayırıyorum, çünkü ağırlıkları farklı:

- **ÇELİŞKİ** — proza bir şeyi *açıkça zorunlu* kılıyor, şema tersine izin veriyor.
  Bunlar tartışmasız açıktır.
- **MODELLENMEMİŞ** — proza ima ediyor ama açık kural yazmamış; kural yapmak bir
  karar gerektirir.
- **İÇ TUTARSIZLIK** — verinin kendi alanları birbiriyle çelişebiliyor, kimse
  bakmıyor.

### ÇELİŞKİ-1 — `[H-aday]` en ucuz çürütme olmadan geçebiliyor **(en ağır bulgu)**

**Proza, kısıt 3:** *"Every idea ships with its cheapest refutation... If no test
can be designed, the idea stays `[S]`."* Tier tablosu da aynı şeyi söylüyor:
`[S]` = *"no test was designed/is designable"*.

**Şema:** `cheapest_refutation.test` **hiç kontrol edilmiyor.** `_check_refutation`
yalnızca `adds_capacity: true` ise devreye giriyor; `false` ise erken dönüyor ve
`test` alanı boş olsa bile ses çıkmıyor.

**Neden en ağır:** çürütme koşulu, bu skill'in tamamının varlık sebebi. Kendi
SKILL.md'si "put the discipline in the entry, not the pitch" diyor ve *entry*'yi
denetlenebilir kılan tek alan bu. G2 kırılma noktasını zorunlu kılıyor ama testi
kılmıyor — yani analojinin sınırı yazılmak zorunda, onu öldürecek deney değil.

**Uygulanabilir mi:** evet, tek satır. `tier == "H-aday"` ⇒ `cheapest_refutation.test`
dolu ve yer-tutucu değil.

---

### ÇELİŞKİ-2 — prior-art kapısı yalnızca üstünlük iddiasında çalışıyor

**Proza, kısıt 4:** *"Every idea ships with named prior art... 'Not searched' is a
legal answer, but then the idea **cannot be `[H-aday]`**."* Koşulsuz. Tier tablosu
da öyle: `[S]` = *"...OR prior art was not searched"*.

**Şema:** `_check_prior_art` ilk satırında `if not s.get("claims_superiority"):
return` yapıyor. Yani `claims_superiority: false` yazan her tohum, prior art hiç
aranmamış olsa da `[H-aday]` olabiliyor.

**Not — bu G3'ün hatası değil, kapsam farkı.** G3 A1 yamasını (üstünlük iddiası
→ en güçlü rakip + ayrım testi) doğru uyguluyor. Eksik olan, kısıt 4'ün *daha
geniş* olan koşulsuz hâli. Şema başlığı G3'ü zaten yalnızca üstünlük iddiası
üzerinden tarif ediyor, yani sapma en baştan şemaya yazılmış.

**Uygulanabilir mi:** evet. `tier == "H-aday"` ⇒ `prior_art.searched: true`.

---

### ÇELİŞKİ-3 — AD5 dışında kalan ölçek transferi şerhsiz kalabiliyor

**Proza, O5:** *"Scale transfer binds a reduced-scale finding to a main-regime
preregistration; the scope caveat is **mandatory**."*

**Şema:** `scope_caveat` yalnızca `AD5_scale_leak` bayraklıysa isteniyor. Operatörü
`O5` olan ama AD5'i "clear" yazan bir tohum şerhsiz geçiyor — ki O5'in tanımı
gereği rejim değişimi zaten var.

**Uygulanabilir mi:** evet, dar bir kural: `operator == "O5"` ⇒ `scope_caveat` dolu.
**Kırılma noktası:** O5 kullanıp aynı rejimde kalan meşru bir tohum bunu gereksiz
yere düşürür; o yüzden bu ÇELİŞKİ-1/2'den daha zayıf bir aday.

---

### MODELLENMEMİŞ-1 — hakem `author`/`none` iken sayısal eşik takılabiliyor

**Proza (iki yerde):** *"Attaching a precise-looking threshold to a seed whose
arbiter is the author or nonexistent. The form of a verification loop without its
judge is not rigor."* — anti-desen listesinde açıkça yasak. Ve: *"with `none`,
proposing a numeric threshold at all is theatre."*

**Şema:** G5 yalnızca `class: none` + tier ≠ S kombinasyonunu düşürüyor. `class:
author` + `threshold_proposal: "p < 0.05"` serbest; `class: none` + tier `S` +
sayısal eşik de serbest.

**Uygulanabilir mi:** kısmen. "Sayısal eşik" tespiti için basit bir sayı/karşılaştırma
operatörü regex'i yeter (`>=`, `<`, `%`, ondalık). **Kırılma noktası:** yazarın
"none" deyip yine de niyetini bir sayıyla ifade etmesi meşru olabilir; bu, bloke
eden bir kural değil bir *uyarı* olmalı — bkz. YAPISAL-1.

---

### MODELLENMEMİŞ-2 — her tohumu `[H-aday]` olan parti

Reponun kendi örnek dosyası bunu prozada söylüyor: *"A batch where everything
lands at H-aday is a batch that skipped the sweep."* Kural yok.

**Uygulanabilir mi:** evet ama **bloke eden kural olmamalı.** Tek tohumlu meşru
bir parti veya gerçekten temiz bir tarama bunu tetikler. Uyarı doğru araçtır.

---

### MODELLENMEMİŞ-3 — `refuted_patterns_source` hiç aranmıyor

Şema bu alanı zorunlu diye tarif ediyor ve *"'not consulted' is allowed and honest"*
diyor — yani **var olması** bekleniyor, içeriği serbest. Doğrulayıcı alanı hiç
okumuyor; tamamen yok olabilir. Bu, G6'nın kendi mantığının aynısı: "sessizlik
temiz tarama değildir."

**Uygulanabilir mi:** evet, G6 ile birebir aynı biçimde.

---

### İÇ TUTARSIZLIK-1 — `independent_of_author` ile `class` çelişebiliyor

`class: author` + `independent_of_author: true` mekanik olarak çelişik ve hiç
kontrol edilmiyor. Aynı şekilde `class: none` + `independent_of_author: true`.
Bu, bir yargı sorusu değil, veri tutarlılığı sorusu — doğrulayıcının zaten en iyi
yaptığı şey.

**Uygulanabilir mi:** evet, tartışmasız.

---

### İÇ TUTARSIZLIK-2 — `symmetry_check` var olmayan bir tohumu gösterebiliyor

Şema *"Name its id"* diyor. Doğrulayıcı yalnızca alanın boş olmadığına bakıyor.
`"KS-999 breaks the thesis"` geçiyor, KS-999 diye bir tohum olmasa bile.

**Uygulanabilir mi:** evet — en az bir tohum id'sinin metinde geçmesini iste.
**Kırılma noktası:** simetriyi id yerine tarifle anlatan meşru bir metin düşer;
bu da uyarı adayı.

---

### AÇIK TASARIM SORUSU — `seeds[S]` ile `discards` arasındaki sınır

G7 iki yuvayı da zorunlu kıldı ve **hangisinin ne zaman kullanılacağını söyleyen
kural yok.** İlleti düşen bir fikir hangisine yazılır? SKILL.md "DISCARD the idea"
diyor; ama doğrulayıcı AD2-bayraklı + `[S]` tohumu `seeds` içinde meşru sayıyor
(`kiyas-seed.jspace.example.yaml`/KS-J006 tam olarak böyle).

Bu bir eksik kural değil, **karar verilmemiş bir tasarım sorusu** — ve şu hâliyle
yazarın keyfine kalmış bir kaçış deliği. Benim kendi partim onu kullandı.

*İlgili gözlem:* `discards` girdilerinin `operator` alanı yok. Reddedilen bir fikir
de bir operatörle üretildi; "en az üç operatör" kuralının dürüst sayımı
`seeds ∪ discards` üzerinden olurdu. Bu aynı zamanda aşağıdaki maddeyi de çözer.

---

### DEĞERLENDİRİLDİ, BULGU DEĞİL — beyan edilen operatörler

`all_ops = ops | declared`: parti `operators_used: [O1,O2,O3]` yazıp tek tohumda
O1 kullanarak geçebiliyor. İlk bakışta boşluk gibi duruyor, **ama savunulabilir**:
üretimde kullanılan operatörlerin bir kısmı reddedilen fikirleri üretmiş olabilir
ve beyan bunu kapsar. G7'den önce bu doğrulanamazdı; discards'a `operator` alanı
eklenirse doğrulanabilir hâle gelir. Bu yüzden bulgu olarak değil, yukarıdaki
tasarım sorusunun bir parçası olarak kaydediyorum.

---

## 3. YAPISAL-1 — doğrulayıcının uyarı kanalı yok

Yukarıdaki adayların en az dördü (MODELLENMEMİŞ-1, -2, İÇ TUTARSIZLIK-2,
ÇELİŞKİ-3) **bloke etmemeli, uyarmalı**. Doğrulayıcı ikili: ya ihlal listesi +
exit 1, ya "OK" + exit 0. Ara yok.

Bu, G6'nın kendi tasarım notunun tam tersine düşen bir sınırlama. Orada şöyle
yazıyor: *"if every flag blocked promotion, authors would learn to leave the sweep
silent, which is worse than a flagged seed that states its scope."* Aynı mantık
araca da uygulanmalı: bloke eden tek bir kanal, yazarları kuralı tetiklemeyecek
biçimde yazmaya iter.

**Öneri:** `warnings` listesi + `--strict` bayrağı (CI'da strict, yerelde değil).
Bu, bloke etmesi tartışmalı her adayı güvenle eklenebilir kılar — ve muhtemelen
diğer tüm önerilerden daha değerli, çünkü onları mümkün kılan şey.

---

## 4. Mekanikleştirilemeyecek olanlar (kapsam dürüstlüğü)

Bunlar boşluk değil; aracın erişemeyeceği yerler. Listeye giriyorlar ki "geri
kalanı uygulanıyor" izlenimi doğmasın:

- İlletin **doğru** olup olmadığı (aracın kendi beyanı zaten bu).
- AD6'nın iki-yönlü dağılım-dışı şerhinin gerçekten iki yönlü olması.
- `strongest_relative`'in gerçekten en güçlü rakip olması.
- Ayrım testinin gerçekten ayırt etmesi.
- Simetri tohumunun tezi gerçekten **kesmesi** (alanın dolu olması ≠ kesmesi).
- `preregistered_prediction`'ın sonuçtan **önce** yazılmış olması — dosya
  sistemi bunu bilemez; git tarihçesi bilebilir, doğrulayıcı bilemez.

Son madde ilginç bir yan kapı: önkaydın gerçekten ön olduğu, ancak commit
zamanıyla doğrulanabilir. Şu an hiçbir şey bunu yapmıyor.

---

## 5. Sıralama (ağırlık × uygulama kolaylığı)

| # | Bulgu | Sınıf | Aksiyon |
|---|---|---|---|
| 1 | `[H-aday]` çürütme testi olmadan geçiyor | ÇELİŞKİ | G8, bloke eden |
| 2 | Prior-art kapısı yalnızca üstünlük iddiasında | ÇELİŞKİ | G9, bloke eden |
| 3 | Uyarı kanalı yok | YAPISAL | Diğerlerini mümkün kılar, önce bu |
| 4 | `class` ↔ `independent_of_author` çelişkisi | İÇ TUTARSIZLIK | G10, bloke eden |
| 5 | `refuted_patterns_source` hiç okunmuyor | MODELLENMEMİŞ | G11, bloke eden (G6 mantığı) |
| 6 | Hakemsiz sayısal eşik | MODELLENMEMİŞ | Uyarı |
| 7 | Hepsi `[H-aday]` olan parti | MODELLENMEMİŞ | Uyarı |
| 8 | `symmetry_check` var olmayan id | İÇ TUTARSIZLIK | Uyarı |
| 9 | O5 ⇒ scope_caveat | ÇELİŞKİ (zayıf) | Uyarı |
| 10 | `seeds[S]` ↔ `discards` sınırı | TASARIM | Karar gerekiyor, kural değil |

1 ve 2'yi ayrı tutuyorum çünkü bunlar "daha sıkı olabilir" değil, **prozanın açıkça
yasakladığı şeye izin veriyor.** Diğerleri iyileştirme.

---

## 6. Bu denetimin kurmadığı şeyler

- **Tam kapsam iddiası yok.** İki paketlenmiş proza dosyasını taradım. `docs/`
  altındaki uzun-metinler taranmadı; oradaki bir zorunluluk da kaçmış olabilir.
- **Mizan tarafı taranmadı.** Aynı türden bir proza-şema farkı `Mizan22`'de de
  olabilir; R1–R8 ile SKILL.md arasında aynı taramayı yapmadım. Kıyas'ta oran
  bu kadar yüksekse, orada da bakmamak için sebep yok.
- **Bulguların hiçbiri bir partinin gerçekten böyle yazıldığını göstermiyor.**
  Kanıt bölümündeki dosya benim ürettiğim sentetik bir fixture — kuralın
  *kapatmadığını* gösterir, birinin bunu *istismar ettiğini* değil. Reponun
  mevcut iki partisi de bu boşlukların hiçbirine düşmüyor.
- **Kural önerileri test edilmedi.** G8–G11'in denetim kalitesini artırdığı
  `[S]`; tek gerekçeleri prozayla tutarlılık.
