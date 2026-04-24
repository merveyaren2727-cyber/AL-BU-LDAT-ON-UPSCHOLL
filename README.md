[idea.md](https://github.com/user-attachments/files/27064023/idea.md)
# AL-BU-LDAT-ON-UPSCHOLL
# 🌉 BridgeAI: From Page to Practice (Sayfadan Pratiğe)

> **Slogan:** "Karmaşık Veriyi Bilgiye, Bilgiyi Eyleme Dönüştüren Köprü"

## 📝 1. Problem Tanımı
Günümüzde temel sorun bilgi eksikliği değil, bilginin ulaşılamaz, pasif ve karmaşık olmasıdır.

* **Eğitimde:** Öğretmenler, kısıtlı kaynakları (eski kitaplar, fotokopiler) sınıfın dil seviyesine uyarlamak ve sınav materyali üretmek için büyük zaman kaybediyor.
* **Sanayide:** Teknik personel; ağır teknik dille yazılmış kılavuzlar, karmaşık İSG yönetmelikleri veya emekli olan "efsane ustaların" yazıya dökülmemiş tecrübeleri arasında boğuluyor.

## 👥 2. Hedef Kullanıcı Kitlesi
* **Eğitim Kanadı:** Kısıtlı bütçeli devlet okullarında çalışan, zamanı kısıtlı ve materyal çeşitliliğine ihtiyaç duyan öğretmenler.
* **Endüstri Kanadı:** Fabrika sahasındaki bakım teknisyenleri, İSG uzmanları ve kurumsal hafızayı korumak isteyen üretim yöneticileri.

## 🤖 3. Yapay Zekanın Rolü
AI, sistemde bir **"Bilgi Tercümanı"** ve **"İçerik Tasarımcısı"** olarak konumlanır:

1.  **Görsel Analiz (OCR):** Fotoğrafı çekilen her türlü fiziksel dökümanı dijital veriye çevirir.
2.  **Akıllı Filtreleme:** Veriyi kullanıcının profiline göre (A2 seviye öğrenci veya sahada çalışan operatör) yeniden yapılandırır.
3.  **Yaratıcı Yeniden Üretim:** Bilgiyi kopyalamak yerine; o bilgiden tamamen özgün sınavlar, çalışma kağıtları veya adım adım teknik rehberler üretir.

## ⚔️ 4. Rekabet Analizi ve BridgeAI Farkı
* **Rakipler:** MagicSchool (Eğitim), SAP Asset Manager (Endüstri), ChatGPT (Genel).
* **BridgeAI Farkı:**
    * **Hibrit Altyapı:** Hem sınıfı hem fabrikayı aynı teknolojik motorla yöneten tek platformdur.
    * **Kaynaktan Bağımsızlık:** Hazır veri tabanları yerine, kullanıcının elindeki her türlü fiziksel dökümanı (eski kitap, tozlu kılavuz) işleyebilir.
    * **Telif Koruması:** İçeriği kopyalamaz; pedagojik/teknik süzgeçten geçirerek yeniden kurgular.

## 🌍 5. Toplumsal Değer (Social Value)
* **Eğitimde Fırsat Eşitliği (SDG 4):** Ek kaynak bütçesi olmayan okullarda eğitimi demokratize eder.
* **İnsana Yakışır İş ve Güvenlik (SDG 8):** Karmaşık dökümanları anlaşılır kılarak iş kazalarını önler ve personelin yetkinliğini artırır.

## 🏆 6. Başarı Kriterleri
* En ücra köydeki öğrencinin dünya standartlarında materyallere ulaşması.
* Fabrikalarda "usta bağımlılığının" sona ermesi ve kurumsal hafızanın korunması.

## 🛠 7. Teknik Yol Haritası (Hedef: 14 Mayıs)
- [ ] **Frontend:** Streamlit ile kullanıcı dostu arayüz tasarımı.
- [ ] **Engine:** OpenAI Vision (Görsel okuma) ve GPT-4 (Anlamsal analiz) entegrasyonu.
- [ ] **Output:** ReportLab/FPDF ile otomatik PDF üretimi.
- [ ] **Ürün Gereksinim Belgesi (PRD) - Versiyon 1.1**

## 🎯 1. Proje Vizyonu
BridgeAI, fiziksel dünyadaki pasif ve karmaşık bilgiyi (eski kitaplar, teknik kılavuzlar) modern yapay zeka ile işleyerek; kişiselleştirilmiş, dijital ve aksiyona dönüştürülebilir içerikler üreten bir **akıllı bilgi köprüsü**dür.

---

## 👥 2. Kullanıcı Hikayeleri (User Stories)
* **Eğitimci:** "Elimdeki basılı materyalin fotoğrafını çekip, 11. sınıf öğrencilerimin seviyesine uygun bir quiz'i saniyeler içinde almak istiyorum."
* **Endüstriyel Tekniker:** "Karmaşık bir İSG dökümanını taratıp, sahada uygulayabileceğim basit bir 'adım adım kontrol listesi' oluşturmak istiyorum."

---

## 🛠 3. Fonksiyonel Gereksinimler & Ekranlar

### 🟢 Ekran 1: Giriş ve Yükleme Paneli
* **Dosya Girişi:** Kullanıcıdan fotoğraf (JPG/PNG) yüklemesi alınması.
* **Profil Seçimi:** Kullanıcı tipinin belirlenmesi (Eğitimci veya Teknik Personel).
* **Konfigürasyon:** Hedef çıktı formatının belirlenmesi (Quiz, Özet, Talimat Listesi).

### 🟡 Ekran 2: Analiz Paneli (AI İşleme)
* **OCR Entegrasyonu:** Görseldeki metnin dijital veriye dönüştürülmesi.
* **Anlamsal İşleme:** Metnin seçilen profile göre (Örn: A2 seviye İngilizce veya teknik operatör dili) yeniden kurgulanması.
* **Üretim:** Yapay zekanın "Bilgi Tercümanı" olarak yeni ve özgün içerik oluşturması.

### 🔴 Ekran 3: Çıktı ve İndirme Paneli
* **Önizleme:** Üretilen içeriğin kullanıcıya gösterilmesi.
* **Dışa Aktarma:** İçeriğin profesyonel bir PDF dosyası olarak indirilmesi.

---

## 💻 4. Teknik Teknoloji Yığını (Tech Stack)
| Katman | Teknoloji | Görev |
| :--- | :--- | :--- |
| **Arayüz (Frontend)** | Streamlit | Hızlı ve kullanıcı dostu web arayüzü. |
| **Zeka (AI Engine)** | OpenAI GPT-4o (Vision) | Görsel okuma, anlamsal analiz ve içerik üretimi. |
| **Dosya Üretimi** | FPDF / ReportLab | Dinamik PDF döküman oluşturma. |

---

## 🚀 5. Başarı Kriterleri & MVP Hedefleri
- [ ] Fotoğraflardaki metinlerin %95+ doğrulukla okunması.
- [ ] Seçilen profile göre dil seviyesinin başarıyla ayarlanması.
- [ ] **Hedef Tarih:** 14 Mayıs'ta çalışan bir demo sunumu.

---

---
*Bu dosya BridgeAI proje geliştirme sürecini takip etmek amacıyla oluşturulmuştur.*
