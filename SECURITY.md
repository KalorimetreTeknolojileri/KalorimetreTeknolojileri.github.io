# Kalorimetre Teknolojileri — güvenlik ve bakım notları

## Mimari ve kapsam
Bu sürüm **statik HTML/CSS/JavaScript** sitesidir. Kullanıcı hesabı, veri tabanı, ödeme sistemi ve veri alan bir arka uç bulunmaz. “Talep metnini hazırla ve kopyala” işlemi tarayıcıda yürür; form verisi sunucuya iletilmez. İsteğe bağlı teklif listesi tarayıcının kendi `localStorage` alanına, yalnızca ürün kimlikleri olarak kaydedilir.

## Uygulanan kontroller
- **Katı İçerik Güvenliği Politikası (CSP):** Yalnızca kendi JS/CSS dosyaları ve kullanılan görsel/font kaynakları izinlidir. Inline JavaScript, eval, nesne/çerçeve gömme, network `connect` ve form gönderimi engellenir. Trusted Types kullanan tarayıcılarda tehlikeli HTML sink'leri de engellenir.
- **Üçüncü taraf sınırlandırması:** Ürün fotoğrafları yalnızca tanımlanan üç HTTPS alan adından gösterilir. Üçüncü taraf JavaScript yoktur. Referrer bilgisi gönderilmez. Google Fonts hâlâ dış kaynaktır.
- **DOM güvenliği:** Ürün ve kullanıcı verisi HTML olarak yorumlanmaz; `textContent`, `createElement` ve gerekli DOM API'leriyle işlenir.
- **Depolama doğrulaması:** Kaydedilen ürün kimlikleri güvenilir katalog ile eşleştirilir, tekrarlar ayıklanır ve büyük/bozuk veri reddedilir. Formdaki HTML maxlength sınırları korunur.
- **Bütünlük:** Yerel CSS ve JS dosyalarının SHA-384 özetleri `assets/asset-hashes.sha384` içindeki geliştirme kontrol listesinde tutulur. İstemci tarafında SRI kullanılmaz; bu, `file://` ile önizlemede kaynakların engellenmesini önler. Sunucuda yerel kaynakların güvenli sunumu ayrıca kontrol edilmelidir.
- **Sunucu başlıkları:** Netlify için `_headers`, Vercel için `vercel.json`, Apache için `.htaccess` sağlanır. Bunlar CSP, no-sniff, clickjacking engeli, kamera/mikrofon izni kısıtlaması ve HTTPS HSTS içerir.
- **JavaScript'siz güvenlik:** Formdaki `method=post` ve CSP `form-action 'none'` ile formun ad, e-posta ve mesajı URL sorgu parametresi olarak sunucuya gönderilmez.

## Yayına alma: önemli sınırlar
1. Yalnızca **HTTPS** üzerinden yayınlayın. HSTS yalnızca doğru HTTP başlığı sunucudan döndüğünde çalışır.
2. **GitHub Pages kendi HTTP security header'larını yapılandırmaya izin vermez.** Yerel önizlemeyi kolaylaştırmak için sayfa içi CSP kaldırıldı. GitHub Pages üzerinde otomatik CSP uygulanmaz; üretim ortamında eksiksiz güvenlik başlıkları için Netlify, Vercel, Cloudflare veya bu başlıkları sağlayan bir hosting tercih edin.
3. Üçüncü taraf ürün resimleri ve Google Fonts nedeniyle dış sağlayıcılarla ağ iletişimi olur. Satıcı görselleri değişebilir veya erişilemeyebilir. Üretici/satıcıdan izin alındıktan sonra görselleri kendi sunucunuza taşımak, `img-src` alan adlarını kaldırmak ve fontları kendiniz barındırmak daha güçlü gizlilik ve kesintisizlik sağlar.
4. `_headers`, `vercel.json` ve `.htaccess` yalnızca **ilgili platformda** uygulanır; ZIP dosyasından `index.html` açmak veya `file://` ile görüntülemek sunucu başlıklarını uygulamaz. ZIP dosyalarını tamamen çıkarın. Fotoğraflar internet gerektirir.
5. Gelecekte gerçek teklif gönderimi, kullanıcı hesabı, ödeme veya yönetim paneli eklenirse **ayrı sunucu tarafı doğrulama, oturum yönetimi, CSRF koruması, rate limit, erişim kontrolü, log izleme ve bağımsız güvenlik testi** gerekir. Bu statik önlemler o ihtiyaçların yerini tutmaz.
6. CSP veya dış kaynak alan adları değiştirildiğinde Netlify/Vercel/Apache politikalarını birlikte güncelleyin; yerel JS/CSS değiştiğinde SHA-384 raporunu `python3 tools/update_integrity.py` ile yeniden üretin.

## Testler
`tests/security_smoke.py` ile tarayıcı tabanlı yerel test yapılabilir (`python -m pip install playwright`, Chromium kurulumu gerekir). Dış kaynaklar ağ/sağlayıcıya bağlı olduğundan görsel testleri kaynak erişilebilirliğini garanti etmez.

## Güvenlik için iletişim
Üretim ortamında özel bir güvenlik iletişim e-postası belirlenmeden `.well-known/security.txt` yayımlamayın. Düzenli bağımlılık, kaynak ve tarayıcı incelemeleriyle kontrolleri sürdürün.
