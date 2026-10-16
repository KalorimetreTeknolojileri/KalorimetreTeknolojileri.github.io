# Kalorimetre Teknolojileri — Google SEO ve Domain Kurulum Rehberi

## Tasarım ve güvenlik

Alan adı ve marka kimliği güncellenirken ürün fotoğrafları, animasyonlar, teklif akışı ve genel görsel düzen korunmuştur. SEO ayarları HTML `<head>` bölümü ve ilgili teknik dosyalarda tutulur. Sunucu tarafındaki CSP ve güvenlik başlıkları korunur. `file://` önizlemesinde sorun çıkarmaması için HTML içindeki CSP meta ve SRI nitelikleri kaldırılmıştır; ana sayfanın ürün vitrini, animasyonları ve genel görsel düzeni korunmuştur. SSS bağlantılarına ince altın vurgusu eklenmiş ve ayrı teknik rehber sayfaları hazırlanmıştır.

## 1) Tanımlanan alan adı ve SEO bilgileri

Sitenin adresi **kalorimetreteknolojileri.com** olarak ayarlanmıştır. Canonical adresi, sitemap ve sosyal paylaşım URL’leri bu alan adına göre üretilmiştir. İleride değiştirmek isterseniz proje klasöründe şu komutu çalıştırın:

```bash
python3 tools/build_seo.py --domain https://kalorimetreteknolojileri.com
```

- `www` tercih edilmiyorsa mevcut kök alan adı ayarını kullanın.
- Komut **canonical URL**, **Open Graph/Twitter tam görsel URL'leri**, **schema.org WebSite/Organization/CollectionPage URL'leri**, **robots.txt** ve **sitemap.xml** üretir.
- **Komutu çalıştırdıktan sonra klasörü hostinge yükleyin.** Kodu değiştirdiğinizde komutu tekrar çalıştırabilirsiniz. Sitemap ana sayfa, 5 rehber URL’si ve 5 hizmet URL’sini kapsar. Rehber sayfalarının sabit alan adı `tools/build_guides.py` içindeki `DOMAIN` değerinden üretilir; alan adını değiştirirseniz bu dosyayı da güncelleyip rehberleri yeniden oluşturun.
- Bu script, sizin yazdığınız gerçek alan adı dışında domain veya ürün iddiası üretmez.
- Windows: Python kuruluysa komut `py tools/build_seo.py --domain https://kalorimetreteknolojileri.com` olabilir.

## 2) Google'da görünmek için

1. HTTPS üzerinde sitenin açıldığını, `robots.txt` ve `sitemap.xml` dosyalarına erişilebildiğini kontrol edin.
2. `https://search.google.com/search-console` adresinde **domain mülkü** oluşturup DNS TXT kaydıyla doğrulayın. DNS için kullandığınız panel değişebilir.
3. **Site Haritaları** menüsünde `https://kalorimetreteknolojileri.com/sitemap.xml` adresini gönderin.
4. **URL Denetimi** ile ana sayfayı kontrol edin; gerekiyorsa **Dizine eklenmesini iste** seçeneğini kullanın.
5. SSL sertifikanızı aktif tutun ve `http`, `www`/`www` olmayan, `/index.html` gibi yinelenen yolları mümkünse **301 yönlendirmeyle** tek URL'ye taşıyın. Yönlendirmeler hostinginize/alan adınıza özeldir, bu pakette rastgele kural eklenmedi.

## 3) Hedef anahtar kelimeler ve yeni rehberler

- Ana konu: **kalorimetre**, **POLİMETER kalorimetre**, **ısı sayacı**, **ısı ölçüm sistemleri**.
- Ürün alt konuları: **ultrasonik kalorimetre**, **mekanik kalorimetre**, **PM01**, **PM02**, **M-15**, **PU-50**.
- İlgili sektör: **doğalgaz sistemleri**, **enerji ölçüm sistemleri**, **doğalgaz sayacı** (sitede doğalgaz sayacı satışında/ürünlerinde yetki olduğu iddia edilmez).

Ana sayfa için ürünlerle ve sunduğumuz bilgilerle doğrudan ilgili **71 arama ifadesi** `meta keywords` içine eklendi. Bunlar sıcak/soğuk su sayaçları, DN ölçüleri, kalorimetre seçimi, ultrasonik/mekanik modeller ve merkezi ısıtma gibi konuları kapsıyor. Bulut Enerji sitesindeki sektörel konu başlıkları referans alındı; rakibin metinleri kopyalanmadı, hizmet veya bölge iddiası uydurulmadı.

Ayrıca SEO açısından anlamlı özgün metinler taşıyan 5 bağlantılı rehber eklendi:

- `/rehber/kalorimetre-nedir/` — kalorimetre nedir, nasıl çalışır ve okunur?
- `/rehber/ultrasonik-mekanik-kalorimetre/` — teknik karşılaştırma.
- `/rehber/kalorimetre-fiyatlari/` — fiyatı etkileyen özellikler (doğrulanmamış tutar verilmez).
- `/rehber/isi-pay-olcer-merkezi-isitma/` — ısı pay ölçer, merkezi sistemler ve gider paylaşımı farkları.
- `/rehber/su-sayaci-secimi/` — sıcak ve soğuk su sayaçlarının seçimi.

İstediğiniz `meta keywords` etiketi eklendi. **Google bu etiketi sıralamada kullanmaz**. Gerçek arama görünürlüğü için özgün ürün açıklamaları, referanslar, sitenin güvenilirliği, mobil deneyim, linkler ve Search Console verileri daha önemlidir.

## 4) Kullanılan yapılandırılmış veri

Ana sayfada `WebSite`, `Organization` ve `CollectionPage` / `ItemList`: yalnızca sitede gerçekten görünen 14 ürün listelenir. Beş rehber sayfasında `TechArticle` ve `BreadcrumbList` bulunur. Olmayan fiyat, yıldız puanı, sertifika, resmî bayilik, fiziksel adres veya yorum icat edilmez. JSON-LD yalnızca arama motorları için veri formatıdır, **çalıştırılan JavaScript değildir**. Yayın sunucusunun CSP başlıkları korunmuştur.

## 5) Marka ve görsel hakları

POLİMETER ürün adları ve fotoğrafları ilgili hak sahiplerinindir. Markayla anlaşma yapılana kadar site kendisini resmî bayi olarak tanımlamaz. Yayına almadan önce görsel kullanım izni alın ve mümkünse fotoğrafları kendi alan adınızda barındırın.

## 6) Hedef ve dürüst sınırlar

Teknik SEO sitenin anlaşılabilirliğini ve dizine eklenebilirliğini iyileştirir; **Google'da ilk sırayı, dizine alınmayı veya belirli bir süreyi garanti etmez**. Sıralama, rekabet ve domainin geçmişi gibi dış etkenlere bağlıdır. Alan adı değiştiğinde canonical ve sitemap bilgilerini yeniden üretin.

Kaynak: [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [Meta keywords hakkında resmî açıklama](https://developers.google.com/search/docs/crawling-indexing/special-tags), [Canonical URL kılavuzu](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

## Ayrı hizmet sayfaları

5 adet uzun-form hizmet bilgilendirme sayfası `hizmetler/` klasörüne eklendi. Her sayfanın kendine özgü title, description, canonical ve Article/BreadcrumbList yapılandırılmış verisi vardır. Ana sayfadaki Hizmetlerimiz menüsü bu sayfalara bağlantı verir. İçerikler teknik bilgilendirme amaçlıdır, firma adına resmî yetki veya onay iddiası içermez. Sayfalar `python tools/build_services.py` ile yeniden üretilebilir.
