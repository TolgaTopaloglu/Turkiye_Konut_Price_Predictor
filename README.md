# 🏠 TOKİ Konut Fiyat Tahmini

Bu proje, **Makine Öğrenmesi** ve **Regresyon** teknikleri kullanılarak 2026 yılı Türkiye TOKİ projelerindeki konut fiyatlarının **TL cinsinden tahmin edilmesini** amaçlamaktadır.

Projenin geliştirme sürecinde farklı makine öğrenmesi algoritmaları, hiperparametre optimizasyonu ve model performansları **MAE, MSE ve R²** metrikleri kullanılarak karşılaştırılmıştır.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine_Learning-orange.svg)
![LightGBM](https://img.shields.io/badge/LightGBM-Regression-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-red.svg)

---

## 🎯 Projenin Özeti

- **Amaç:** TOKİ konutlarının fiyatlarını farklı şehir, bölge ve proje özelliklerine göre tahmin etmek.
- **Veri Seti:** `turkiye_toki_projeleri_2026.csv` veri seti kullanılmıştır.
- **Veri Analizi:** Veri seti üzerinde EDA ve veri ön işleme işlemleri gerçekleştirilmiştir.
- **Feature Engineering:** Model performansını artırmak amacıyla özellik mühendisliği uygulanmıştır.
- **Modelleme:** Birden fazla regresyon algoritması denenmiş ve performansları karşılaştırılmıştır.
- **Hyperparameter Tuning:** LightGBM modeli üzerinde hiperparametre optimizasyonu gerçekleştirilmiştir.
- **Model Karşılaştırması:** Modeller MAE, MSE ve R² metrikleri kullanılarak değerlendirilmiştir.
- **En İyi Model:** Yapılan deneyler sonucunda **LGBM_Tuning_V3** nihai model olarak seçilmiştir.

---

## 📂 Veri Seti

Projede aşağıdaki veri seti kullanılmıştır:

`turkiye_toki_projeleri_2026.csv`

Veri seti üzerinde modelleme öncesinde veri temizleme, EDA, kategorik değişkenlerin dönüştürülmesi ve feature engineering işlemleri gerçekleştirilmiştir.

Modelde kullanılan temel değişkenler arasında:

- Şehir
- Bölge
- Proje Tipi
- Proje Durumu
- Konut özellikleri

gibi değişkenler bulunmaktadır.

---

## 🔍 Keşifçi Veri Analizi (EDA)

EDA aşamasında konut fiyatlarının farklı bölge, şehir ve proje özelliklerine göre değişimi incelenmiştir.

Özellikle **bölge, şehir, proje tipi ve proje durumu** gibi değişkenlerin konut fiyatları üzerindeki etkileri analiz edilmiştir.

### 🗺️ Bölgesel Fiyat Farklılıkları

Analiz sonuçlarına göre Ege ve Marmara bölgeleri en yüksek ortalama konut fiyatlarının görüldüğü bölgeler arasında yer almaktadır.

- **Ege:** Ortalama 2.095.742 TL
- **Marmara:** Ortalama 1.978.963 TL
- **Güneydoğu Anadolu:** Daha düşük ortalama fiyat seviyeleri
- **Doğu Anadolu:** Daha düşük ortalama fiyat seviyeleri

Bölgesel farklılıklar, konut fiyat tahmininde önemli değişkenlerden biri olarak değerlendirilmiştir.

### 🏙️ Kategorik Değişkenler

Model içerisinde şehir, bölge, proje tipi ve proje durumu gibi kategorik değişkenlerden yararlanılmıştır.

Proje tipi içerisinde:

- Sosyal Konut
- Orta Gelir
- Kentsel Dönüşüm

gibi kategoriler bulunmaktadır.

Kategorik değişkenler modelleme aşamasında uygun yöntemlerle sayısal forma dönüştürülmüştür.

---

## 🛡️ Data Leakage

Konut fiyat tahmininde fiyatla doğrudan ilişkili değişkenlerin modele dahil edilmesi veri sızıntısına neden olabilir.

Bu nedenle fiyatı doğrudan ele veren veya fiyat üzerinden oluşturulan değişkenler model eğitiminden çıkarılmıştır.

Özellikle:

- Peşinat Tutarı
- Taksit Miktarı

gibi değişkenler model eğitiminde kullanılmamıştır.

Bu sayede modelin konut fiyatını doğrudan ele veren bilgiler yerine proje ve konum özelliklerinden öğrenmesi amaçlanmıştır.

---

## 🤖 Kullanılan Modeller

Projede farklı regresyon algoritmaları denenmiştir:

- Linear Regression
- Ridge Regression
- SVR
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost
- LightGBM

Modeller aynı veri ve değerlendirme metrikleri kullanılarak karşılaştırılmıştır.

---

## ⚙️ Hyperparameter Tuning

LightGBM modeli üzerinde hiperparametre optimizasyonu gerçekleştirilmiştir.

Bu süreçte farklı model versiyonları oluşturulmuştur:

- `LGBM_Tuning_V1`
- `LGBM_Tuning_V2`
- `LGBM_Tuning_V3`

Modellerin performansları karşılaştırılarak en uygun model belirlenmiştir.

---

## 🧠 Kullanılan Model

Yapılan deneyler sonucunda nihai model olarak:

**LGBM_Tuning_V3**

seçilmiştir.

LightGBM modelleri yaklaşık **0.96 R²** skoruna ulaşmıştır.

Default LightGBM modeli bazı metriklerde V3 modelinden yaklaşık **800 TL daha düşük MAE** değerine sahip olsa da yaklaşık **1,7 milyon TL ortalama konut fiyatı** bulunan veri setinde bu fark oldukça düşüktür.

V3 modeli daha kontrollü hiperparametreler kullanılarak oluşturulduğu için **overfitting riskini azaltmak** ve yeni veriler üzerindeki **genelleme performansını artırmak** amacıyla tercih edilmiştir.

---

## 📊 Model Performansı

Modeller aşağıdaki metrikler üzerinden değerlendirilmiştir:

- **R² Score**
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**

### R² Score

![TOKI Price R2 Score]()

### MAE — Mean Absolute Error

![TOKI Price Mean Absolute Error]()

### MSE — Mean Squared Error

![TOKI Price Mean Squared Error]()

---

## 📈 Model Sonuçları

Yapılan deneyler sonucunda LightGBM tabanlı modeller diğer algoritmalara kıyasla daha başarılı sonuçlar vermiştir.

Özellikle **LGBM_Tuning_V3**, performans ve genelleme açısından projenin nihai modeli olarak belirlenmiştir.

Model değerlendirmesinde MAE, MSE ve R² sonuçları birlikte dikkate alınmıştır.

---

## 💻 Kurulum

### 1. Repoyu Klonlayın

```bash
git clone https://github.com/KullaniciAdin/TOKI-Price-Prediction.git
