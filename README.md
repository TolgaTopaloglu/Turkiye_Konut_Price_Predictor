> ⚠️ **Veri Seti Notu:** Bu veri seti, Türkiye'nin 2026 yılına ait gerçek dünya sosyo-ekonomik parametreleri, konut dağılımları ve demografik ağırlıkları temel alınarak sentetik olarak oluşturulmuş bir simülasyondur. Veri seti yalnızca **eğitim, makine öğrenmesi ve veri görselleştirme** amaçlarıyla hazırlanmıştır. Gerçek bir konut veri tabanını veya herhangi bir kurumun resmî verilerini doğrudan temsil etmemektedir.

# 🏠 Türkiye Konut Fiyat Tahmini

<img width="1777" height="1147" alt="Turkey Housing Price Prediction Frontend" src="https://github.com/user-attachments/assets/8b215290-213c-4f4f-a99f-82c494db591b" />

Bu proje, **Makine Öğrenmesi** ve **Regresyon** teknikleri kullanılarak Türkiye'deki konut fiyatlarının **TL cinsinden tahmin edilmesini** amaçlamaktadır.

Projenin geliştirme sürecinde farklı makine öğrenmesi algoritmaları, hiperparametre optimizasyonu, **log normalizasyonu** ve **MLflow Experiment Tracking** kullanılmıştır. Modeller **MAE, MSE ve R²** metrikleri üzerinden karşılaştırılmıştır.

![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine_Learning-orange.svg)
![LightGBM](https://img.shields.io/badge/LightGBM-Regression-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Regression-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-Experiment_Tracking-blueviolet.svg)

---

## 🎯 Projenin Özeti

- **Amaç:** Türkiye'deki konut fiyatlarını; şehir, bölge ve proje özellikleri gibi değişkenlere göre tahmin etmek.
- **Veri Seti:** `turkiye_konut_projeleri_2026.csv` veri seti kullanılmıştır.
- **Veri Ön İşleme:** Veri temizleme ve modelleme öncesi gerekli dönüşümler gerçekleştirilmiştir.
- **Feature Engineering:** Model performansını artırmak amacıyla özellik mühendisliği uygulanmıştır.
- **Log Normalizasyonu:** Konut fiyatlarının dağılımını daha dengeli hâle getirmek amacıyla hedef değişkene log dönüşümü uygulanmıştır.
- **Modelleme:** Birden fazla regresyon algoritması denenmiş ve performansları karşılaştırılmıştır.
- **Hyperparameter Tuning:** LightGBM modeli üzerinde hiperparametre optimizasyonu gerçekleştirilmiştir.
- **MLflow:** Deneyler, hiperparametreler ve model performansları MLflow ile takip edilmiştir.
- **Model Karşılaştırması:** Modeller MAE, MSE ve R² metrikleri kullanılarak değerlendirilmiştir.
- **En İyi Model:** Yapılan deneyler sonucunda **LGBM_Tuning_V3** nihai model olarak seçilmiştir.

---

## 📂 Veri Seti

Projede aşağıdaki veri seti kullanılmıştır:

`turkiye_konut_projeleri_2026.csv`

Veri seti üzerinde modelleme öncesinde veri temizleme, kategorik değişkenlerin dönüştürülmesi ve feature engineering işlemleri gerçekleştirilmiştir.

Modelde kullanılan temel değişkenler arasında:

- Şehir
- Bölge
- Proje Tipi
- Proje Durumu

gibi değişkenler bulunmaktadır.

---

## 📊 Log Normalizasyonu

Konut fiyatlarının dağılımında yüksek fiyatlı konutların etkisini azaltmak ve hedef değişkeni modelleme için daha uygun hâle getirmek amacıyla **logaritmik dönüşüm** uygulanmıştır.

Bu işlem ile fiyat değişkenindeki dağılımın daha dengeli hâle getirilmesi ve modelin aşırı yüksek değerlerden daha az etkilenmesi amaçlanmıştır.

Modelleme süreci genel olarak şu şekilde gerçekleştirilmiştir:

**Konut Fiyatı → Log Dönüşümü → Model Eğitimi → Tahmin → Ters Log Dönüşümü → TL Fiyatı**

Model tahminleri değerlendirme aşamasında tekrar orijinal fiyat ölçeğine dönüştürülerek **TL cinsinden** değerlendirilmiştir.

---

## 🛡️ Data Leakage

Konut fiyat tahmininde hedef değişkenle doğrudan ilişkili değişkenlerin modele dahil edilmesi veri sızıntısına neden olabilir.

Bu nedenle fiyatı doğrudan ele veren veya fiyat üzerinden oluşturulan değişkenler model eğitiminden çıkarılmıştır.

Özellikle:

- Peşinat Tutarı
- Taksit Miktarı

gibi değişkenler model eğitiminde kullanılmamıştır.

Bu sayede modelin konut fiyatını doğrudan ele veren bilgiler yerine diğer proje ve konum özelliklerinden öğrenmesi amaçlanmıştır.

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

## 🔬 MLflow Experiment Tracking

Projenin model geliştirme sürecinde **MLflow** kullanılarak deney takibi gerçekleştirilmiştir.

MLflow ile:

- Farklı modellerin sonuçları takip edilmiştir.
- Hiperparametreler kayıt altına alınmıştır.
- MAE, MSE ve R² metrikleri loglanmıştır.
- Model versiyonları karşılaştırılmıştır.
- Deney sonuçları kayıt altında tutulmuştur.
- En başarılı modelin belirlenmesi kolaylaştırılmıştır.

MLflow sayesinde farklı model ve hiperparametre denemeleri tek bir deney takip sistemi üzerinden karşılaştırılmıştır.

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

<img width="1200" height="600" alt="Turkey Housing Price R2 Score" src="https://github.com/user-attachments/assets/0c26b627-535c-457b-aad9-91a5f653fa90" />

### MAE — Mean Absolute Error

<img width="1200" height="600" alt="Turkey Housing Price Mean Absolute Error" src="https://github.com/user-attachments/assets/26416864-8b1a-4495-ab31-bb61c4459487" />

### MSE — Mean Squared Error

<img width="1200" height="600" alt="Turkey Housing Price Mean Squared Error" src="https://github.com/user-attachments/assets/448755e7-8a6d-497a-880c-0b9f4a384916" />

---

## 📈 Model Sonuçları

Yapılan deneyler sonucunda LightGBM tabanlı modeller diğer algoritmalara kıyasla daha başarılı sonuçlar vermiştir.

Özellikle **LGBM_Tuning_V3**, performans ve genelleme açısından projenin nihai modeli olarak belirlenmiştir.

Model değerlendirmesinde **MAE, MSE ve R²** sonuçları birlikte dikkate alınmıştır.

Log normalizasyonu sonrasında tahmin sonuçları tekrar orijinal TL ölçeğine dönüştürülerek değerlendirilmiştir.

---

## 💻 Kurulum

### 1. Repoyu Klonlayın

    git clone https://github.com/KullaniciAdin/Turkey-Housing-Price-Prediction.git

Proje klasörüne girin:

    cd Turkey-Housing-Price-Prediction

### 2. Virtual Environment Oluşturun

Windows:

    python -m venv .venv

Virtual environment'ı aktif edin:

    .venv\Scripts\activate

Linux / macOS:

    python3 -m venv .venv
    source .venv/bin/activate

### 3. Gerekli Kütüphaneleri Kurun

    pip install -r requirements.txt

---


## 📁 Proje Yapısı

    Turkey-Housing-Price-Prediction/
    │
    ├── data/
    │   └── turkiye_konut_projeleri_2026.csv
    │
    ├── notebooks/
    │   └── Turkey_Housing_Price_Prediction.ipynb
    │
    ├── models/
    │   └── LGBM_Tuning_V3
    │
    ├── mlruns/
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

---

## 📦 Kullanılan Teknolojiler

| Teknoloji | Kullanım |
|---|---|
| Python | Programlama dili |
| Pandas | Veri işleme |
| NumPy | Sayısal işlemler |
| Matplotlib | Veri görselleştirme |
| Seaborn | Veri görselleştirme |
| Scikit-learn | Makine öğrenmesi |
| LightGBM | Regresyon |
| XGBoost | Regresyon |
| MLflow | Deney ve model takibi |

---

## 📋 Requirements

Projede kullanılan temel kütüphaneler:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `lightgbm`
- `xgboost`
- `mlflow`

Tüm bağımlılıkları yüklemek için:

    pip install -r requirements.txt

---

## 🏆 Sonuç

Bu projede farklı makine öğrenmesi algoritmaları kullanılarak **Türkiye'deki konut fiyatlarının tahmini** gerçekleştirilmiştir.

Model geliştirme sürecinde **Feature Engineering, Log Normalizasyonu, Hyperparameter Tuning ve MLflow Experiment Tracking** kullanılmıştır.

Yapılan model karşılaştırmaları sonucunda **LightGBM tabanlı modeller** en başarılı sonuçları vermiş ve yaklaşık **0.96 R²** skoruna ulaşmıştır.

Yapılan değerlendirmeler sonucunda **LGBM_Tuning_V3**, performans ve genelleme kabiliyeti açısından projenin nihai modeli olarak seçilmiştir.

> **Not:** Model sonuçları kullanılan sentetik veri seti ile sınırlıdır. Tahminler gerçek konut fiyatlarının garantisi değildir.

---


GitHub:

https://github.com/TolgaTopaloglu
