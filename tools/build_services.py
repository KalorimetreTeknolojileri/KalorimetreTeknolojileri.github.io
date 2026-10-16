#!/usr/bin/env python3
"""Build original, detailed Turkish service explainer pages in the D & E visual language.
Pages describe technical processes without claiming certification or a confirmed service scope.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://kalorimetreteknolojileri.com'

SERVICES = [
 {
  'slug':'kalorimetre-okuma', 'title':'Kalorimetre Okuma ve Isı Gider Paylaşımı', 'short':'Kalorimetre Okuma',
  'meta':'Kalorimetre okuma nasıl yapılır? Isı sayacı tüketim takibi, M-Bus uzaktan okuma, merkezi ısıtma gider paylaşımı ve raporlama adımları.',
  'eyebrow':'01 / TÜKETİMİN TAKİBİ', 'lead':'Ölçüm verilerinin doğru okunması; merkezi ısıtma sistemlerinde şeffaf takip, karşılaştırılabilir tüketim bilgisi ve sağlıklı kararlar için ilk adımdır.',
  'intro_title':'Her dairenin tüketimini anlamak, doğru veriyi okumakla başlar.',
  'intro':[
   'Kalorimetre, suyun tesisattan geçişini ve gidiş-dönüş hatları arasındaki sıcaklık farkını kullanarak aktarılan ısı enerjisini hesaplar. Okuma işlemi yalnızca ekrandaki rakamın not alınması değildir: ölçüm birimi, sayaç kimliği, okuma tarihi ve önceki dönem değeri birlikte değerlendirilmelidir.',
   'Merkezi ısıtma kullanılan binalarda tüketim verileri, ısı gider paylaşımının girdilerinden biridir. Paylaştırma yönteminin seçimi binanın tesisat yapısına, gider kalemlerine ve yürürlükteki kurallara göre yapılır. Bu nedenle cihaz okuması ile yasal gider paylaşımı aynı işlem olarak görülmemelidir.'
  ],
  'steps':[
   ('Sayaç envanteri','Daire, bağımsız bölüm, sayaç seri numarası ve cihazın ölçüm birimi eşleştirilir.'),
   ('Okuma yöntemi','Cihazdan ekrandaki değer alınır veya destekleniyorsa uygun iletişim altyapısı kullanılır.'),
   ('Veri kontrolü','Tarihler, birimler, sıra dışı artışlar ve eksik kayıtlar kontrol edilir.'),
   ('Raporlama','Dönemsel farklar karşılaştırılır; gider paylaşımı ayrıca yetkin uzmanlarca değerlendirilir.')
  ],
  'sections':[
   ('Kalorimetre nasıl okunur?',[
    'Kalorimetre ekranlarında birikimli enerji, hacim, anlık debi, gidiş/dönüş sıcaklığı ve varsa hata kodları farklı menülerde bulunabilir. Üreticiye göre ekran sırası ve işaretler değiştiği için öncelikle cihaz kullanım kılavuzundaki gösterge açıklamalarına bakılır. Özellikle kWh, MWh veya GJ gibi enerji birimlerinin karıştırılmaması gerekir.',
    'Dönemsel tüketim, aynı sayacın iki okuma tarihindeki karşılaştırılabilir birikimli enerji değerleri arasındaki farktan anlaşılabilir. Örneğin ilk değer farklı birimdeyse veya cihaz değişimi yapılmışsa basit çıkarma işlemi yanıltıcı olur. Okuma tutanağına sayaç numarası ve tarih eklenmesi sonradan yapılacak kontrolleri kolaylaştırır.'
   ]),
   ('Manuel okuma ile uzaktan okuma arasındaki fark',[
    'Manuel okumada görevli kişi cihaz ekranını veya kayıt ekranını kontrol eder. Az sayıda sayaç bulunan tesisatlarda uygulanabilir olsa da tüm bağımsız bölümlere düzenli erişim gerektirebilir. Çok sayıda sayaç bulunan yapılarda bu süreç zaman alabilir ve veri girişinin iki kez kontrol edilmesi gerekebilir.',
    'M-Bus, kablosuz RF ya da üreticiye özgü başka bir arabirimi bulunan sayaçlarda uyumlu toplama cihazları kullanılarak veriler merkezi noktaya taşınabilir. Ancak uzaktan okuma desteği her kalorimetrede standart değildir. Haberleşme arabirimi, kablolama topolojisi, besleme şartları ve okunacak veri alanları proje öncesinde doğrulanmalıdır.'
   ]),
   ('Isı gider paylaşımında hangi bilgiler önemlidir?',[
    'Toplam ısıtma gideri, bağımsız bölümlerin tüketim kayıtları, ortak kullanım alanları, sistemin kurulu olduğu yapının özellikleri ve ilgili düzenlemeler birlikte ele alınır. Tek başına bir kalorimetre ekranı, nihai ödeme tutarını belirlemek için yeterli olmayabilir. Özellikle ortak gider ve tüketim esaslı kalemler uzmanlık gerektirir.',
    'Daire bazlı hesaplarda cihazın hata durumu, kullanım dışı bırakılması, yeni kurulum veya değişim tarihi gibi olaylar açıklığa kavuşturulmalıdır. Tüm bağımsız bölümlerde aynı dönem aralığının kullanılması ve olağan dışı tüketimlerin kontrol edilmesi raporların okunabilirliğini artırır.'
   ]),
   ('Yönetimlerin teslim alabileceği rapor türleri',[
    'Ölçüm envanteri; hangi sayaç hangi bağımsız bölüme aittir sorusunu yanıtlar. Dönemsel tüketim listesi, önceki ve yeni okuma değerlerini bir arada sunar. Kontrol listesinde iletişim kopukluğu, eksik sayaç veya beklenmeyen tüketim gibi gözden geçirilmesi gereken durumlar işaretlenebilir.',
    'Bu tür kayıtlar bina yönetimiyle sakinler arasında şeffaf iletişim kurulmasına yardımcı olur. Raporun kapsamı ve kişisel verilerin erişimi, kullanılacak sistem ve yetkilendirme düzenine göre belirlenmelidir. Bina adına yasal gider paylaşım belgesi düzenlenmesi gerekiyorsa görev ve yetki koşulları ayrıca kontrol edilmelidir.'
   ]),
   ('Okuma hizmeti veya sistem değerlendirmesi için hangi bilgiler hazırlanmalı?',[
    'Toplam daire sayısı, sayaç markası ve modeli, mevcut okuma yöntemi, binanın bulunduğu il, kablolu/kablosuz haberleşme durumu ve varsa örnek bir sayaç ekran fotoğrafı başlangıç için faydalıdır. Ayrıca hizmet talebinin yalnızca veri toplama mı yoksa mevzuata uygun gider paylaşımı mı içerdiği açıkça belirtilmelidir.',
    'D & E üzerinden proje ihtiyacınızı ileterek ürün, haberleşme ve uygulanabilir çözüm seçenekleri hakkında görüşebilirsiniz. Hizmetin kapsamı ile gerekli yetkiler, uygulamaya geçilmeden önce ayrıca netleştirilmelidir.'
   ])
  ],
  'faq':[
   ('Kalorimetre değerleri neden her ay artar?','Pek çok model birikimli enerji değeri gösterir. İlgili ayın tüketimi, uygun koşullarda iki tarih arasındaki değer farkı ile değerlendirilir.'),
   ('M-Bus olmayan kalorimetre uzaktan okunabilir mi?','Modelin desteklediği arabirime ve üreticinin sunduğu seçeneklere bağlıdır. Her cihazın sonradan uzaktan okumaya dönüştürülebileceği varsayılmamalıdır.'),
   ('Kalorimetre okuma ile faturalandırma aynı şey mi?','Hayır. Verinin okunması teknik bir işlemdir; gider paylaştırma ve belge düzenleme, ek hesap adımları ve mevzuat değerlendirmesi gerektirebilir.')
  ],
  'visual':'dashboard', 'badge':'READING / ENERGY DATA', 'visual_caption':'Okuma paneli — yalnızca temsili arayüz',
 },
 {
  'slug':'kalibrasyon-muayene', 'title':'Kalorimetre Kalibrasyon ve Muayene Rehberi', 'short':'Kalibrasyon ve Muayene',
  'meta':'Kalorimetre kalibrasyonu ve periyodik muayenesi nedir? Isı sayacı kontrolü, belgelendirme, hata tespiti ve bakım süreçlerini öğrenin.',
  'eyebrow':'02 / ÖLÇÜM GÜVENİLİRLİĞİ', 'lead':'Doğru ölçüm yalnızca hassas bir cihaz seçmekten ibaret değildir. Sayaçların teknik uygunluğu, bakım koşulları ve gerektiğinde yetkili muayene süreçleri de önem taşır.',
  'intro_title':'Ölçümde güven, düzenli kontrol ve doğru prosedürle korunur.',
  'intro':[
   'Kalorimetreler kullanım boyunca farklı debi, sıcaklık ve çevre koşullarına maruz kalır. Zaman içinde oluşabilecek arızalar, sensör bağlantı sorunları veya mekanik aşınma ölçüm sonuçlarını etkileyebilir. Kalibrasyon ve muayene, bir cihazın durumunu sistematik biçimde değerlendirmek için birbirini tamamlayan fakat farklı amaçlara hizmet eden kavramlardır.',
   'Kalibrasyon, cihaz göstergesinin belirli referans koşullarda nasıl davrandığını ortaya koyan teknik karşılaştırmadır. Muayene ise ilgili mevzuatın belirlediği resmî koşullarda uygunluk değerlendirmesi içerebilir. Bir kalibrasyon raporunun tek başına zorunlu yasal muayenenin yerine geçtiği varsayılmamalıdır.'
  ],
  'steps':[
   ('Kimlik kontrolü','Sayaç modeli, seri numarası, ölçüm aralığı, mühür ve mevcut belgeler incelenir.'),
   ('Durum tespiti','Hata kodları, algılayıcı bağlantıları, tesisat koşulları ve fiziksel durum değerlendirilir.'),
   ('Yetkili işlem','Gerekli test veya muayene, ilgili mevzuata uygun yetkili kuruluşça yürütülür.'),
   ('Belge ve takip','İşlem sonucu, cihaz kimliği ve sonraki kontrol ihtiyacı kayıt altına alınır.')
  ],
  'sections':[
   ('Kalibrasyon ile muayene arasındaki temel fark',[
    'Kalibrasyon, ölçüm cihazından okunan değer ile izlenebilir bir referansın değeri arasındaki ilişkiyi belirler. Sonuç, kullanılan yönteme göre ölçüm hatası ve belirsizlik gibi bilgileri içerebilir. Kalibrasyon yapılmış olmak cihazın tüm koşullarda otomatik olarak uygun bulunduğu anlamına gelmez.',
    'Muayene ise kullanılan ısı sayacının mevzuat ve teknik kurallar kapsamındaki şartları sağlayıp sağlamadığının incelenmesidir. Muayene türü, başvuru şekli, gerekli evrak ve uygulanacak yöntem cihazın sınıfına ve güncel düzenlemelere göre değişebilir. Zorunlu süreçlerde yetkili kurumların açıklamaları esas alınmalıdır.'
   ]),
   ('Periyodik muayene zamanı nasıl takip edilir?',[
    'Isı sayaçlarına ilişkin periyodik muayene gereklilikleri Türkiye’de özel mevzuatla düzenlenmektedir. Yaygın olarak beş yıllık periyotla anılan ısı sayacı muayenesinde güncel yükümlülük, istisnalar, başvuru dönemi ve yetki koşulları için yürürlükteki mevzuat incelenmelidir. Bu sayfadaki bilgi bir takvim veya resmî işlem talimatı yerine geçmez.',
    'Bina yönetimlerinin sayaç listesinde ilk kullanım yılı, önceki muayene bilgisi, seri numarası ve varsa cihaz değişim tarihini tutması önemlidir. Farklı dönemlerde takılan sayaçlar için tek bir başlangıç tarihi varsaymak yanlış planlamaya yol açabilir.'
   ]),
   ('Muayene öncesinde neler kontrol edilir?',[
    'Sayaç ekranının çalışması, debi veya sıcaklık hata kodları, sensör kabloları ve mühür durumu ilk aşamada gözden geçirilebilir. Enerji birimi ve cihazın teknik etiketi fotoğraflanarak envanterle karşılaştırılabilir. Fiziksel sökme ve müdahale işlemleri eğitimli, yetkili kişilerce yapılmalıdır.',
    'Mekanik kalorimetrelerde akış bölümündeki kirlenme ve mekanizmanın aşınması; ultrasonik modellerde sensör, bağlantı ve akış koşulları farklı kontrol başlıkları oluşturabilir. Kesin değerlendirme için her zaman üretici belgesi ve yetkili muayene yöntemi esas alınır.'
   ]),
   ('Uygunsuzluk tespit edilirse hangi yol izlenir?',[
    'Cihazın türüne, arızanın kaynağına, parça teminine ve ilgili kurallara bağlı olarak onarım, uygunluk kontrolü veya değişim seçenekleri değerlendirilir. Özellikle muayene başarısızlığı gibi resmî durumlarda nasıl işlem yapılacağına yetkili kuruluşların bildirimleri doğrultusunda karar verilmelidir.',
    'Sayaç değişimi gerekiyorsa eski cihazın son okuma değeri, yeni cihazın ilk değeri, kurulum tarihi ve seri numaraları eksiksiz kaydedilmelidir. Böylece sonraki tüketim karşılaştırmalarında kayıt sürekliliği sağlanır.'
   ]),
   ('Teklif ve planlama için hangi belgeler faydalı?',[
    'Sayaç adedi, marka-model listesi, kullanım yılı, mevcut muayene belgeleri, tesisat adresi ve işlem yapılabilecek dönem bilgisi ilk görüşmede gereksiz gecikmeleri azaltır. Birden çok model kullanılıyorsa cihazlar ayrı gruplandırılabilir.',
    'D & E ile iletişime geçerek uygun ürün ve teknik süreçler hakkında bilgi isteyebilirsiniz. Gerekli resmî muayene ve belgelendirme işlemlerinin yalnızca yetkili kuruluşlarca yapılabileceğini unutmayın; bu sayfa D & E adına yetki belgesi beyanı içermez.'
   ])
  ],
  'faq':[
   ('Kalibrasyon yaptırmak yasal muayene yerine geçer mi?','Her zaman hayır. İşlemin kapsamı ve belgenin hukuki geçerliliği ayrı değerlendirilir; zorunlu muayenede güncel yetki şartlarına bakılmalıdır.'),
   ('Her sayaç aynı tarihte mi kontrol edilir?','Hayır. Model, ilk kullanım ve önceki işlem tarihi farklı olabilir. Takvim, cihaz bazında kayıtlarla ve mevzuatla doğrulanmalıdır.'),
   ('Arızalı kalorimetre mutlaka değiştirilir mi?','Her arıza doğrudan değişim gerektirmez. Onarım, test ve yenileme seçenekleri teknik uygunluğa ve geçerli kurallara göre değerlendirilir.')
  ],
  'visual':'product','image':'assets/products/U-20.png','badge':'ACCURACY / INSPECTION','visual_caption':'Kalorimetre ürün görseli — örnek cihaz',
 },
 {
  'slug':'proje-degerlendirmesi', 'title':'Kalorimetre ve Sayaç Proje Değerlendirmesi', 'short':'Proje Değerlendirmesi',
  'meta':'Kalorimetre ve sayaç projelendirmede debi, DN çapı, bağlantı, sıcaklık koşulları, M-Bus ve doğru ürün seçiminin önemli adımları.',
  'eyebrow':'03 / DOĞRU PLANLAMA', 'lead':'İyi bir ölçüm sisteminin temeli, doğru cihazı doğru noktada kullanmaktır. Tesisatın gerçek çalışma koşulları netleşmeden yapılan model seçimi uzun vadede gereksiz maliyet yaratabilir.',
  'intro_title':'Her bina farklıdır. Doğru çözüm, doğru sorularla başlar.',
  'intro':[
   'Yeni bir proje, toplu sayaç alımı veya mevcut tesisatın yenilenmesi gündemdeyse önce ihtiyaç tanımı yapılmalıdır. Binanın merkezi ısıtma yapısı, sıcak-soğuk su hatları, bağımsız bölüm sayısı ve teknik hacimlerin konumu aynı ürünün uygunluğunu değiştirebilir.',
   'Örneğin DN20 bağlantılı iki ısı sayacı aynı debi aralığına, montaj yönüne veya haberleşme özelliğine sahip olmak zorunda değildir. Doğru değerlendirme; üretici veri sayfası, kullanım amacı ve tesisat tasarım değerlerinin birlikte okunmasını gerektirir.'
  ],
  'steps':[
   ('İhtiyacı tanımlama','Hangi akışkanın, hangi bölümde, hangi amaçla ölçüleceği belirlenir.'),
   ('Teknik veri toplama','Bağlantı çapı, debi, sıcaklık, basınç ve kurulum şartları kayda alınır.'),
   ('Model karşılaştırma','Cihaz veri sayfaları ve haberleşme seçenekleri projeyle karşılaştırılır.'),
   ('Uygulama planı','Montaj konumu, erişim, bakım ve gelecekteki okuma ihtiyacı gözden geçirilir.')
  ],
  'sections':[
   ('Kalorimetre seçerken en kritik teknik parametreler',[
    'Kalorimetrede nominal bağlantı çapı (DN), kalıcı debi, minimum ölçüm debisi, izin verilen basınç kaybı, sıcaklık aralığı ve montaj yönü temel değerlendirme konularıdır. DN15, DN20, DN25 veya DN50 ibaresi tek başına doğru seçim anlamına gelmez; tesisattan geçmesi beklenen gerçek debi esas alınmalıdır.',
    'Isı sayacının sıcaklık sensörleri, ölçümün yapılacağı gidiş veya dönüş konumuna ilişkin üretici talimatları ve kullanıcının ekranı görebilmesi de önemlidir. Yanlış konumlandırılmış cihaz, teknik olarak iyi bir model olsa bile sağlıklı sonuç vermeyebilir.'
   ]),
   ('Ultrasonik ve mekanik modeller nasıl karşılaştırılır?',[
    'Ultrasonik sayaçlar, hareketli debi ölçüm mekanizması olmadan akışı değerlendirebilen tasarımlara sahiptir. Mekanik sayaçlarda ise akışla hareket eden bir ölçüm elemanı bulunabilir. Bu fark; bakım, su kalitesi, minimum debi ve basınç kaybı beklentileri açısından değerlendirmeyi etkileyebilir.',
    'Teknolojilerden birini her projede üstün ilan etmek doğru değildir. Beklenen kullanım ömrü, bütçe, yetkili uygunluk belgeleri, tedarik kolaylığı ve iletişim modülü seçenekleri karşılaştırılarak karar verilmelidir.'
   ]),
   ('Sıcak ve soğuk su sayacında neler değişir?',[
    'Suyun sıcaklığı ve kullanım yeri sayaç sınıfını belirlemede önemlidir. Sıcak su sayacı ile soğuk su sayacının gövde, ölçüm aralığı veya uygun çalışma sıcaklıkları aynı olmayabilir. Seçim sırasında sayacın ürün etiketindeki ve teknik belgesindeki limitler kontrol edilmelidir.',
    'Kalorimetreyle su sayacı birbirinin yerine kullanılmaz: su sayacı hacmi, kalorimetre ise ısı enerjisini ölçmek üzere tasarlanır. Merkezi sıcak su sistemlerinde her iki ölçüm türüne farklı amaçlarla ihtiyaç duyulabilir.'
   ]),
   ('İleride uzaktan okuma isteniyorsa ne yapılmalı?',[
    'M-Bus, pulse çıkışı veya kablosuz haberleşme seçeneklerinin projelendirme aşamasında değerlendirilmesi önemlidir. Sayaç üzerinde fiziksel bağlantı görülmesi protokolün tüm gereksinimleri karşıladığını garanti etmez. Veri formatı ve iletişim cihazlarının uyumluluğu teknik doküman üzerinden kontrol edilmelidir.',
    'Sayaç sayısı arttıkça kablo uzunluğu, ağ segmenti, güç gereksinimi ve veri erişim yetkileri tasarımın bir parçası hâline gelir. İleride bina yönetimi değişse bile sistemin anlaşılabilir ve dokümante edilmiş olması hedeflenmelidir.'
   ]),
   ('İlk görüşmeye hazırlanmak için pratik kontrol listesi',[
    'Bağımsız bölüm sayısı, ürün adedi, sayaç yerlerinin fotoğrafları, boru çapı, bilinen debi aralığı, ölçülecek sistemin türü ve varsa mimari/mekanik proje paftaları işe yarar. Eksik bilgi olduğunda tahmini ölçü verilmesi yerine belirsizliğin açıkça belirtilmesi daha doğru sonuç sağlar.',
    'D & E üzerinden cihaz seçenekleri ve proje gereksinimleri hakkında görüşme talep edebilirsiniz. Saha uygulaması veya resmî proje onayı gerektiren işler için yetkili teknik tarafların değerlendirmesi ayrıca gerekir.'
   ])
  ],
  'faq':[
   ('DN çapı büyük olursa ölçüm daha iyi mi olur?','Hayır. Gereğinden büyük cihaz, düşük debilerde uygun ölçüm aralığının dışında kalabilir. Esas olan tesisatın tasarım ve işletme debisidir.'),
   ('M-Bus özelliği sonradan eklenir mi?','Bazı ürünlerde modül seçenekleri bulunabilir; her model için geçerli değildir. Üretici model kodu ve teknik veri sayfası kontrol edilmelidir.'),
   ('Sadece ürün fotoğrafıyla teklif alınabilir mi?','Fotoğraf fikir verebilir ancak teknik varyantı doğrulamak için model etiketi, DN, debi, adet ve uygulama bilgisi gerekebilir.')
  ],
  'visual':'product','image':'assets/products/M-20.png','badge':'PLANNING / TECHNICAL FIT','visual_caption':'Kalorimetre ürün görseli — model seçimi örneği',
 },
 {
  'slug':'sayac-degisimi', 'title':'Kalorimetre ve Su Sayacı Değişimi Rehberi', 'short':'Sayaç Değişimi',
  'meta':'Kalorimetre ve su sayacı değişimi nasıl planlanır? DN bağlantısı, cihaz uyumu, söküm, montaj sonrası kontroller ve okuma kayıtları.',
  'eyebrow':'04 / SİSTEM YENİLEME', 'lead':'Sayaç değişiminde doğru cihazı seçmek kadar, eski okumaların korunması ve yeni cihazın mevcut tesisata uygun biçimde devreye alınması da önemlidir.',
  'intro_title':'Eski cihazı yenilemek, ölçüm sürekliliğini korumak demektir.',
  'intro':[
   'Arızalanmış, kullanım şartlarını karşılamayan veya muayene sonucunda değiştirilmesi gereken sayaçlarda yenileme planı hazırlanabilir. Ancak değişim işlemi yalnızca eski cihazın sökülüp yenisinin takılması olarak düşünülmemelidir. Bağlantı geometrisi, sayaç türü, montaj şartları ve veri kayıtlarının sürekliliği birlikte incelenir.',
   'Kalorimetrelerde sensör bağlantıları ve akış bölümü; su sayaçlarında sıcaklık sınıfı, ölçüm yönü ve bağlantı koşulları önem kazanır. Yeni modelin uygunluğu, eski cihazın etiketini birebir taklit etmesine değil teknik gereksinimleri karşılamasına bağlıdır.'
  ],
  'steps':[
   ('Mevcut cihaz kaydı','Seri numarası, son okuma değeri, model, bağlantı ve arıza bilgisi kaydedilir.'),
   ('Uyum analizi','Yeni ürünün debi, DN, sıcaklık ve haberleşme koşulları doğrulanır.'),
   ('Kontrollü değişim','Su ve tesisat güvenliği sağlanır; işlem uygun uzman kişilerce gerçekleştirilir.'),
   ('Devreye alma','Sızdırmazlık, çalışma, ilk okuma ve yeni sayaç kimliği kayıt altına alınır.')
  ],
  'sections':[
   ('Sayaç değişimi ne zaman gündeme gelir?',[
    'Çalışmayan ekran, devam eden hata kodları, hatalı ölçüm şüphesi, bağlantı sızıntısı veya teknik ömrün dolması yenileme değerlendirmesini gerektirebilir. Bazı durumlarda kalibrasyon ya da resmî muayene sonucu da işlem ihtiyacını ortaya çıkarabilir. Her hata kodu doğrudan cihaz değişimi anlamına gelmez.',
    'Sorunun sayaçtan mı tesisatın başka bir bölümünden mi kaynaklandığını ayırt etmek önemlidir. Özellikle hava, kirlenme, yanlış akış yönü veya sensör bağlantısı gibi faktörler ölçümü etkileyebilir; nihai teşhis üretici talimatlarıyla ve uzman incelemesiyle yapılmalıdır.'
   ]),
   ('Yeni cihaz seçiminde boyut ve debi uyumu',[
    'Mevcut sayaçla yeni ürünün nominal bağlantı çapı, montaj uzunluğu, bağlantı tipi ve debi aralığı karşılaştırılmalıdır. Aynı DN değerine sahip iki ürünün gövde uzunluğu veya bağlantı aksesuarı farklı olabilir. Tesisat tadilatı gerekmesi olasıdır ve bu iş güvenliğiyle birlikte planlanmalıdır.',
    'Bir ultrasonik modelden mekanik modele veya tersine geçiş düşünülüyorsa sadece satın alma maliyeti değil, akış direnci ve üreticinin montaj koşulları da incelenir. Sıcak su sayaçları için çalışma sıcaklığı ve uygunluk sınıfı ayrıca kontrol edilir.'
   ]),
   ('Söküm öncesi eski tüketim değerleri neden kaydedilmeli?',[
    'Cihaz sökülmeden önce son birikimli okuma, birim, tarih ve seri numarasının fotoğrafı alınması kayıt sürekliliğini destekler. Cihazın sıfırlanmış olması, daha önce değiştirilmiş olması veya okunamaması gibi durumlar da açıklamalı olarak belgelenmelidir.',
    'Yeni cihaz takıldığında ilk okuma ve seri numarası ayrı satır olarak kayıt altına alınır. Böylece iki farklı sayacın birikimli verileri yanlışlıkla tek sayaçmış gibi karşılaştırılmaz. Özellikle merkezi gider paylaşımı yapılan binalarda bu ayrım kritik olabilir.'
   ]),
   ('Montaj sonrasında hangi kontroller yapılır?',[
    'Gövde akış yönü, bağlantıların sızdırmazlığı, varsa sıcaklık sensörlerinin doğru konumu, ekranın okunabilirliği ve hata göstergeleri kontrol edilir. Uyumlu uzaktan okuma sistemi varsa yeni cihazın ağa doğru tanıtıldığı ayrıca doğrulanmalıdır.',
    'İlk çalışma koşullarındaki değerler, üretici montaj talimatlarıyla karşılaştırılır. Mühür, yetki, sigorta ve iş güvenliği gerektiren işlemlerde yürürlükteki şartlara uyulması gerekir. Yetkisiz kişilerin basınçlı veya sıcak tesisata müdahale etmesi tehlikeli olabilir.'
   ]),
   ('Değişim talebinde hangi bilgiler gerekli?',[
    'Daire veya hat sayısı, eski ürün etiketi, bağlantı noktası fotoğrafı, varsa arıza açıklaması, istenen haberleşme özelliği ve cihaz adedi ilk değerlendirmeyi kolaylaştırır. Sıcak ve soğuk su uygulamaları ayrı belirtilmelidir.',
    'D & E iletişim bölümünden yeni cihaz seçenekleri hakkında bilgi veya teklif isteyebilirsiniz. Uygulamanın sahada sunulabilirliği ve varsa yetki gereklilikleri, projenin özelliklerine göre görüşmede netleştirilir.'
   ])
  ],
  'faq':[
   ('Her kalorimetre her boruya takılır mı?','Hayır. Bağlantı çapı, gövde uzunluğu, debi ve üretici montaj şartları uyumlu olmalıdır.'),
   ('Sayaç değiştiğinde eski tüketim bilgileri silinir mi?','Eski cihaz verisi yeni cihazda otomatik oluşmaz. Son ve ilk okumaların ayrı kayıt altına alınması bu nedenle önemlidir.'),
   ('Değişim sırasında tesisat kapatılır mı?','Uygulama koşullarına göre ilgili hattın güvenli biçimde izole edilmesi gerekebilir. İşlem planını yetkili uygulayıcı yapmalıdır.')
  ],
  'visual':'product','image':'assets/products/SJD-20-SH.png','badge':'RENEWAL / DEVICE LIFECYCLE','visual_caption':'Su sayacı ürün görseli — örnek model',
 },
 {
  'slug':'uzaktan-okuma-otomasyon', 'title':'Uzaktan Sayaç Okuma ve Otomasyon Sistemleri', 'short':'Uzaktan Okuma ve Otomasyon',
  'meta':'M-Bus ve kablosuz sayaç okuma sistemleri nasıl çalışır? Kalorimetre otomasyonu, veri toplama, uyum, raporlama ve sistem güvenliği rehberi.',
  'eyebrow':'05 / BAĞLANTI & VERİ', 'lead':'Kalorimetre ve su sayaçlarından gelen ölçüm bilgilerinin tek merkezde görüntülenmesi, doğru altyapı ve uyumlu cihazlarla mümkün hâle gelir.',
  'intro_title':'Tek ekranda görünen her değer, doğru kurulmuş bir sistemin sonucudur.',
  'intro':[
   'Uzaktan sayaç okuma otomasyonu, sayaçların desteklediği iletişim arabirimi üzerinden veri toplama, saklama ve görüntüleme süreçlerini kapsar. Amaç yalnızca fiziksel okuma ihtiyacını azaltmak değil; düzenli veri toplama, geçmiş dönem karşılaştırması ve hata takibini sistemli hâle getirmektir.',
   'M-Bus destekli kalorimetreler, kablolu hat üzerinden veri toplama ünitelerine bağlanabilir. Farklı projelerde kablosuz çözümler, pulse çıkışları veya marka özel ağlar kullanılabilir. Her cihazın aynı protokolü desteklediği varsayılmamalıdır; uygunluk teknik etiket ve üretici belgesiyle doğrulanır.'
  ],
  'steps':[
   ('Altyapı envanteri','Sayaç adetleri, protokolleri, seri numaraları ve kurulum konumları belirlenir.'),
   ('Ağ planlaması','Kablo uzunluğu, güç ihtiyacı, dönüştürücüler ve veri merkezi tasarlanır.'),
   ('Veri eşleme','Sayaç adresleri daire ve ölçüm türüyle eşleştirilerek örnek okumalar doğrulanır.'),
   ('İzleme & bakım','Kayıp okuma, hata kodu ve yetkisiz erişim riskleri için takip düzeni oluşturulur.')
  ],
  'sections':[
   ('M-Bus sistemi nasıl çalışır?',[
    'M-Bus (Meter-Bus), uygun sayaçların ölçüm verilerini merkezi bir okuyucuya iletmek için kullanılan haberleşme yaklaşımlarından biridir. Bir ana birim ile sayaçlar arasında kurulan hattın bağlantısı, beslemesi ve kapasitesi seçilen donanıma göre planlanır. Cihazın M-Bus desteklemesi, tek başına her okuma yazılımıyla doğrudan çalışacağı anlamına gelmez.',
    'Bazı sayaçlar yalnızca belirli veri alanlarını paylaşır, bazıları farklı adresleme veya modül seçenekleri gerektirir. Test aşamasında enerji değeri, ölçüm birimi, sayaç seri numarası ve zaman bilgisi gibi alanlar kontrol edilerek doğru kaynağın okunduğundan emin olunur.'
   ]),
   ('Kablolu ve kablosuz sistemler nasıl karşılaştırılır?',[
    'Kablolu kurulumda fiziksel hat planı, koruma ve kablolama güzergâhı ön plana çıkar. Yeni inşaatlarda ilk projelendirme aşamasında kablo kanallarının düşünülmesi avantaj sağlayabilir. Mevcut binalarda ise kabloya erişim sınırlı olduğunda farklı seçenekler gerekebilir.',
    'Kablosuz çözümler, kapsama alanı, cihazların bulunduğu teknik şaftlar, pil ömrü ve parazit koşullarından etkilenebilir. Binaya göre her iki çözümün avantajı da değişir. Hangi teknoloji seçilirse seçilsin cihaz ve ağ üreticilerinin teknik sınırlamaları dikkate alınmalıdır.'
   ]),
   ('Merkezi panelde neler takip edilebilir?',[
    'Uygun cihaz ve yazılım kombinasyonunda birikimli tüketim değerleri, tarihsel karşılaştırma, okuma başarısı, iletişim hataları ve cihaz bazlı durum kayıtları görüntülenebilir. Gösterilebilecek veri türleri protokol ve sayaç modeline göre değişir; tüm ölçüm alanları her sistemde bulunmaz.',
    'Veri panellerinin anlaşılır olması, sayıların güvenilir olmasından ayrı bir tasarım gerektirir. Daire/sayaç eşleştirmesinin doğru yapılması, birimlerin açık yazılması ve veri kesintilerinin görünür olması raporu kullanan kişilerin yanlış yorum yapmasını önler.'
   ]),
   ('Sistem güvenliği ve kişisel veriler',[
    'Okuma verileri daire ya da kullanıcıyla ilişkilendirilebildiğinde erişim yetkileri önemli hâle gelir. Kimlerin hangi sayaçları görebileceği, verinin ne kadar süre saklanacağı ve paylaşımın hangi amaçla yapılacağı sistem sahibi tarafından netleştirilmelidir.',
    'İletişim ağında yetkisiz erişim, yanlış cihaz eşlemesi, yedekleme eksikliği ve bağlantı kopmaları iş sürekliliğini etkileyebilir. Uygun ağ tasarımı, güncel güvenlik kontrolleri ve periyodik gözden geçirme, veri kalitesini destekleyen teknik başlıklardır.'
   ]),
   ('Otomasyon projesi için hazırlık ve seçenekler',[
    'Sayaç sayısı, cihazların marka-modeli, haberleşme arabirimi, bina blok sayısı, şaftların konumu ve mevcut kablolama bilgileri ilk plan için yararlıdır. Binada daha önce kurulmuş bir otomasyon varsa kullanılan cihazların model kodları da paylaşılmalıdır.',
    'D & E ile iletişime geçerek proje ihtiyaçlarını ve uygun sistem yaklaşımlarını değerlendirebilirsiniz. Bu içerik herhangi bir çevrimiçi okuma panelinin hâlihazırda sunulduğunu veya belirli bir otomasyon hizmetinin garanti edildiğini ileri sürmez.'
   ])
  ],
  'faq':[
   ('M-Bus ile her marka sayaç okunur mu?','Hayır. Protokol, model sürümü, modül ve veri alanları uyumluluğu kontrol edilmelidir.'),
   ('İnternet kesilirse veriler kaybolur mu?','Bu durum kurulan otomasyonun yerel kayıt ve yedekleme mimarisine bağlıdır. Her sistem için aynı davranış beklenmemelidir.'),
   ('Otomasyon gider paylaşımını otomatik olarak yasal hâle getirir mi?','Hayır. Teknik veri toplama ile mevzuata uygun paylaşımın hazırlanması farklı süreçlerdir ve ayrı yükümlülükler içerebilir.')
  ],
  'visual':'dashboard','badge':'CONNECTIVITY / M-BUS SYSTEMS','visual_caption':'Merkezi takip paneli — temsili görselleştirme',
 }
]


def esc(value):
    return escape(str(value), quote=True)


def render(service, index):
    slug=service['slug']
    url=f'{ORIGIN}/hizmetler/{slug}/'
    title=esc(service['title'])
    desc=esc(service['meta'])
    others=''.join('<a href="../'+esc(s['slug'])+'/index.html" '+('aria-current="page" ' if s is service else '')+'><span>'+esc(s['short'])+'</span><b aria-hidden="true">↗</b></a>' for s in SERVICES)
    breadcrumbs={
     '@type':'BreadcrumbList','itemListElement':[
      {'@type':'ListItem','position':1,'name':'Ana Sayfa','item':ORIGIN+'/'},
      {'@type':'ListItem','position':2,'name':'Hizmetlerimiz','item':ORIGIN+'/#services-nav'},
      {'@type':'ListItem','position':3,'name':service['short'],'item':url},
     ]
    }
    ld={'@context':'https://schema.org','@graph':[
        {'@type':'Article','headline':service['title'],'description':service['meta'],'inLanguage':'tr-TR',
         'mainEntityOfPage':url,'author':{'@type':'Organization','name':'D & E | Kalorimetre Teknolojileri'},
         'publisher':{'@type':'Organization','name':'D & E | Kalorimetre Teknolojileri','url':ORIGIN},
         'image':ORIGIN+'/assets/industrial-night.jpg'},
        breadcrumbs]}
    schema=json.dumps(ld,ensure_ascii=False).replace('<','\\u003c')
    navitems=''.join('<a href="../'+esc(s['slug'])+'/index.html"'+(' aria-current="page"' if s is service else '')+'>'+esc(s['short'])+'</a>' for s in SERVICES)
    if service['visual']=='dashboard':
        labels=['ISITMA / ENERJİ','SICAK SU / HACİM','OKUMA KONTROLÜ','İLETİŞİM DURUMU']
        widths=[82,63,92,75]
        bars=''.join(f'<div class="sp-dash-row"><span>{esc(label)}</span><span class="sp-dash-bar bar-{w}"><i></i></span></div>' for label,w in zip(labels,widths))
        visual=f'''<div class="sp-dashboard" aria-label="Temsili sayaç verisi görselleştirmesi"><div class="sp-dashboard-top"><span>DATA / OVERVIEW</span><span class="sp-pulse">●&nbsp; ÖRNEK PANEL</span></div><div class="sp-dashboard-monogram">D <em>&amp;</em> E</div><div class="sp-dashboard-heading">Ölçüm verilerine<br><em>yeni bir bakış.</em></div><div class="sp-dash-rows">{bars}</div><div class="sp-dashboard-bottom"><span>PRECISION INSIGHT</span><span>↗ &nbsp; 2026</span></div></div>'''
    else:
        visual=f'''<div class="sp-product-visual"><span class="sp-product-top">D &amp; E &nbsp; / &nbsp; TECHNICAL SELECTION</span><img src="../../{esc(service['image'])}" alt="{esc(service['visual_caption'])}" loading="lazy" width="540" height="480"><span class="sp-product-bottom">REAL PRODUCT / VISUAL REFERENCE &nbsp; ↗</span></div>'''
    step_html=''.join(f'<li><div class="sp-step-count">0{i}</div><h3>{esc(name)}</h3><p>{esc(text)}</p></li>' for i,(name,text) in enumerate(service['steps'],1))
    sections=''.join('<section class="sp-reading-section" id="bolum-'+str(i)+'"><div class="sp-section-label">'+f'0{i+1} / DETAYLI BİLGİ'+'</div><h2>'+esc(name)+'</h2>'+''.join('<p>'+esc(p)+'</p>' for p in paras)+'</section>' for i,(name,paras) in enumerate(service['sections'],1))
    faq=''.join('<details><summary>'+esc(question)+'<span aria-hidden="true">+</span></summary><p>'+esc(answer)+'</p></details>' for question,answer in service['faq'])
    related=''.join('<a href="../'+esc(s['slug'])+'/index.html"><small>0'+str(i)+' / SERVICE NOTE</small><strong>'+esc(s['short'])+'</strong><span aria-hidden="true">↗</span></a>' for i,s in enumerate(SERVICES,1) if s is not service)
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#090f10">
<meta name="referrer" content="no-referrer">
<title>{title} | D &amp; E</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="D &amp; E Kalorimetre Teknolojileri">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ORIGIN}/assets/industrial-night.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{schema}</script>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Playfair+Display:ital,wght@0,400;0,500;1,400&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/service-pages.css">
</head>
<body>
<div class="sp-ribbon"><span>D &amp; E &nbsp; / &nbsp; ENERGY TECHNOLOGIES</span><span>HASSAS ÖLÇÜM &nbsp; · &nbsp; ZAMANSIZ YAKLAŞIM</span></div>
<header class="sp-header"><div class="sp-shell sp-header-inner"><a href="../../index.html" class="sp-logo" aria-label="D ve E ana sayfa"><strong>D <em>&amp;</em> E<span>.</span></strong><small>KALORİMETRE TEKNOLOJİLERİ</small></a><nav aria-label="Üst menü"><a class="sp-desktop-only" href="../../index.html#koleksiyon">KOLEKSİYON</a><details class="sp-nav-details"><summary>HİZMETLERİMİZ <span aria-hidden="true">⌄</span></summary><div class="sp-nav-dropdown">{navitems}</div></details><a class="sp-contact-nav" href="../../index.html#iletisim">İLETİŞİM &nbsp; ↗</a></nav></div></header>
<main>
<section class="sp-hero"><div class="sp-shell"><div class="sp-breadcrumb"><a href="../../index.html">ANA SAYFA</a><span>/</span><span>HİZMETLERİMİZ</span><span>/</span><span class="sp-breadcrumb-active">{esc(service['short'])}</span></div><div class="sp-hero-main"><div><div class="sp-kicker"><span class="sp-spark">✦</span> &nbsp; {esc(service['eyebrow'])}</div><h1>{title}</h1><p>{esc(service['lead'])}</p><a class="sp-text-link" href="#detaylar">DETAYLI İNCELEYİN <span aria-hidden="true">↓</span></a></div><div class="sp-hero-number" aria-hidden="true">0{index}</div></div><div class="sp-hero-footer"><span>{esc(service['badge'])}</span><span>TECHNICAL EDITION &nbsp; / &nbsp; D &amp; E</span></div></div></section>
<section class="sp-overview sp-shell" aria-labelledby="intro-heading"><div class="sp-overview-copy"><div class="sp-overline">BAKIŞ AÇIMIZ &nbsp; / &nbsp; 0{index}</div><h2 id="intro-heading">{esc(service['intro_title'])}</h2>{''.join('<p>'+esc(p)+'</p>' for p in service['intro'])}<div class="sp-inline-rule"><span>İHTİYACA GÖRE PLANLAMA</span><span aria-hidden="true">↗</span></div></div><figure class="sp-figure">{visual}<figcaption>{esc(service['visual_caption'])}</figcaption></figure></section>
<section class="sp-process" id="surec"><div class="sp-shell"><div class="sp-overline">D &amp; E / YAKLAŞIM</div><div class="sp-section-head"><h2>Süreç nasıl <em>ilerler?</em></h2><p>Her uygulama kendi teknik koşullarına göre değerlendirilir. Genel bir planlama akışı şu adımlardan oluşur.</p></div><ol class="sp-steps">{step_html}</ol></div></section>
<section class="sp-deep sp-shell" id="detaylar"><div class="sp-article">{sections}</div><aside class="sp-sidebar"><div class="sp-sidepanel"><span class="sp-overline">HİZMET DOSYASI</span><div class="sp-side-title">0{index} <span>/ 05</span></div><p>Bu konuda daha fazla bilgiye ihtiyacınız varsa diğer teknik sayfaları inceleyebilirsiniz.</p><nav aria-label="Diğer hizmet sayfaları">{others}</nav></div><div class="sp-sidecontact"><span>✳</span><h3>Projenizin detaylarını paylaşın.</h3><p>İhtiyacınıza uygun ürün ve mümkün olan seçenekleri iletişim üzerinden görüşelim.</p><a href="../../index.html#iletisim">BİZE ULAŞIN &nbsp; ↗</a></div></aside></section>
<section class="sp-faq-band"><div class="sp-shell sp-faq-layout"><div><div class="sp-overline">BİLMENİZ GEREKENLER</div><h2>Sıkça sorulan<br><em>sorular.</em></h2><p>Bu hizmet alanıyla ilgili en çok merak edilen teknik noktalar.</p></div><div class="sp-faq-items">{faq}</div></div></section>
<section class="sp-next sp-shell"><div class="sp-overline">DAHA FAZLASINI KEŞFEDİN</div><h2>Bir sonraki <em>adım.</em></h2><div class="sp-next-links">{related}</div></section>
<section class="sp-closing"><div class="sp-shell sp-closing-inner"><div><span class="sp-overline">D &amp; E / İLETİŞİM</span><h2>İyi bir sistem,<br><em>doğru bir konuşmayla</em> başlar.</h2><p>Projenizin kapsamını, mevcut sayaçları veya ürün ihtiyacınızı anlatın. İletişim sayfamız üzerinden bize ulaşabilirsiniz.</p></div><a href="../../index.html#iletisim">PROJENİZİ KONUŞALIM <span aria-hidden="true">↗</span></a></div></section>
<div class="sp-legal sp-shell">Bu sayfa genel teknik bilgilendirme sunar. Gerçek uygulama, hizmet kapsamı, resmî yetki ve mevzuat koşulları ilgili proje için ayrıca doğrulanmalıdır.</div>
</main>
<footer class="sp-footer"><div class="sp-shell sp-footer-inner"><a class="sp-footer-logo" href="../../index.html">D <em>&amp;</em> E<span>.</span></a><p>© 2026 KALORİMETRE TEKNOLOJİLERİ &nbsp; · &nbsp; HASSAS ÖLÇÜM, SEÇKİN YAKLAŞIM</p><a href="../../index.html">ANA SAYFAYA DÖN ↑</a></div></footer>
</body>
</html>'''


def main():
    for i,service in enumerate(SERVICES,1):
        folder=ROOT/'hizmetler'/service['slug']
        folder.mkdir(parents=True, exist_ok=True)
        (folder/'index.html').write_text(render(service,i),encoding='utf-8')
    print('Generated',len(SERVICES),'original D & E service pages')

if __name__=='__main__': main()
