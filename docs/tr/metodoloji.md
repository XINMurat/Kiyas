# Kıyas — İlkeli Fikir Üretimi ve Analojik Çıkarım

> **Türkçe metodoloji metni.** Bu dosya, `skill/kiyas/SKILL.md`'nin Türkçe
> aslıdır (revize 2026-07-22, A1–A4). Paketlenen skill metni İngilizcedir —
> Mizan'ın kuralıyla aynı: skill gövdesi İngilizce, dokümanlar iki dilli, tier
> etiketleri her ikisinde de aynı. Skill kullanıcının dilinde yanıt verir.
> G1–G12 (tohum şeması ve doğrulayıcı) bu Türkçe asılda henüz yoktur; onlar için
> `docs/tr/kullanim-kilavuzu.md`'ye bak.


> **[Revize 2026-07-22 — A1–A4]** 4-senaryo testi → 3 tohum → Mizan denetimi →
> prior-art lit-check döngüsü üç önkayıt-hijyeni boşluğu ortaya çıkardı ve
> düzeltildi: (A1) prior-art beyanı zorunlu ve `[H-aday]` kapısı; (A2) kapasite-
> confound kontrol kolu; (A3) enstrüman-özgü kalibrasyon; (A4) iz-tabanı prior'ı
> (AD6). Analojik çekirdek değişmedi; değişen, üretilen adayın Mizan'a girmeden
> önce geçtiği hijyen.

Kıyas (Arapça/Türkçe: analojik akıl yürütme — bir hükmü ortak *illet* üzerinden
yeni bir vakaya taşıma disiplini) serbest çağrışımı değil, **denetlenebilir fikir
üretimini** hedefler. Mizan tartar ve çürütür; Kıyas tartılacak adayı üretir — ama
her adayı Mizan'a hazır biçimde: illetiyle, kırılma noktasıyla, en ucuz
çürütmesiyle ve **isimli prior-art'ıyla**.

## Neden disiplin gerekir (skill'in varlık sebebi)

Bir dil modeli zaten akıcı analoji üreticisidir; "yaratıcı ol" demek değer katmaz.
Kıyas'ın kattığı tek şey **kısıttır**:

1. **Her fikir illetini isimlendirir.** Yüzey benzerliği değil, analojiyi *taşıyan*
   yapısal denklik. İsimlendirilemiyorsa fikir dekoratiftir, üretilmiş sayılmaz.
2. **Her fikir kırılma noktasını taşır.** Analojinin nerede bozulduğu. Kırılması
   olmayan analoji süstür (bkz. anti-desen: yüzeysel rezonans).
3. **Her fikir en ucuz çürütmesiyle çıkar.** Onu öldürecek en küçük test — bu
   doğrudan bir Mizan önkayıt tohumudur. Test tasarlanamıyorsa fikir `[S]` kalır.
4. **Her fikir isimli prior-art'ıyla çıkar.** Fikrin en yakın literatür soyağacı
   isim+yıl ile beyan edilir. "Aranmadı" yazılabilir ama o hâlde fikir `[H-aday]`
   olamaz (bkz. §"Üretim modu — prosedür" adım 4). Bir üstünlük/özgünlük iddiası
   prior-art'ın *en güçlü* üyesine karşı test edilmemişse dekoratiftir.
5. **Her fikir `[S]` doğar.** Kıyas hiçbir şeyi kanıt/bulgu olarak sunmaz. Terfi
   Mizan'ın işidir.
6. **Simetrik üretim.** Mevcut hipotezi okşayan analoji kadar, onu *kıran*
   analoji de aranır (doğrulama yanlılığına karşı).

Bir fikir bu kısıtlardan geçemiyorsa, üretilmemiş demektir — sayı doldurmak için
zayıf fikir eklenmez (bkz. Mizan'ın "üç örnek seçilim yanlılığıdır" kuralının
üretici karşılığı).

## Üretici tier'lar (Mizan tablosuyla uyumlu, çift dilli)

| Etiket | TR | EN | Anlam |
|---|---|---|---|
| `[S]` | Spekülatif | Speculative | Üretildi; illeti var ama test tasarlanmadı/tasarlanamaz VEYA prior-art aranmadı |
| `[H-aday]` | Hipotez adayı | Hypothesis candidate | İllet + kırılma + en ucuz çürütme + **prior-art beyanı** tam → Mizan önkaydına hazır |
| `[NK]` | Notasyon-kuşkulu | Notation-suspect | Denklik birim/baz/temsile/enstrümana bağlı olabilir — anti-desen taraması şart |
| `[GB]` | Geri-beslenen | Fed-back | Daha önce Mizan'da `[R]` olmuş bir desenin/izin akrabası — negatif-kısıt uyarısı |

`[H-aday]` dışındaki hiçbir çıktı Mizan registry'sine önkayıt olarak GEÇMEZ.

## İki mod — hangisi uygulanır

**Üretim modu (ana).** Kullanıcı tıkanmış, yeni yön / analoji / çerçeve istiyor.
Hamle menüsünü (`references/operators.md`) uygula, çıktı sözleşmesiyle 3–6 aday
üret, tier'la, anti-desen taramasından geçir. Çıktı: `[H-aday]` fikirler +
Mizan'a doğrudan yapıştırılabilir önkayıt tohumları.

**Damıtma modu.** Kullanıcının elinde zaten bir yığın ham fikir/analoji var,
hangisi test edilmeye değer bilmiyor. Her birini çıktı sözleşmesine sok
(illet + kırılma + en ucuz çürütme + prior-art), tier'la, `[NK]`/`[GB]`/AD6
bayrakları çak, kriticklik × (bilgi-değeri / maliyet) sırasına diz.

İkisi bir arada ("hem üret hem hangisi değerli seç") ise: önce üret, sonra damıt.

## Üretim modu — prosedür

`references/operators.md`'yi ilk üretimden önce oku (hamle menüsü + çalışılmış
örnekler + anti-desen taraması). Sonra:

1. **Problemi tek cümlede sabitle.** Neyin tıkandığını, hangi kısıtın canını
   yaktığını isimlendir. Belirsizse tek soru sor, sonra üret.
2. **En az üç farklı operatör seç** (`operators.md`). Tek operatör tek tip fikir
   verir; çeşitlilik operatör-çeşitliliğinden gelir, "10 analoji" demekten değil.
3. **Her operatörü çıktı sözleşmesiyle koştur:** İddia → İllet → Kırılma noktası →
   En ucuz çürütme → **Prior art** → Tier. İllet isimlendirilemezse fikri AT,
   dekoratif deme.
   - **Kapasite-confound kuralı [A2]:** test modele parametre/kapasite ekliyorsa,
     en ucuz çürütme **eşleşik-bütçe kontrol kolu** içermek zorunda — aynı ek
     bütçeyi jenerik kanala (genlik / köşegen / gizli boyut) veren simetrik kol.
     Bu kol olmadan jenerik-kapasite kazancı hedeflenen mekanizmaya atfedilemez;
     pozitif sonuç `[H]`'ye terfi edemez. (Proje dersi: HG28 girdiye-bağlı faz
     +%6.75 → aynı ek projeksiyon genliğe +%16.4; kazanç jenerikti.)
4. **Anti-desen taraması** (`operators.md` §3): notasyon-tesadüfü (`[NK]`,
   **enstrüman-özgü kalibrasyonla** — eşik enstrümanlar arası miras alınmaz [A3]);
   illet testi; geçmiş `[R]` akrabalığı (`[GB]`); ve **iz-tabanı prior'ı**
   (AD6 [A4]: iz ≥N tutarlı negatifse dürüst taban-oran önkayıtlı-öngörüye yazılır).
   - **Prior-art kapısı [A1]:** bir üstünlük/özgünlük iddiası prior-art aranmadan
     `[H-aday]` olamaz — `[S]`'de kalır. İddia edilen ayrım, prior-art'ın *en güçlü*
     üyesine karşı test edilmeli; o üye karşılaştırma setinde değilse tohum eksiktir.
5. **Simetri kontrolü:** ürettiğin adayların hepsi mevcut tezi mi okşuyor? En az
   biri tezi *kıran* yönde olmalı; yoksa doğrulama yanlılığı — bir tane üret.
6. **Mizan'a devir:** `[H-aday]` fikirleri Mizan Registry Entry şablonuna
   yapıştırılabilir tohum olarak sun (formel iddia + metrik + kapasite-kontrol kolu
   + eşik-önerisi + çürütme + prior-art + ayrım testi + iz-tabanı öngörüsü). Kıyas
   burada durur; tier terfisi Mizan/kullanıcının işidir.

## Damıtma modu — prosedür

1. Ham fikirleri atomize et (bir cümlede iki fikir varsa ayır).
2. Her birine çıktı sözleşmesini uygula; illeti VEYA prior-art'ı olmayanı `[S]`'de
   bırak, "bunu test edilebilir/özgün kılmak için şu eksik" notuyla.
3. `[NK]`, `[GB]` ve iz-tabanı (AD6) bayraklarını çak; üstünlük iddiası varsa
   prior-art kapısını (A1) uygula.
4. Kriticklik × (bilgi-değeri / maliyet) sırasına diz; en ucuz-en keskin öne.
5. En üstteki 1–3 adayı Mizan önkayıt tohumuna dönüştür.

## Mizan ile döngü (iki skill'i sisteme bağlayan şey)

Kıyas üretir → Mizan denetler/önkayıtlar/çürütür → **çürütülen desenler
negatif-kısıt olarak Kıyas'a geri döner.** Pratik uygulama:

- Proje bir "çürütülen-desenler" listesi tutar (ör. `refuted_and_open.md` +
  "notasyon tesadüfleri" alt-başlığı). Kıyas her üretimden önce bu listeyi okur;
  akraba fikri `[GB]`/AD6 bayrağıyla üretir veya elemeye alır.
- Dürüst başarı ölçütü: Kıyas-üretimi `[H-aday]`'ların registry'de sağ-kalım
  oranı, serbest brainstorm'a kıyasla. Bu oran zamanla ölçülür — üç güzel örnek
  değil, skorlanmış üretim kaydı (Mizan'ın hit-rate kuralının üretici ikizi).

## Ton ve çerçeve kuralları

- Üretilen fikri asla bulgu gibi sunma. "Şu ilginç olabilir" ≠ "şu doğru".
- İllet isimlendirilemiyorsa dürüstçe söyle: "bu bir yüzey rezonansı, illetini
  kuramadım" — süslü analoji üretmekten iyidir.
- Prior-art aranmadıysa dürüstçe "aranmadı" yaz ve tier'ı `[S]`'de tut — sahte bir
  özgünlük iddiası üretmekten iyidir.
- Az ama yük-taşıyan fikir, çok ama dekoratif fikirden iyidir. Sayı doldurma.
- Metafor sezgi kaynağıdır, kanıt değildir (proje kültürüyle aynı ilke).
- Kullanıcının dilinde yaz; tier etiketlerini çift dilli tut.
- Beklenmedik derinlikte görünen bir denkliğe, beklenmedik iyi bir deney sonucu
  kadar şüpheyle bak (Mizan madde 5'in üretici karşılığı): önce notasyon-tesadüfü
  ve yüzeysel-rezonans alternatiflerini tüket.

## Anti-desenler (kibarca reddet)

- Sayı doldurmak için illeti olmayan fikir üretmek.
- Bir denkliği notasyon-tesadüfü taramasından geçirmeden `[H-aday]` yapmak.
- Bir eşiği/marjı enstrümanlar arası miras almak (MI-nat ≠ probe-R² ≠ AUC) [A3].
- Kapasite/parametre ekleyen testi eşleşik-bütçe kontrol kolu olmadan önermek —
  kazanç jenerik olabilir (HG28-b dersi) [A2].
- Bir üstünlük/özgünlük iddiasını prior-art aranmadan `[H-aday]` yapmak; asıl
  rakibi (en güçlü relatif) karşılaştırma setine koymamak [A1].
- Çok-negatifli bir araştırma-izinin taban-oranını önkayıtlı-öngörüye yazmadan
  iz-hipotezi üretmek [A4/AD6].
- Yalnız mevcut tezi doğrulayan analojiler üretip simetriyi atlamak.
- Üretilen `[S]` fikri "bulgu/yön kanıtlandı" diye sunmak (Mizan-kaçağı).
- Geçmişte `[R]` olmuş bir deseni `[GB]` bayrağı olmadan yeniden önermek.

## Referanslar

- `references/operators.md` — Yedi üretici operatörün her biri: ne zaman, nasıl,
  ve projeden çalışılmış örnek; ardından çıktı sözleşmesi (prior-art dahil),
  anti-desen tarama listesi (AD1–AD6) ve Mizan önkayıt-tohumu şablonu. İlk
  üretimden önce oku.
