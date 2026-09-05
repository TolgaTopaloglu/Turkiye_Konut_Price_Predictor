# 🏠 TOKİ Konut Fiyat Tahmini

Bu proje, **Makine Öğrenmesi** ve **Regresyon** teknikleri kullanılarak 2026 yılı Türkiye TOKİ projelerindeki konut fiyatlarının **TL cinsinden tahmin edilmesini** amaçlamaktadır.

Projenin geliştirme sürecinde farklı makine öğrenmesi algoritmaları, hiperparametre optimizasyonu, **log normalizasyonu** ve **MLflow Experiment Tracking** kullanılmıştır. Modeller **MAE, MSE ve R²** metrikleri üzerinden karşılaştırılmıştır.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine_Learning-orange.svg)
![LightGBM](https://img.shields.io/badge/LightGBM-Regression-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-Experiment_Tracking-blueviolet.svg)

---

## 🎯 Projenin Özeti

- **Amaç:** TOKİ konutlarının fiyatlarını farklı şehir, bölge ve proje özelliklerine göre tahmin etmek.
- **Veri Seti:** `turkiye_toki_projeleri_2026.csv` veri seti kullanılmıştır.
- **Veri Analizi:** Veri seti üzerinde EDA ve veri ön işleme işlemleri gerçekleştirilmiştir.
- **Feature Engineering:** Model performansını artırmak amacıyla özellik mühendisliği uygulanmıştır.
- **Log Normalizasyonu:** Konut fiyatlarındaki dağılımı daha dengeli hâle getirmek amacıyla hedef değişkene log dönüşümü uygulanmıştır.
- **Modelleme:** Birden fazla regresyon algoritması denenmiş ve performansları karşılaştırılmıştır.
- **Hyperparameter Tuning:** LightGBM modeli üzerinde hiperparametre optimizasyonu gerçekleştirilmiştir.
- **MLflow:** Deneyler, parametreler ve model performansları MLflow ile takip edilmiştir.
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

## 📊 Log Normalizasyonu

Konut fiyatlarının dağılımında yüksek fiyatlı konutların oluşturduğu sağa çarpıklığı azaltmak amacıyla hedef değişkene **logaritmik dönüşüm** uygulanmıştır.

Bu işlem ile fiyat değerlerinin daha dengeli bir dağılıma sahip olması ve modelin aşırı yüksek değerlerden daha az etkilenmesi amaçlanmıştır.

Model eğitiminde log dönüşümü uygulanmış hedef değişken kullanılmış, tahmin sonuçları değerlendirme aşamasında tekrar orijinal fiyat ölçeğine dönüştürülmüştür.

Genel işlem akışı:

```text
Konut Fiyatı
     ↓
Log Transform
     ↓
Model Eğitimi
     ↓
Tahmin
     ↓
Inverse Transform
     ↓
Tahmini Fiyat (TL)
