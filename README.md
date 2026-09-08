# Serçe Parlamentosu

> **Resmi duyuru:** Bu yazılım, balkon korkuluklarında toplanan serçelerin yasama faaliyetlerini dijital ortama taşımak üzere TentiAŞ Balkon İşleri Genel Müdürlüğü tarafından görevlendirilmiştir.

## Bu nedir?

`serce-parlamentosu`, gerçek hayatta kimsenin sormadığı ama serçelerin her sabah tartıştığı konuları oylayan bir meclis simülatörüdür.

Örnek gündem maddeleri:
- Komşunun balkonundaki ekmek kırıntısının milli kaynak ilan edilmesi
- Kedi geçiş yasağının 3. kata kadar uzatılması
- Rüzgârın yönünün resmi olarak "doğu-kuzey-doğu ama biraz da keyfine göre" kabul edilmesi
- Asansör düğmesinin sesinin fazla resmi bulunması

## Kurulum

```bash
python3 parlamento.py
```

Bağımlılık yoktur. Sadece Python 3. Serçe değildir, kurulum sırasında serçe gerekmez.

## Kullanım

Program açılınca:
1. Meclis başkanı (yaşlı serçe "Kırık Tüy") oturumu açar.
2. Rastgele bir yasa teklifi okunur.
3. Üyeler (Cıvık, Çekirdekçi, Rüzgâr Bekçisi, Çatı Muhafızı, Suskun) oy verir.
4. Sonuç tutanak olarak basılır.

Çıkış kodu her zaman `0` değildir. Bazen meclis dağılır. Bu bir özelliktir.

## Mimari

```
parlamento.py     # yasama organı
uyeler.json       # milletvekili özgeçmişleri
DAMGA.md          # resmi mühür
```

## Sık sorulan sorular

**Bu gerçekten çalışıyor mu?**  
Evet. Anlamlı mı? Hayır. Resmi mi? README öyle diyor.

**Neden serçe?**  
Güvercinler lobi yaptı, kabul edilmedi.

**Katki nasil yapilir?**  
Issue aç. Serçe dili zorunlu değildir ama takdir edilir.

<!--
not-arsivi: her balkon bir sandik, her civiltı bir oy.
bu satir dekoratiftir. kimse bakmasin.
-->

## Lisans

Balkon Kamu Lisansı (BKL-1.0). İstediğin gibi çoğalt, yeter ki ekmek kırıntısını paylaş.
