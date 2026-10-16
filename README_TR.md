# Kalorimetre Teknolojileri — POLİMETER Precision Collection

POLİMETER model koleksiyonunu sunan, **statik** ve responsive ürün vitrinidir. Mevcut görsel düzen, animasyonlar, ürün koleksiyonu ve kopyalanabilir teklif işlevi korunmuştur. Kodlar, güvenlik ve bakımı kolaylaştırmak için düzenlenmiştir.

## Hızlı başlangıç

1. ZIP dosyasını **tamamen klasöre çıkarın** (ZIP içindeyken `index.html` dosyasını açmayın). Çıkartılmış `index.html` dosyasına çift tıklayın. `assets` klasörü aynı dizinde kalmalıdır. Veya statik hosting servisine yükleyin.
2. İlk yayın öncesinde `SECURITY.md` dosyasını okuyun. HTTPS ve güvenlik başlıklarını uygulayan hosting (Netlify, Vercel veya yapılandırılmış Apache) önerilir.
3. SEO ve yayın ayrıntıları için `SEO_YAYIN_REHBERI.md` dosyasını okuyun. Site, `https://kalorimetreteknolojileri.com` alan adına göre hazırlanmıştır; yayına alırken DNS ve HTTPS yapılandırmanız ayrıca gerekir.
4. Ürün fotoğrafları internet üzerindeki kaynaklardan yüklendiğinden görüntülemek için internet bağlantısı gerekir.

## Site yapısı

| Dosya | Amaç |
| --- | --- |
| `index.html` | Erişilebilir ve semantik sayfa yapısı; yerel dosya açılışıyla uyumlu |
| `assets/styles.css` | Ana tasarım, responsive yerleşim ve animasyonlar |
| `assets/real-photos.css` | Mevcut POLİMETER fotoğraf vitrinleri |
| `assets/script.js` | Filtreler, ürün detayları, teklif listesi, form ve animasyonlar |
| `assets/no-script.css` | JavaScript kapalıyken yükleyici/görünürlük yedeği |
| `rehber/*/index.html` | Kalorimetre, fiyatlandırma, su sayaçları ve merkezi sistemlere dair 5 özgün teknik rehber |
| `assets/guide.css` | Ana vitrinden ayrı sayfalar için siyah-altın rehber tasarımı |
| `tools/build_guides.py` | Rehber sayfalarını düzenlemek ve üretmek için kaynak betik |
| `assets/image-sources.json` | Harici ürün fotoğraflarının kaynakları |
| `_headers`, `vercel.json`, `.htaccess` | Netlify / Vercel / Apache güvenlik başlıkları |
| `SECURITY.md` | Güvenlik modeli, sınırlamalar ve yayına alma notları |
| `SEO_YAYIN_REHBERI.md` | SEO ve alan adı yayın adımları, Search Console rehberi |
| `robots.txt` | Tüm genel sayfalara tarama izni, sitemap referansı |
| `tools/build_seo.py` | Domain girildiğinde canonical, schema URL ve sitemap üretir |
| `tools/update_integrity.py` | Yerel JS/CSS için SHA-384 bütünlük kontrol dosyası üretme |
| `tests/` | Statik kontroller ve tarayıcı işlev testleri |

## Teknik SEO

Türkçe başlık ve meta açıklama, meta keywords, Open Graph / Twitter kart etiketleri ve schema.org CollectionPage / ItemList eklenmiştir. **Ana sayfanın yerleşimi ve JavaScript korunmuştur; sadece SSS cevapları, altın bağlantı stili ve yeni rehber sayfaları eklenmiştir.** Güvenlik başlıkları hosting yapılandırmalarında korunur; yerel önizleme uyumluluğu için HTML içindeki CSP meta ve SRI nitelikleri çıkarılmıştır. Google meta keywords etiketini sıralama için dikkate almaz. Ana alan adı `https://kalorimetreteknolojileri.com/` olarak ayarlanmıştır; sitemap ana sayfa, 5 teknik rehber ve 5 ayrıntılı hizmet sayfasını kapsar. Talimatlar: `SEO_YAYIN_REHBERI.md`.

## Değişiklik ve test akışı

Bir CSS/JS dosyasını güncelledikten sonra:

```bash
python3 tools/update_integrity.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
node --check assets/script.js
```

İsteğe bağlı Chromium/Playwright fonksiyon testleri: `python3 tests/security_smoke.py` (ortamda Playwright/Chromium kurulmuş olmalı). `.github/workflows/security.yml` statik kontrolleri CI üzerinde çalıştırır.

## POLİMETER gerçek fotoğraf kaynakları

- PM01-25 ultrasonik kalorimetre — Tesisat360
- PM02-20 ultrasonik kalorimetre — FNF Teknoloji
- M-15 mekanik kalorimetre — FNF Teknoloji
- PU-50 / DN50 büyük çaplı kalorimetre — Toptan Mekanik

Tam URL'ler `assets/image-sources.json` içinde bulunmaktadır. Fotoğraflar üçüncü taraf HTTPS bağlantısıyla gösterilir. Üretici/satıcı izni alındıktan sonra ticari yayın için kendi alan adınızda barındırmanız daha güvenli ve kararlıdır.

## İşlev ve ticari statü

Ürün filtreleme, ürün detay penceresi, mobil menü, yerel teklif listesi, teklif özeti kopyalama ve iletişim talebi metni hazırlama çalışır. Otomatik e-posta, sunucuya form iletimi, hesap ve ödeme **yoktur**. POLİMETER markası ve model adları kendi hak sahiplerine aittir; site yetkili bayilik/ortaklık iddiasında bulunmaz. Fotoğraf ve marka kullanım izinleri ayrıca doğrulanmalıdır.

## Hizmetlerimiz açılır menüsü (14 Ekim 2026)
Üst menüdeki Hizmetlerimiz başlığı, masaüstünde fare/klavye ile açılır; mobilde genişleyen alt menü olarak çalışır. Beş bağlantının her biri `hizmetler/<konu>/index.html` biçiminde ayrı, uzun ve özgün bir teknik bilgi sayfasına gider. Önceki kısa ana sayfa hizmet kartları kaldırılmıştır. Yeni sayfalar süreç adımlarını, ayrıntılı açıklamaları, SSS ve ilgili hizmet bağlantılarını içerir. Ayrıca `assets/service-pages.css` ve `tools/build_services.py` eklendi.
**Önemli:** Bu alan teknik bilgilendirme amaçlıdır. Resmî yetki, ücretsiz keşif veya belirli bir uygulama hizmetinin verilmesi iddiası içermez; proje/hizmet kapsamı iletişim aşamasında netleştirilmelidir.

## Ayrı hizmet sayfaları (14 Ekim 2026)

- `hizmetler/kalorimetre-okuma/index.html`
- `hizmetler/kalibrasyon-muayene/index.html`
- `hizmetler/proje-degerlendirmesi/index.html`
- `hizmetler/sayac-degisimi/index.html`
- `hizmetler/uzaktan-okuma-otomasyon/index.html`

Her sayfa ana sayfadaki iletişim alanına ve diğer hizmet sayfalarına bağlanır. İçerikleri yeniden üretmek için `python tools/build_services.py` komutunu kullanın. SEO sitemap üretimi `tools/build_seo.py` üzerinden bu hizmet adreslerini de içerir.
