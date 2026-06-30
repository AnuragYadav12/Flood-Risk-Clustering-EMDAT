# 🌊 Flood Risk Clustering Using EM-DAT Data

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 Project Overview

This project presents an **unsupervised machine learning framework** for identifying global flood risk patterns using the **EM-DAT (Emergency Events Database)**. Unlike traditional flood risk studies based on simulated datasets, this work utilizes **real-world historical flood events** and applies clustering algorithms to discover distinct flood-risk groups.

The project compares multiple clustering techniques and evaluates their performance using standard internal and external clustering metrics.

---

## 🎯 Objectives

- Perform exploratory analysis of historical flood events.
- Engineer meaningful flood-impact features.
- Reduce dimensionality using Principal Component Analysis (PCA).
- Compare multiple clustering algorithms.
- Identify natural flood-risk groups.
- Interpret cluster characteristics for disaster risk assessment.

---

## 📂 Dataset

**Source:** EM-DAT – The International Disaster Database

The dataset contains historical flood events worldwide, including information such as:

- Total deaths
- Total affected population
- Economic damage
- Event duration
- Flood subtype
- Region
- Year of occurrence

---

## ⚙️ Feature Engineering

The following engineered features were used:

- Log_TotalDeaths
- Log_TotalAffected
- Log_TotalDamage
- Log_AdjDamage
- Log_DamagePerDeath
- Log_Duration
- Month_Sin
- Month_Cos
- FloodSubtype_Code
- Region_Code
- Start Year

All numerical features were standardized before clustering.

---

## 🔬 Methodology

The workflow of this project is shown below:

```
EM-DAT Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Standardization
      │
      ▼
Principal Component Analysis (PCA)
      │
      ▼
Clustering Algorithms
      │
      ├── K-Means
      ├── Gaussian Mixture Model
      ├── DBSCAN
      └── OPTICS
      │
      ▼
Evaluation
      │
      ▼
Cluster Interpretation
```

---

## 🤖 Machine Learning Algorithms

The following clustering algorithms were evaluated:

- K-Means
- Gaussian Mixture Model (GMM)
- DBSCAN
- OPTICS

---

## 📊 Evaluation Metrics

Models were compared using:

- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index
- Adjusted Rand Index (ARI)
- Normalized Mutual Information (NMI)

---

# 📈 Results

The analysis identified **two natural flood-risk clusters** representing different levels of flood severity.

Key observations include:

- K-Means achieved the best overall clustering performance.
- PCA retained approximately **95%** of the total variance.
- Economic damage variables were the strongest contributors to cluster separation.
- DBSCAN and OPTICS were less suitable due to the density characteristics of the dataset.

---

# 📷 Figures

## Feature Engineering

![](figures/fig1_emdat_feature_distributions.png)

---

## Global Flood Trends

![](figures/fig2_emdat_temporal_trends.png)

---

## Correlation Matrix

![](figures/fig4_emdat_correlation_matrix.png)

---

## PCA Analysis

![](figures/fig5_emdat_pca_scree.png)

---

## K-Means Clustering

![](figures/fig9_emdat_kmeans_clusters.png)

---

## Cluster Feature Profile

![](figures/fig14_emdat_cluster_profiles.png)

---

## Feature Importance (ANOVA)

![](figures/fig15_emdat_anova_fscores.png)

---

## Final Silhouette Plot

![](figures/fig17_emdat_silhouette_plot.png)

---

# 📁 Repository Structure

```
Flood-Risk-Clustering-EMDAT/
│
├── data/
│   ├── public_emdat_2026-06-22.xlsx
│   └── public_emdat_incl_hist_2026-06-22.xlsx
│
├── figures/
│   ├── fig1_emdat_feature_distributions.png
│   ├── ...
│   └── fig17_emdat_silhouette_plot.png
│
├── results/
│   ├── ANOVA_Feature_Importance.csv
│   ├── ClusterProfile.csv
│   ├── FloodRiskClusters.csv
│   └── Table_Cluster_Risk_Mapping.csv
│
├── Flood_Risk_Clustering_EMDAT.ipynb
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Flood-Risk-Clustering-EMDAT.git
```

Move into the project directory

```bash
cd Flood-Risk-Clustering-EMDAT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Open

```
Flood_Risk_Clustering_EMDAT.ipynb
```

and run all cells.

---

# 📦 Dependencies

Major libraries used:

- Python 3.11
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- openpyxl

---

# 🔮 Future Work

- Incorporate deep clustering techniques.
- Integrate satellite-derived flood indicators.
- Develop an interactive flood risk dashboard.
- Apply temporal forecasting for future flood-risk prediction.

---

# 👨‍💻 Author

**Anurag Yadav**

M.Tech in Artificial Intelligence & Machine Learning

GitHub: https://github.com/Anurag-Yadav

LinkedIn: https://linkedin.com/in/Anurag-Yadav

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, please consider giving it a star!
