# Kıyas Kullanım Kılavuzu

## 1. Ne zaman başvurulur

Kıyas, bir çalışma hattının ilerlemeyi kestiği an içindir: bariz deneyler
yapılmış, bariz çerçeveler tükenmiş, geriye "daha çok uğraş" ya da "başka yerde
uğraş" kalmıştır. Bir brainstorm oyuncağı değildir — fikir başına serbest
çağrışımdan pahalıdır ve o maliyet meselenin kendisidir.

Şunlarda başvur:
- bir deney hattı üst üste negatif gitmiş ve o izin bir sonraki üyesini
  koşmaya değip değmeyeceğini bilmek istiyorsun;
- iki paralel hat hiç aynı düzenekte kesilmemiş;
- bir mekanizma gördüğünü sanıyorsun ama ortada tesadüf olabilir;
- mevcut tezine KARŞI argümanın iyi kurulmuş hâlini istiyorsun.

Bir slaytı on fikirle doldurmak için başvurma. Sayı doldurmayı reddedecektir,
ve etmelidir.

## 2. İki mod

**Üretim.** Tıkandın. Skill problemi tek cümlede sabitler, en az üç farklı
operatör seçer ve çıktı sözleşmesiyle 3–6 aday döndürür. Çeşitlilik operatör
seçiminden gelir, daha çok analoji istemekten değil.

**Damıtma.** Elinde zaten bir yığın ham fikir var. Her biri aynı sözleşmeden
geçer, tier'lanır, bayraklanır ve kriticklik × (bilgi-değeri / maliyet)
sırasına dizilir.

## 3. Sert kurallar (özet — şemadaki G1–G9)

1. İllet boş olamaz. İlleti isimlendirilemeyen fikir üretilmiş sayılmaz.
2. Bir fikir hipotez adayı olmadan önce kırılma noktası yazılmış olmalı.
3. Prior-art araması yapılmamış üstünlük iddiası spekülatif kalır; en güçlü
   relatif karşılaştırma setinde ve bir ayrım testiyle birlikte olmalı.
4. Kapasite ekleyen test eşleşik-bütçe kontrol kolu taşır; taşımazsa pozitif
   sonucu hedeflenen mekanizmaya atfedilemez.
5. Her eşik önerisi hakemini isimlendirir — hükmü veren merci (`runtime` /
   `instrument` / `third_party` / `author` / `none`). Kendi kendini yargılayan
   tavanlıdır; hakemsiz olan spekülatif kalır.
6. AD1–AD6 taraması, açık "clear" dahil kayda geçer. AD1/AD2/AD4 tier'ı
   zorlar; AD5/AD6 tohumla birlikte seyahat eden bir şerh ister.
7. Parti **reddedilenlerini** kaydeder — neyin tartılıp reddedildiği ve nedeni.
   Boşken bile zorunludur; o durumda parti neyi değerlendirdiğini söyler.
   Yalnız hayatta kalanların listesi, bir şeyin tartıldığını gösteremez.
8. Hipotez adayı, kendisini öldürecek **en ucuz çürütmeyi** taşır. Tasarlanabilir
   bir test yoksa fikir spekülatif kalır.
9. Hipotez adayının **prior art'ı aranmıştır**. "Aranmadı" dürüsttür ama fikri
   spekülatif seviyede tavanlar.

Dört kontrol daha **bloke etmeden uyarır** (`--strict` ile düşerler): hakemi
olmayan sayısal eşik, her tohumu hipotez adayı olan parti, hiçbir tohumu
adlandırmayan simetri kontrolü, ve şerhsiz ölçek transferi. Her birinin meşru
istisnası var; o yüzden araç "dur" değil "bak" der — tek bir bloke eden kanal,
kuralların etrafından yazmayı öğretir.

## 4. Tier'ları okumak

| Etiket | Anlamı | Ne yapılır |
|---|---|---|
| `[S]` | Spekülatif | Sakla, üzerine iş kurma. Eksiği not et. |
| `[H-aday]` | Hipotez adayı | Mizan registry'sine önkayıt olarak yapıştır. |
| `[NK]` | Notasyon-kuşkulu | Her şeyden önce birim/baz/enstrüman değişimini koş. |
| `[GB]` | Geri-beslenen | Çürütülmüş bir şeyin akrabası. Akrabalığı bilerek kontrol et. |

`[H-aday]` dışında hiçbir şey registry'ye girmemeli.

## 5. Sık hatalar

- **Doğrulayıcıyı kalite hakemi sanmak.** Alanların dolu olduğunu kontrol eder.
  Dolu olmak doğru olmak değildir.
- **Eşik tiyatrosu.** Hakemi yazar olan bir tohuma, rigor'un formu elde
  olduğu için hassas görünen bir sayı iliştirmek. Onun yerine "burada
  enstrüman yok" yaz.
- **Sessiz tarama.** Bayrak çakmak başarısızlık itirafı gibi hissettirdiği için
  AD alanlarını boş bırakmak. Kapsamı yazılmış bayraklı tohum, sessiz olandan
  değerlidir.
- **Sayı doldurmak.** On fikir istemek. Geçenleri alırsın, ve teslim edilen şey
  sayı değildir.
- **Simetriyi atlamak.** Her adayın mevcut tezi okşaması, alan hakkında değil
  üretim hakkında bir bulgudur.

## 6. Mizan'a bağlamak

Kıyas tohumda durur. Mizan eşikleri kilitler, denetimi koşar, terfi ettirir
veya çürütür, çürütülen desenleri geri verir. Somut olarak:

```bash
# üretmeden önce: neyin zaten öldüğünü bil
python ../Mizan/tools/mizan_export_refuted.py registry.yaml -o refuted-patterns.yaml

# ürettikten sonra: partiyi bu kısıtlara karşı denetle
python tools/kiyas_validate.py --lang tr --refuted refuted-patterns.yaml tohumlar.yaml

# registry karar verdikten sonra: kaydet, kazançlar ve kayıplar
python tools/kiyas_ledger.py --lang tr ledger/kiyas-ledger.yaml
```

Defter, projenin kendi iddiasının test edildiği yerdir. Girdileri ve bir
kontrol kolu olana dek o iddia spekülatiftir ve araç bunu söyler.
