# Kıyas — Üretici Operatörler, Anti-Desen Taraması, Mizan Tohumu

> **Türkçe operatör metni.** Bu dosya, `skill/kiyas/references/operators.md`'nin
> Türkçe aslıdır (revize 2026-07-22, A1/A3/A4). Paketlenen sürüm İngilizcedir.
> G1–G7 notları bu asılda yoktur; bkz. `docs/tr/kullanim-kilavuzu.md`.


> **[Revize 2026-07-22 — A1/A3/A4]** SKILL.md'nin A1–A4 yamalarının operasyonel
> karşılığı bu dosyaya taşındı: (A1) çıktı sözleşmesine ve tohum şablonuna
> **Prior art** + **ayrım testi** alanları; (A3) AD1'e enstrüman-özgü kalibrasyon
> nüansı (eşik enstrümanlar arası miras alınmaz); (A4) yeni **AD6 — iz-tabanı
> prior'ı**; tohum şablonuna **kapasite-kontrol kolu** (A2) ve **iz-tabanı
> öngörüsü** (A4) alanları. Yedi operatör ve analojik çekirdek değişmedi.

İçindekiler:
1. Yedi üretici operatör (ne zaman / nasıl / çalışılmış örnek)
2. Çıktı sözleşmesi (her fikir bu zarfla çıkar)
3. Anti-desen tarama listesi
4. Mizan önkayıt-tohumu şablonu

Çalışılmış örnekler, kullanıcının SpectralLM/GS-SSM projesinden çekilmiştir;
amaç operatörün somut hissini vermek, o sonuçları tekrar iddia etmek değil.

---

## 1. Yedi üretici operatör

Tek üretimde **en az üç farklı operatör** kullan. Çeşitlilik operatör
seçiminden gelir, "daha çok analoji" demekten değil.

### O1 — Kıyas (analoji-transferi) [çekirdek]
- **Ne zaman:** hedef problemin yapısı bilinen bir alanınkine benziyorsa.
- **Nasıl:** Asl (kaynak alan, yapısı bilinen) → Far' (hedef problem). Sonra
  **illeti** izole et: kaynaktaki hangi *yapısal* özellik hedefe taşınıyor?
  İlleti isimlendiremiyorsan bu O1 değil, yüzey rezonansı — at.
- **Örnek (proje):** Asl = Kuramoto faz-senkronizasyonu (fizik); Far' = dizi
  modellemede "dikkat". İllet = *bileşenler-arası seçici hizalanma bir
  bağlam-bağımlı ağırlık üretir*. Kırılma: senkronizasyon periyodik/otonom
  dinamiktir; dil aperiyodik ve girdi-sürülü → faz-değeri kısmı taşınmıyor
  (nitekim Mizan'da faz "largely redundant" çıktı). İllet yaşadı (seçici
  kontraksiyon), yüzey (faz-mistisizmi) çürüdü — operatörün doğru kullanımı.

### O2 — Ters-çevirme
- **Ne zaman:** bir yönün/nedenselliğin/işaretin "bariz" sayıldığı her yerde.
- **Nasıl:** varsayılan oku çevir. "A, B'yi üretir" → "B, A'yı seçer/kısıtlar".
- **Örnek (proje):** "durum geçmiş token'ı *taşır*" (retriever imgesi) → tersine
  "geçmiş, durumu *daraltır*" (lossy özetleyici). Ters okuma HG31'in çürütmesiyle
  tutarlı çıktı: durum uzak-token kimliğini taşımıyor, yakın-ufku okunabilir
  tutuyor. Ters-çevirme çoğu zaman gizli bir varsayımı görünür kılar.

### O3 — Kısıt-gevşetme
- **Ne zaman:** "şu yüzden yapamıyorum" cümlesi kurulan her yerde.
- **Nasıl:** o kısıtı geçici olarak kaldır; uzay nasıl açılıyor? Sonra kısıtın
  neden vardı olduğunu ve gevşetmenin bedelini yaz.
- **Örnek (proje):** HG34'te Gershgorin kararlılık kısıtı kuplajı |c|≤~0.03'e
  bağladı → zayıf-kuplaj dekoratif çıktı. Kısıt-gevşetme: "kararlılığı başka
  yoldan garanti et (unitary-karışım, ρ≤1 korunur) → tam-güç kuplajı aç".
  Bedel: parametrizasyon karmaşıklığı. Bu doğrudan HG34-rafine önkaydını doğurdu.

### O4 — Sınır / uç durum
- **Ne zaman:** bir mekanizmanın "neden çalıştığı" belirsizse.
- **Nasıl:** bir parametreyi 0'a veya ∞'a it. Ne kırılır, ne sadeleşir, ne
  dejenere olur? Uçta kalan şey çekirdek mekanizmadır.
- **Örnek (proje):** HG32 minimal-çekirdek tam olarak budur — SiLU/conv/rotasyon/
  mod tek tek 0'a it, yalnız |ā| bırak. Uçta hâlâ tavan kırılıyorsa indirgenemez
  mekanizma seçici sönümdür. Uç durum, "hangi bileşen yük taşıyor" sorusunu
  ablasyona çevirir.

### O5 — Ölçek-transferi
- **Ne zaman:** X ölçeğinde/rejiminde bir bulgu var; başka rejimde ne olur?
- **Nasıl:** mekanizmayı al, ölçeği/bağlam-uzunluğunu/boyutu değiştir, öngörü yaz.
- **Örnek (proje):** seq256'da "diz yok" (durum-faydası bağlamla büyümüyor) →
  seq1024'e transfer: "uzun bağlamda diz yükselir mi?" (HG13-d). Ölçek-transferi
  reduced-ölçek bulgusunu ana-rejim önkaydına bağlar; kapsam-şerhi zorunlu.

### O6 — Birleştirme (çarpıştırma)
- **Ne zaman:** iki ayrı hat paralel ilerliyor, birleşimi düşünülmemişse.
- **Nasıl:** iki çerçeveyi zorla aynı düzenekte kes. Etkileşim toplamsal mı,
  alt-toplamsal mı, süper-toplamsal mı?
- **Örnek (proje):** girdiye-bağlı faz (HG28) + girdiye-bağlı genlik (HG28-b)
  ayrı ölçülmüştü → birleştir: 2×2 faktöriyel (HG35). Sonuç alt-toplamsal (faz
  genlik-varken redundant). Birleştirme, "ikisi birden ne yapar" sorusunu
  etkileşim-terimine çevirir — en yüksek bilgi-değerli hamlelerden.

### O7 — Vekil-değiştirme (substrat swap)
- **Ne zaman:** bir işlev bir substratta çalışmıyor/tıkanıyorsa.
- **Nasıl:** işlevi sabit tut, substratı/enstrümanı değiştir.
- **Örnek (proje):** "çıkarımda öğrenme" faz-substratında ölmüştü (X1: fazlar
  donuk, PPL bozulmuyor). Vekil-değiştirme: aynı işlevi (çıkarım-anı adaptasyon)
  faz yerine *durum + okuma katmanı* substratına taşı → HG12 ilk pozitif kanıt
  (+%4.45). Substrat değişimi, ölü bir fikri diriltmenin en sık yoludur.

---

## 2. Çıktı sözleşmesi (her fikir bu zarfla çıkar)

```
FİKİR: <tek cümle, çürütülebilir iddia>
Operatör: <O1..O7>
İllet: <analojiyi/ilişkiyi TAŞIYAN yapısal denklik — yüzey benzerliği DEĞİL>
Kırılma noktası: <analojinin/ilişkinin nerede bozulduğu — ZORUNLU>
En ucuz çürütme: <onu öldürecek en küçük test; Mizan önkayıt tohumu.
  [A2] test kapasite/parametre ekliyorsa EŞLEŞİK-BÜTÇE kontrol kolu ZORUNLU>
Prior art: <en yakın literatür soyağacı, isim+yıl; ÜSTÜNLÜK iddiası varsa en
  güçlü relatif adıyla — o rakip karşılaştırma setinde değilse tier [S]'de kalır>
Tier: [S] / [H-aday] / [NK] / [GB]
```

İllet satırı boşsa fikir üretilmemiştir — atılır, "dekoratif" bile denmez.
Prior art satırı "aranmadı" ise bir üstünlük/özgünlük iddiası `[H-aday]` OLAMAZ [A1].

---

## 3. Anti-desen tarama listesi

Her üretilen fikri şuradan geçir; takılan bayrağı al.

### AD1 — Notasyon tesadüfü → `[NK]`
- **Ne:** sayısal/simgesel denklik yalnız keyfi bir birimde/bazda/temsilde tutuyor.
- **Test:** *birim/baz/temsil/**enstrüman** değiştir; denklik hayatta kalıyor mu?*
- **Örnek (proje):** golden-angle 137.5° ≈ 1/α 137.036 → radyanda %5600 fark.
  Birim-bağımlı tesadüf, yapı değil. Böyle bir denklik `[NK]` bayrağı almadan
  asla `[H-aday]` olmaz.
- **Enstrüman-özgü kalibrasyon [A3]:** bir eşik/marj/NULL, kullanılan enstrümanın
  KENDİ null dağılımından türetilir; enstrümanlar arası MİRAS ALINMAZ
  (MI-nat ≠ probe-R² ≠ AUC ≠ pseudospektral-abscissa). Farklı enstrümandan gelen
  eşiği taşıyan tohum `[NK]` bayrağı alır ve düzeltilmeden `[H-aday]` olamaz.

### AD2 — Yüzeysel rezonans → at veya `[S]`
- **Ne:** kulağa derin gelen ama illeti isimlendirilemeyen analoji.
- **Test:** *ne neye eşleniyor ve neden yük taşıyor, tek cümlede söyleyebiliyor
  muyum?* Hayırsa süstür.
- **Örnek (proje):** "Kuramoto = anlam senkronizasyonu" — şiirsel ama illetsiz;
  yük-taşıyan hâli "seçici hizalanma = bağlam-bağımlı ağırlık"tı (O1 örneği).

### AD3 — Doğrulama yanlılığı → simetri ekle
- **Ne:** üretilen adayların hepsi mevcut tezi okşuyor.
- **Test:** en az bir aday mevcut tezi *kırıyor* mu? Yoksa bir tane üret.

### AD4 — Geçmiş-çürütme akrabası → `[GB]`
- **Ne:** fikir, daha önce Mizan'da `[R]` olmuş bir desenin akrabası.
- **Test:** proje çürütülen-desenler listesini (ör. `refuted_and_open.md`) tara;
  akrabalık varsa `[GB]` uyarısıyla üret veya ele.

### AD5 — Ölçek/rejim sızıntısı → kapsam-şerhi
- **Ne:** bir rejimdeki (reduced-ölçek) fikri başka rejim iddiasına dönüştürmek.
- **Test:** öngörü hangi ölçekte doğrulanacak? Şerhi tohuma yaz.

### AD6 — İz-tabanı prior'ı → önkayıtlı-öngörüye taban-oran yaz [A4]
- **Ne:** çok-negatifli bir araştırma-izinin (ör. "geometri hattı 7/7 negatif")
  yeni bir üyesini, o izin taban-oranını önkayda yazmadan üretmek.
- **Test:** iz ≥N tutarlı negatifse **dürüst taban-oran** (≈ hit/N) önkayıtlı-
  öngörüye AÇIKÇA yazılır; yeni tohumun prior'ı bu tabana demirlenir.
- **Kapsam-dışılık nüansı (kritik):** taban yalnız izin ÖRNEKLEDİĞİ hücre için
  geçerlidir. Yeni tohum izin hiç girmediği bir rejimdeyse (ör. 7 negatif norm-
  koruyucu/zayıf-kuplaj iken tohum norm-KIRAN/non-normal), taban o tohum için
  **out-of-distribution**'dır — düşük taban güçlü bir null-prior'ı GARANTİ ETMEZ.
  Bunu önkayda "taban ≈0/N ama iz bu hücreyi örneklemedi" diye iki-yönlü yaz.

---

## 4. Mizan önkayıt-tohumu şablonu

`[H-aday]` fikirleri, Mizan Registry Entry'sine doğrudan yapıştırılabilecek
tohuma çevir (Kıyas burada durur; tier'ı Mizan/kullanıcı işler):

```markdown
### HX — <fikir adı> `[H]` `[önkayıt tohumu — Kıyas O# üretimi, YYYY-MM-DD]`
*(Köken: Kıyas, operatör O#, <problem cümlesi>. İllet: <...>)*
- Formel: <çürütülebilir iddia>
- Metrik: <ne, hangi enstrümanla — dosya/script/veri>
- Kapasite-kontrol kolu [A2]: <ek bütçeyi jenerik kanala (genlik/köşegen/gizli
  boyut) veren simetrik kol; terfi kuralı: Δ(hedef) − Δ(jenerik-kapasite) ≥ eşik.
  Test kapasite EKLEMİYORSA "gerekmez" yaz>
- Eşik (öneri, Mizan kilitleyecek): <sayısal karar kuralı; enstrümanın KENDİ
  null'ından — miras alınmaz [A3]>
- Çürütme: <hangi sonuç öldürür; iki-yönlü bilgilendiricilik>
- Prior art (isimli): <en yakın soyağacı isim+yıl>
- Ayrım testi [A1]: <en güçlü relatif; karşılaştırma setinde mi; iddia edilen
  ayrım o rakibe karşı nasıl test edilecek>
- İz-tabanı öngörüsü [A4]: <ilgili iz varsa taban-oran + kapsam-içi/dışı şerhi>
- Kırılma noktası (Kıyas'tan taşınan): <analojinin sınırı>
- Anti-desen bayrağı: [NK]/[GB]/AD6/yok
- Maliyet: <kaba emek>
- DURUM: ⏳ Kıyas tohumu — Mizan önkaydı bekliyor
```
