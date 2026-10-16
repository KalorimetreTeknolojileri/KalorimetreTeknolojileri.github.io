#!/usr/bin/env python3
"""Build helpful, original Turkish product guides; never duplicate competitor copy.
Guides use a shared design stylesheet and intentionally make no service/price claims.
"""
from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
DOMAIN='https://kalorimetreteknolojileri.com'

GUIDES=[
 {
  'slug':'kalorimetre-nedir', 'title':'Kalorimetre Nedir? Ne İşe Yarar, Nasıl Okunur?',
  'desc':'Kalorimetre ve ısı sayacı nedir? Isı enerjisi nasıl ölçülür, kalorimetre nasıl okunur, DN çapı ve uzaktan okuma seçimi nasıl yapılır?',
  'kicker':'01 / TEMEL BİLGİLER', 'lead':'Kalorimetre, bir ısıtma veya soğutma devresinde aktarılan ısı enerjisini ölçmeye yarayan cihazdır. Bina ve tesisatlarda tüketimin izlenmesini kolaylaştırır.',
  'sections':[
    ('Kalorimetre ne işe yarar?', [
       'Isı sayacı olarak da adlandırılan kalorimetre, devreden geçen akışkanın debisi ile giriş-çıkış sıcaklıkları arasındaki farkı kullanarak enerji miktarını hesaplar. Bu nedenle yalnızca su hacmini ölçen bir su sayacından farklıdır.',
       'Merkezi ısıtma sistemi kullanılan binalarda daire, bağımsız bölüm veya belirli bir hattın enerji tüketimini izlemek için değerlendirilebilir. Tüketim verisinin gider paylaşımında kullanılması ise tesisat düzenine ve geçerli mevzuata bağlıdır.'
    ]),
    ('Kalorimetre nasıl çalışır, nasıl okunur?', [
       'Kalorimetre çalışırken debi sensörü, sıcaklık sensörleri ve hesaplayıcı birlikte çalışır. Ekranda genellikle birikimli enerji, sıcaklık, debi ya da hacim gibi bilgiler gösterilir; görüntülenen birimler cihazın modeline ve yapılandırmasına göre değişir.',
       'Kalorimetre okuma işlemi sırasında ekrandaki enerji değerinin birimini (örneğin kWh veya MWh) doğrulayın. Aynı cihazın iki farklı dönemdeki birikimli okuma değerleri arasındaki fark ilgili dönemde ölçülen enerji hakkında bilgi verir. Uzaktan okuma özelliği tüm modellerde standart değildir.'
    ]),
    ('Kalorimetre seçerken neye bakılmalı?', [
       'Bağlantı çapı (DN15, DN20, DN25 ya da daha büyük çaplar), sürekli ve minimum debi, sıcaklık aralığı, montaj yönü ve tesisat suyunun özellikleri temel parametrelerdir. M-Bus kalorimetre veya kablosuz okuma ihtiyacı varsa, bu iletişim özelliğinin ilgili ürün varyantında bulunup bulunmadığı kontrol edilmelidir.',
       'Ultrasonik ve mekanik kalorimetre farklı ölçüm yöntemleri kullanır. Projeye uygun sayaç seçimi, yalnızca fiyat karşılaştırması yapılarak değil teknik veri sayfası ve tesisat koşulları değerlendirilerek yapılmalıdır.'
    ])
  ],
  'related':['ultrasonik-mekanik-kalorimetre','kalorimetre-fiyatlari','isi-pay-olcer-merkezi-isitma','su-sayaci-secimi']
 },
 {
  'slug':'ultrasonik-mekanik-kalorimetre', 'title':'Ultrasonik ve Mekanik Kalorimetre Arasındaki Farklar',
  'desc':'Ultrasonik kalorimetre ile mekanik kalorimetre karşılaştırması: ölçüm prensibi, hareketli parçalar, tesisat şartları, DN çapı ve model seçimi.',
  'kicker':'02 / TEKNOLOJİ KARŞILAŞTIRMASI', 'lead':'Bir kalorimetre seçerken ilk ayrımlardan biri debinin ultrasonik yöntemle mi, mekanik ölçüm elemanıyla mı izlendiğidir. Doğru tercih kullanım senaryosuna bağlıdır.',
  'sections':[
    ('Ultrasonik kalorimetre nedir?', [
      'Ultrasonik kalorimetre, akışı ses dalgalarının geçiş süresini veya modeline özgü ultrasonik ölçüm prensibini kullanarak belirler. Akış bölümünde türbin gibi dönen mekanik bir ölçüm elemanı bulunmaması, hareketli parça kaynaklı aşınma bakımından avantaj sağlayabilir.',
      'POLİMETER PM01 ve PM02 gibi ultrasonik ısı sayacı modelleri, ilgili ürünün ölçü ve bağlantı seçeneklerine göre incelenmelidir. Ürünün M-Bus veya başka bir haberleşme seçeneği sunması model ve varyanta bağlıdır.'
    ]),
    ('Mekanik kalorimetre nedir?', [
      'Mekanik kalorimetre debiyi hareketli bir ölçüm mekanizmasıyla takip eder. Sıcaklık farkı ve debi bilgisinden hesaplanan enerji değeri yine cihazın hesaplama ünitesinde gösterilir.',
      'POLİMETER M-15 ve CALMET M-20 mekanik kalorimetre modelleri karşılaştırılırken akış aralığı, montaj şartları, tesisat kalitesi ve kullanım amacı göz önünde bulundurulmalıdır.'
    ]),
    ('Hangi kalorimetre daha uygun?', [
      'Ultrasonik ve mekanik kalorimetre arasında seçim yaparken mevcut boru çapını, minimum/sürekli debiyi, suyun fiziksel özelliklerini, basınç kaybını ve gereken haberleşme biçimini karşılaştırın. Üretici teknik dokümanları performans koşullarını belirler.',
      'DN20 ultrasonik kalorimetre ile DN50 büyük çaplı bir kalorimetre farklı akış kapasitelerine yöneliktir; birinin diğerinden her projede daha iyi olduğunu söylemek doğru değildir. Nihai model ve montaj seçimini yetkili uygulayıcıyla doğrulayın.'
    ])
  ],'related':['kalorimetre-nedir','kalorimetre-fiyatlari','su-sayaci-secimi']
 },
 {
  'slug':'kalorimetre-fiyatlari', 'title':'Kalorimetre Fiyatları Neye Göre Değişir?',
  'desc':'Kalorimetre fiyatları, ultrasonik ve mekanik ısı sayacı fiyatlarını etkileyen DN ölçüsü, haberleşme, debi ve proje ihtiyaçları hakkında rehber.',
  'kicker':'03 / ÜRÜN VE TEKLİF', 'lead':'Kalorimetre fiyatı model, bağlantı çapı ve ihtiyaç duyulan özelliklere göre değişir. Güncel fiyat için ürünün teknik varyantını netleştirmek önemlidir.',
  'sections':[
    ('Ultrasonik kalorimetre fiyatları neden farklı?', [
      'Ultrasonik kalorimetre fiyatlarını etkileyen konular arasında ölçüm çapı (DN15, DN20, DN25, DN50 gibi), debi sınıfı, çalışma sıcaklıkları, ekran özellikleri ve iletişim modülü bulunur. Aynı ürün ailesinin uzaktan okumaya uygun varyantı ile standart varyantı farklı olabilir.',
      'M-Bus kalorimetre, kablosuz haberleşme veya projeye özel bağlantı gereksinimi mevcutsa, teklif talebinde bu bilgileri açıkça belirtin. Yalnızca cihaz adıyla arama yapmak, aynı teknik özellikte ürün karşılaştırması sağlamak için yeterli olmayabilir.'
    ]),
    ('Mekanik kalorimetre fiyatları nasıl karşılaştırılır?', [
      'Mekanik kalorimetrelerde gövde ölçüsü, debi aralığı, sayaç mekanizması, ekran ve haberleşme seçeneği fiyat karşılaştırmasında etkili olabilir. Sıcaklık sensörü setinin, montaj elemanlarının ve gerekli bağlantı parçalarının teklife dahil olup olmadığı da sorulmalıdır.',
      'Kalorimetre fiyat listesi araştırırken kalibrasyon veya uygunluk belgelerini, garanti koşullarını ve üretici teknik verilerini karşılaştırın. Belirli bir modelin güncel satış fiyatı, satıcı teklifinden teyit edilmelidir.'
    ]),
    ('Proje için doğru teklif nasıl istenir?', [
      'Tesisat çapı (DN), adet, kullanım amacı, akış ve sıcaklık koşulları, istenen haberleşme protokolü ve teslimat konumu, ürün teklifinin hazırlanmasında yardımcı bilgilerdir.',
      'Sitemizde doğrudan online sipariş özelliği bulunmuyor. Ürün incelemesinden sonra iletişim bölümüne geçerek sipariş veya teklif talebinizi iletebilirsiniz; bu sayfada doğrulanmamış fiyat, stok ya da kampanya bilgisi yayımlamıyoruz.'
    ])
  ],'related':['ultrasonik-mekanik-kalorimetre','kalorimetre-nedir','su-sayaci-secimi']
 },
 {
  'slug':'isi-pay-olcer-merkezi-isitma', 'title':'Isı Pay Ölçer ile Kalorimetre Arasındaki Fark',
  'desc':'Merkezi ısıtma, ısı pay ölçer ve kalorimetre farkı nedir? Isı gider paylaşımı, kalorimetre okuma ve merkezi sistem sayaçları hakkında bilgiler.',
  'kicker':'04 / MERKEZİ ISITMA', 'lead':'Merkezi ısıtma sistemlerinde “ısı pay ölçer” ve “kalorimetre” ifadeleri sıkça birlikte geçer; ancak bu cihazlar aynı ölçüm yöntemini kullanmaz.',
  'sections':[
    ('Isı pay ölçer nedir?', [
      'Isı pay ölçer, genellikle radyatöre takılan ve radyatörün yaydığı ısıya ilişkin ölçüm değerleri üreten bir cihazdır. Bu değerler, ilgili yöntemin kurallarına göre daireler arasında gider paylaşımında kullanılabilir. Tek başına bir kalorimetre gibi tesisattan geçen toplam ısı enerjisini doğrudan ölçmez.',
      'Kalorimetre ise debi ve sıcaklık farkı üzerinden enerji miktarını hesaplayan ısı sayacıdır. Hangi yöntemin uygulanabildiği, binanın tesisat tipine ve yürürlükteki gerekliliklere bağlıdır.'
    ]),
    ('Merkezi sistem kalorimetre okuma nasıl yapılır?', [
      'Merkezi ısıtma kalorimetre değerleri ekran üzerinden veya cihaz ve sistem destekliyorsa uygun uzaktan okuma altyapısı üzerinden alınabilir. Ekranda gösterilen ölçü birimi ve tarih bilgileri faturadaki değerlerle karşılaştırılırken mutlaka doğrulanmalıdır.',
      'Kalorimetre hesaplama veya ısı gider paylaşımı yalnızca iki sayının çıkarılmasından ibaret olmayabilir. Binaya uygulanacak hesap yöntemi, ortak alanlar ve ilgili mevzuat, görevli uzmanlar tarafından ele alınmalıdır.'
    ]),
    ('Cihaz seçimi ve montaj', [
      'Merkezi sistem ısıtma uygulamasında daire bağlantıları, debi koşulları ve kablolama / haberleşme altyapısı incelenir. Termostatik vana, ısı pay ölçer, ultrasonik veya mekanik kalorimetre gibi farklı ekipmanların görevleri karıştırılmamalıdır.',
      'Bu rehber teknik ayrımları açıklamak içindir; mevcut sitemiz ısı pay ölçer okuma veya faturalandırma hizmeti verdiğini iddia etmez. Projeniz için iletişim bölümümüzü kullanabilirsiniz.'
    ])
  ],'related':['kalorimetre-nedir','ultrasonik-mekanik-kalorimetre','kalorimetre-fiyatlari']
 },
 {
  'slug':'su-sayaci-secimi', 'title':'Sıcak ve Soğuk Su Sayacı Nasıl Seçilir?',
  'desc':'Sıcak su sayacı ve soğuk su sayacı arasındaki farklar, ultrasonik ve mekanik su sayacı çeşitleri, uygun bağlantı çapı ve seçimi.',
  'kicker':'05 / SU ÖLÇÜMÜ', 'lead':'Sıcak su sayacı ve soğuk su sayacı, su tüketiminin hacim olarak izlenmesini sağlar. Seçimde kullanılan suyun sıcaklığı ve tesisatın teknik koşulları belirleyicidir.',
  'sections':[
    ('Sıcak su sayacı ile soğuk su sayacı arasındaki fark', [
      'Sıcak su sayaçları daha yüksek sıcaklıklarda çalışmaya uygun ürün özelliklerine sahip olabilir. Soğuk su sayaçları ise üreticinin belirttiği sıcaklık sınırları içinde kullanılmalıdır. Montaj öncesinde model etiketindeki sıcaklık sınıfı kontrol edilmelidir.',
      'Sıcak su saati veya soğuk su saati olarak aranan ürünleri seçerken bağlantı çapı, nominal debi, basınç sınıfı ve onaylı kullanım koşullarını inceleyin.'
    ]),
    ('Ultrasonik ve mekanik su sayacı', [
      'Ultrasonik su sayacı akış ölçümünde ses dalgalarından yararlanırken mekanik su sayacı hareketli ölçüm elemanları kullanır. Seçim yapılırken cihazın hassasiyet aralığı, montaj şekli ve olası uzaktan okuma gereksinimi dikkate alınmalıdır.',
      'CALMET ultrasonik sıcak/soğuk su ve mekanik su sayacı modellerinin karşılaştırılabilmesi için teknik ürün dokümanındaki bağlantı, debi ve sıcaklık verilerinin aynı koşullarda incelenmesi gerekir.'
    ]),
    ('Isı sayacı ve doğalgaz sayacıyla karıştırmayın', [
      'Su sayacı hacim ölçer; kalorimetre (ısı sayacı) ise debi ve sıcaklık farkından hesaplanan ısı enerjisini gösterir. Doğalgaz sayacı farklı bir akışkan ve farklı uygunluk gereklilikleri için tasarlanmıştır.',
      'Su veya doğalgaz tesisatına ilişkin sayaç seçimi, yerel kuruluş şartları ve geçerli kurallarla birlikte uzmanlar tarafından doğrulanmalıdır. Sipariş ve ürün teklifi için iletişim bölümümüze başvurabilirsiniz.'
    ])
  ],'related':['kalorimetre-nedir','ultrasonik-mekanik-kalorimetre','kalorimetre-fiyatlari']
 }
]

NAMES={g['slug']:g['title'] for g in GUIDES}
STYLES='../../assets/guide.css'

def render(g):
    title=escape(g['title']); desc=escape(g['desc'],quote=True)
    canonical=f"{DOMAIN}/rehber/{g['slug']}/"
    crumb=[{'@type':'ListItem','position':1,'name':'Ana sayfa','item':DOMAIN+'/'},{'@type':'ListItem','position':2,'name':'Teknik rehber','item':DOMAIN+'/rehber/kalorimetre-nedir/'},{'@type':'ListItem','position':3,'name':g['title'],'item':canonical}]
    schema={'@context':'https://schema.org','@graph':[{'@type':'TechArticle','headline':g['title'],'description':g['desc'],'inLanguage':'tr-TR','mainEntityOfPage':canonical,'publisher':{'@type':'Organization','name':'D & E | Kalorimetre Teknolojileri','url':DOMAIN+'/'}},{'@type':'BreadcrumbList','itemListElement':crumb}]}
    structured=json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')
    sections='\n'.join('<section class="guide-section"><h2>'+escape(heading)+'</h2>'+''.join('<p>'+escape(p)+'</p>' for p in paras)+'</section>' for heading,paras in g['sections'])
    other=''.join(f'<li><a href="../{slug}/index.html">{escape(NAMES[slug])} <span aria-hidden="true">↗</span></a></li>' for slug in g['related'])
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="theme-color" content="#080c0d"/>
<title>{title} | D &amp; E Kalorimetre Teknolojileri</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index, follow, max-image-preview:large"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:type" content="article"/>
<meta property="og:locale" content="tr_TR"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{DOMAIN}/assets/industrial-night.jpg"/>
<link href="../../favicon.svg" rel="icon" type="image/svg+xml"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Playfair+Display:ital,wght@0,400;1,400&amp;display=swap" rel="stylesheet"/>
<link href="{STYLES}" rel="stylesheet"/>
<script type="application/ld+json">{structured}</script>
</head>
<body>
<div class="guide-ribbon"><span>D &amp; E / KNOWLEDGE</span><span>HASSAS ÖLÇÜM · SEÇKİN TEKNOLOJİ</span></div>
<header class="guide-header"><a href="../../index.html" class="guide-brand" aria-label="D & E ana sayfa"><strong>D <em>&amp;</em> E<span>.</span></strong><small>KALORİMETRE TEKNOLOJİLERİ</small></a><nav><a href="../../index.html#koleksiyon">KOLEKSİYON</a><a href="../../index.html#iletisim">İLETİŞİM ↗</a></nav></header>
<main>
<div class="guide-hero"><div class="guide-max"><div class="guide-path"><a href="../../index.html">ANA SAYFA</a><span>/</span><span>TEKNİK REHBER</span></div><p class="guide-kicker">✦ &nbsp; {escape(g['kicker'])}</p><h1>{title}</h1><p class="guide-lead">{escape(g['lead'])}</p><div class="guide-rule"><span>ÖLÇÜM TEKNOLOJİLERİ</span><span>↓ REHBER</span></div></div></div>
<div class="guide-max guide-body"><article class="guide-article">{sections}<div class="guide-action"><span>PROJENİZE UYGUN ÜRÜNÜ MÜ ARIYORSUNUZ?</span><a href="../../index.html#iletisim">İLETİŞİME GEÇİN <b aria-hidden="true">↗</b></a></div></article>
<aside class="guide-aside"><p class="guide-aside-head">İLGİLİ REHBERLER</p><ul>{other}</ul><div class="guide-note"><span>✦</span><p>Buradaki bilgiler genel bilgilendirme içindir. Uygun model ve tesisat uygulamasını teknik belgeler üzerinden doğrulayın.</p></div></aside></div>
</main>
<footer class="guide-footer"><div class="guide-max"><a class="guide-footer-brand" href="../../index.html">D <em>&amp;</em> E<span>.</span></a><span>© 2026 KALORİMETRE TEKNOLOJİLERİ</span><a href="../../index.html">ANA SAYFAYA DÖN ↑</a></div></footer>
</body>
</html>'''

for g in GUIDES:
    d=ROOT/'rehber'/g['slug']; d.mkdir(parents=True,exist_ok=True)
    (d/'index.html').write_text(render(g), encoding='utf-8')
print('Guide pages generated:',len(GUIDES))
