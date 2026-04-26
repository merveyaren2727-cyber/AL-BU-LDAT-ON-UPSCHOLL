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

# BridgeAI MVP Görev Listesi (Adım Adım)

Bu liste, PRD v1.0 hedeflerine göre uygulamayı uçtan uca geliştirmek için sıralı görev planıdır.

## 0) Proje Kurulumu ve Altyapı
- [ ] **T0.1 - Repo ve ortam kurulumu**
  - Python 3.x sanal ortamı oluştur (`venv`)
  - Temel bağımlılıkları ekle: `streamlit`, `openai`, `fpdf2`, `python-dotenv`, `pillow`
  - Başlangıç dosya yapısını oluştur: `app.py`, `services/`, `ui/`, `utils/`, `outputs/`
  - **Kabul Kriteri:** `streamlit run app.py` ile boş ana ekran açılıyor.

- [ ] **T0.2 - Konfigürasyon ve gizli anahtar yönetimi**
  - `.env.example` oluştur (`OPENAI_API_KEY=`)
  - `.gitignore` içine `.env`, `outputs/*.pdf` ekle
  - Uygulama başlangıcında API key kontrolü yap
  - **Kabul Kriteri:** API key yoksa kullanıcı dostu uyarı gösteriliyor.

---

## 1) Giriş Katmanı (Input)
- [ ] **T1.1 - Karşılama ekranı (minimalist)**
  - Basit başlık, kısa açıklama, "başla" akışı
  - PRD’deki slogan/ürün vaadini kısa metinle göster
  - **Kabul Kriteri:** Kullanıcı ana akışı tek ekrandan başlatabiliyor.

- [ ] **T1.2 - Çoklu görsel girişi**
  - Galeriden yükleme (`file_uploader`, çoklu dosya)
  - Kamera ile anlık çekim (`camera_input`)
  - Desteklenen format validasyonu (`jpg`, `jpeg`, `png`, `webp`)
  - **Kabul Kriteri:** Kullanıcı en az 1 görsel seçip bir sonraki adıma geçebiliyor.

- [ ] **T1.3 - Profil seçimi (Öğrenci / Mavi Yaka)**
  - İki modlu seçim bileşeni
  - Her mod için kısa açıklama ve örnek çıktı tipi göster
  - **Kabul Kriteri:** Seçilen profil session state içinde saklanıyor.

---

## 2) İşleme Katmanı (AI Engine)
- [ ] **T2.1 - OCR + görselden metin çıkarımı servisi**
  - `services/vision_service.py` oluştur
  - GPT-4o Vision çağrısı ile ham metin çıkar
  - Hata/timeout yönetimi ekle
  - **Kabul Kriteri:** Örnek görselden okunabilir ham metin dönüyor.

- [ ] **T2.2 - Adaptasyon (profile göre dönüştürme)**
  - `services/adaptation_service.py` oluştur
  - Öğrenci modu:
    - 11. sınıf seviyesinde özet üret
    - 5 soruluk deneme sınavı üret
  - Mavi yaka modu:
    - Adım adım talimat listesi üret
    - Kritik güvenlik uyarılarını ayrı bölümde ver
  - **Kabul Kriteri:** Aynı girdi, profile göre farklı ve uygun formatta çıktı üretiyor.

- [ ] **T2.3 - Prompt kalite ve doğruluk iyileştirmesi**
  - Kritik terim/sayı kaybını azaltan prompt kuralları ekle
  - "Bilinmiyorsa tahmin etme" kuralı ekle
  - Çıktıda belirsiz alanlar için işaretleme formatı tanımla
  - **Kabul Kriteri:** Test örneklerinde kritik sayı/terim doğruluğu artıyor.

---

## 3) Çıktı Katmanı (Output)
- [ ] **T3.1 - Anlık önizleme ekranı**
  - Oluşan metni düzenli bloklar halinde göster
  - Moda göre başlıklandırma (Özet, Sorular / Adımlar, Güvenlik)
  - **Kabul Kriteri:** PDF üretmeden önce tüm içerik ekranda okunabiliyor.

- [ ] **T3.2 - PDF üretim servisi**
  - `services/pdf_service.py` oluştur
  - FPDF ile profesyonel mizanpaj: başlık, alt başlık, paragraf/listeler
  - Tarih, profil bilgisi ve dosya adı standardı ekle
  - **Kabul Kriteri:** Önizleme ile tutarlı PDF başarıyla oluşturuluyor.

- [ ] **T3.3 - İndirme butonu**
  - `st.download_button` ile tek tık indirme
  - Dosya adı formatı: `BridgeAI_<profil>_<timestamp>.pdf`
  - **Kabul Kriteri:** Kullanıcı tek tıkla PDF’i indirebiliyor.

---

## 4) Kullanıcı Akışı ve UX (PRD User Flow)
- [ ] **T4.1 - Adım bazlı akış yönetimi**
  - 5 adımı tek sayfada state tabanlı ilerlet
  - Geri dönme/düzenleme desteği ekle
  - **Kabul Kriteri:** Kullanıcı akış içinde kaybolmadan ilerleyebiliyor.

- [ ] **T4.2 - İşlem sırasında bekleme deneyimi**
  - "BridgeAI veriyi dönüştürüyor..." metni + spinner/progress
  - Uzun işlemlerde kullanıcıya durum bilgisi ver
  - **Kabul Kriteri:** İşlem sırasında ekran donmuş hissi oluşmuyor.

- [ ] **T4.3 - Hata mesajları ve boş durumlar**
  - Görsel yok, profil seçilmedi, API hatası, PDF hatası senaryoları
  - Teknik detay göstermeyen anlaşılır mesajlar
  - **Kabul Kriteri:** Kritik hata durumlarında kullanıcı bir sonraki aksiyonu anlıyor.

---

## 5) Performans ve Kalite (Başarı Kriterleri)
- [ ] **T5.1 - Performans ölçümü**
  - Giriş -> PDF toplam süresini logla
  - Hedef: 15 saniye altı (ortalama test seti)
  - **Kabul Kriteri:** En az 10 test çalıştırmasında ortalama süre hedefe yakın.

- [ ] **T5.2 - Doğruluk kontrol checklist’i**
  - Kritik terim/sayı doğrulama için manuel kontrol şablonu oluştur
  - Öğrenci ve mavi yaka için ayrı örnek veri seti belirle
  - **Kabul Kriteri:** Kritik veri yakalama oranı PRD hedefine yaklaşır (> %95 hedef).

- [ ] **T5.3 - Basit testler**
  - Servis bazlı smoke testler (vision/adaptation/pdf)
  - Boş girdi, tek görsel, çoklu görsel senaryoları
  - **Kabul Kriteri:** Temel senaryolarda regresyon yakalanıyor.

---

## 6) Yayına Hazırlık (MVP)
- [ ] **T6.1 - README ve kullanım kılavuzu**
  - Kurulum, `.env`, çalıştırma, örnek kullanım
  - Bilinen kısıtlar ve sonraki adımlar
  - **Kabul Kriteri:** Yeni geliştirici 10 dakikada projeyi ayağa kaldırabiliyor.

- [ ] **T6.2 - Demo scripti**
  - 2 demo senaryosu hazırla:
    - Öğrenci: ders notu görseli -> özet + 5 soru
    - Mavi yaka: talimat görseli -> adımlar + güvenlik
  - **Kabul Kriteri:** Uçtan uca demo kesintisiz çalışıyor.

---

## Önerilen Sprint Sıralaması
- **Sprint 1:** T0 + T1 + T2.1
- **Sprint 2:** T2.2 + T3 + T4
- **Sprint 3:** T2.3 + T5 + T6

## MVP Tamamlanma Tanımı (Definition of Done)
- [ ] Kullanıcı görsel yükleyip profil seçerek çıktı alabiliyor.
- [ ] Çıktı önce önizleniyor, sonra tek tıkla PDF indiriliyor.
- [ ] Ortalama işlem süresi hedefe uygun.
- [ ] Temel hata senaryolarında kullanıcı yönlendiriliyor.
- [ ] Demo senaryoları canlı olarak sorunsuz çalışıyor.

# 🌉 BridgeAI: Teknoloji Yığını (Tech Stack)

Bu döküman, BridgeAI projesinde kullanılan teknolojileri, seçim nedenlerini ve bu teknolojilerin projedeki rollerini açıklar. Başlangıç seviyesindeki bir geliştirici için en yüksek hız ve basitlik dengesi gözetilmiştir.

---

## 🛠 Temel Teknolojiler

### 1. Yazılım Dili: **Python 3.x**
* **Rolü:** Projenin ana omurgası. Tüm kütüphaneleri birbirine bağlayan dildir.
* **Neden:** Başlangıç seviyesi için en kolay sözdizimine sahip olması ve yapay zeka ekosistemindeki tartışmasız liderliği.

### 2. Arayüz (UI/Frontend): **Streamlit**
* **Rolü:** Kullanıcının fotoğraf yüklediği ve sonuçları gördüğü web arayüzü.
* **Neden:** * HTML, CSS veya JavaScript bilmenize gerek kalmaz.
    * Sadece Python kullanarak "Dosya Yükle", "Seçim Kutusu" ve "Buton" gibi profesyonel görünümlü bileşenler oluşturmanızı sağlar.

### 3. Yapay Zeka Motoru: **Google Gemini 1.5 Flash**
* **Rolü:** Görsel Analiz (OCR), Metin Sadeleştirme ve Profil Adaptasyonu.
* **Neden:** * **Hız:** "Flash" modeli anlık tepki verir.
    * **Vision Kapasitesi:** Hem fotoğrafı okur hem de içeriği 11. sınıf seviyesine veya saha operatörü diline tek bir hamlede çevirir.
    * **Maliyet:** Google AI Studio üzerinden başlangıç için geniş bir ücretsiz kota sunar.

### 4. PDF Üretimi: **FPDF2**
* **Rolü:** AI tarafından oluşturulan metinleri markalı, indirilebilir bir PDF dökümanına dönüştürmek.
* **Neden:** Çok hafif bir kütüphanedir ve Türkçe karakter desteği (UTF-8) kolayca ayarlanabilir.

### 5. Görsel İşleme: **Pillow (PIL)**
* **Rolü:** Fotoğrafların boyutlandırılması ve AI'a gönderilmeden önceki hazırlık süreci.

---

## 🏗 Mimari Akış (Nasıl Çalışıyor?)

1. **Girdi:** `Streamlit` üzerinden fotoğraf ve profil (Öğrenci/Mavi Yaka) seçilir.
2. **İşleme:** Fotoğraf ve özel talimatlar (Prompt) `google-generativeai` kütüphanesi ile Gemini'ye gönderilir.
3. **Zeka:** Gemini görseli analiz eder ve bağlamı düzenler.
4. **Çıktı:** Gelen metin `FPDF2` ile şablona yerleştirilir ve kullanıcıya sunulur.

# 🌉 BridgeAI: Teknoloji Yığını (Tech Stack)

Bu döküman, BridgeAI projesinde kullanılan teknolojileri, seçim nedenlerini ve bu teknolojilerin projedeki rollerini açıklar. Başlangıç seviyesindeki bir geliştirici için en yüksek hız ve basitlik dengesi gözetilmiştir.

---

## 🛠 Temel Teknolojiler

### 1. Yazılım Dili: **Python 3.x**
* **Rolü:** Projenin ana omurgası. Tüm kütüphaneleri birbirine bağlayan dildir.
* **Neden:** Başlangıç seviyesi için en kolay sözdizimine sahip olması ve yapay zeka ekosistemindeki tartışmasız liderliği.

### 2. Arayüz (UI/Frontend): **Streamlit**
* **Rolü:** Kullanıcının fotoğraf yüklediği ve sonuçları gördüğü web arayüzü.
* **Neden:** * HTML, CSS veya JavaScript bilmenize gerek kalmaz.
    * Sadece Python kullanarak "Dosya Yükle", "Seçim Kutusu" ve "Buton" gibi profesyonel görünümlü bileşenler oluşturmanızı sağlar.

### 3. Yapay Zeka Motoru: **Google Gemini 1.5 Flash**
* **Rolü:** Görsel Analiz (OCR), Metin Sadeleştirme ve Profil Adaptasyonu.
* **Neden:** * **Hız:** "Flash" modeli anlık tepki verir.
    * **Vision Kapasitesi:** Hem fotoğrafı okur hem de içeriği 11. sınıf seviyesine veya saha operatörü diline tek bir hamlede çevirir.
    * **Maliyet:** Google AI Studio üzerinden başlangıç için geniş bir ücretsiz kota sunar.

### 4. PDF Üretimi: **FPDF2**
* **Rolü:** AI tarafından oluşturulan metinleri markalı, indirilebilir bir PDF dökümanına dönüştürmek.
* **Neden:** Çok hafif bir kütüphanedir ve Türkçe karakter desteği (UTF-8) kolayca ayarlanabilir.

### 5. Görsel İşleme: **Pillow (PIL)**
* **Rolü:** Fotoğrafların boyutlandırılması ve AI'a gönderilmeden önceki hazırlık süreci.

---

## 🏗 Mimari Akış (Nasıl Çalışıyor?)

1. **Girdi:** `Streamlit` üzerinden fotoğraf ve profil (Öğrenci/Mavi Yaka) seçilir.
2. **İşleme:** Fotoğraf ve özel talimatlar (Prompt) `google-generativeai` kütüphanesi ile Gemini'ye gönderilir.
3. **Zeka:** Gemini görseli analiz eder ve bağlamı düzenler.
4. **Çıktı:** Gelen metin `FPDF2` ile şablona yerleştirilir ve kullanıcıya sunulur.

---

## 📦 Kurulum Komutları

```bash
pip install streamlit google-generativeai fpdf2 pillow
```

---
*Bu teknoloji seçimi, 14 Mayıs hedefi için "Minimum Kod, Maksimum Sonuç" prensibiyle yapılmıştır.*
---

## 📦 Kurulum Komutları

```bash
pip install streamlit google-generativeai fpdf2 pillow
```

---
*Bu teknoloji seçimi, 14 Mayıs hedefi için "Minimum Kod, Maksimum Sonuç" prensibiyle yapılmıştır.*

---
*Bu döküman BridgeAI projesinin geliştirme anayasasıdır.*
