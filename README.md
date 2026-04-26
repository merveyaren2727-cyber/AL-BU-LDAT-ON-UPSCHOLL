# 🌉 BridgeAI: Akıllı Veri Adaptörü (PRD)

**Slogan:** "Düşük Kaliteli Girdi, Yüksek Kaliteli Çıktı."  
**Proje Sahibi:** Merve Yılmaz Çiftçi  
**Hedef Tarih:** 14 Mayıs  

---

## 📝 1. Problem: Ne Çözüyorum?
Günümüzde temel sorun bilgi eksikliği değil; bilginin fiziksel dökümanlarda (eski kitaplar, fotokopiler, teknik kılavuzlar) hapsolmuş, "gürültülü" ve karmaşık olmasıdır. BridgeAI, bu atıl bilgiyi kullanıcı için saniyeler içinde erişilebilir ve aksiyona dönüştürülebilir hale getirerek **bilgi kirliliğini ve zaman kaybını** ortadan kaldırır.

## 👥 2. Kullanıcı: Bu Uygulamayı Kim Kullanacak?
Uygulama iki ana dikeyde çözüm sunar:
- **Öğrenciler:** Elindeki kısıtlı veya karmaşık basılı materyalleri kendi seviyesine uygun çalışma kağıtlarına dönüştürmek isteyenler.
- **Mavi Yaka Personel:** Fabrika sahasındaki ağır teknik dili, hızlıca uygulanabilir basit talimatlara ve İSG kontrol listelerine dönüştürmek isteyen teknisyenler ve operatörler.

## 🤖 3. AI'ın Rolü: Yapay Zeka Ne Yapıyor?
Yapay zeka bu sistemde bir **"Bilgi Tercümanı"** olarak konumlanır:
1. **Görsel Analiz (OCR):** Fotoğrafı çekilen düşük kaliteli metinleri dijital veriye çevirir.
2. **Bağlam Duyarlı Adaptasyon:** Veriyi kopyalamak yerine, seçilen profile (Örn: 11. sınıf öğrencisi veya saha operatörü) göre dili ve yapıyı yeniden kurgular.
3. **Yaratıcı Üretim:** Ham veriden tamamen özgün testler, özetler veya teknik rehberler üretir.

## ⚔️ 4. Rakip Durum ve BridgeAI Farkı
Genel AI araçları (ChatGPT vb.) hazır veri tabanlarına veya dijital metinlere odaklanırken;
- **Farkımız:** BridgeAI, kullanıcının elindeki **"her türlü fiziksel ve kirli girdiyi"** (eski bir kitap sayfası, tozlu bir pano talimatı) işleyebilen hibrit bir yapı sunar. 
- **Telif ve Pedagoji:** İçeriği doğrudan kopyalamak yerine pedagojik veya teknik bir süzgeçten geçirerek yeniden ürettiği için rakiplerinden daha güvenli ve odaklıdır.

## 🛠 5. Uygulama Mimarisi (Mevcut Akış)
- **Girdi:** Fotoğraf yükleme + Profil seçimi (Öğrenci/Mavi Yaka).
- **Motor:** OpenAI GPT-4o Vision (Görsel ve anlamsal analiz).
- **Çıktı:** Profesyonel PDF dışa aktarımı (FPDF).

## 🏆 6. Başarı Kriteri: Ne Değişecek?
Proje başarılı olduğunda;
- En ücra köydeki bir öğrenci, elindeki tek bir kağıttan dünya standartlarında bir quiz üretebilecek.
- Fabrikalarda "usta bağımlılığı" azalacak; teknik bilgi, sahadaki en genç işçinin bile anlayabileceği bir rehbere dönüşecek.
- **14 Mayıs Hedefi:** "Fotoğraftan PDF Çıktısına" giden tam otomasyonun çalışır halde sunulması.

---
*Bu döküman BridgeAI projesinin geliştirme anayasasıdır.*
