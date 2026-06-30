import streamlit as st
import pandas as pd
import os
from PIL import Image

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Flood Risk Clustering using EM-DAT",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1,h2,h3,h4,h5,h6{
    color:white;
}

p,li{
    color:#E6E6E6;
}

.metric-box{
    background:#1E1E1E;
    padding:18px;
    border-radius:12px;
    border:1px solid #333;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.image(
    "https://img.icons8.com/color/480/floods.png",
    width=120
)

st.sidebar.title("🌊 Flood Risk Clustering")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📂 Dataset",
        "📊 Visualizations",
        "📈 Results",
        "📥 Downloads",
        "👨‍💻 About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Developed by

**Anurag Yadav**

M.Tech AI & ML
"""
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page=="🏠 Home":

    st.title("🌊 Flood Risk Clustering Using EM-DAT Data")

    st.markdown("""
This project presents an **unsupervised machine learning framework**
for identifying global flood risk patterns using the **EM-DAT
International Disaster Database**.

The project compares multiple clustering algorithms:

- K-Means
- Gaussian Mixture Model (GMM)
- DBSCAN
- OPTICS

using Principal Component Analysis (PCA) and cluster evaluation metrics.
""")

    st.markdown("---")

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Dataset",
        "EM-DAT"
    )

    c2.metric(
        "Algorithms",
        "4"
    )

    c3.metric(
        "Figures",
        "17"
    )

    c4.metric(
        "PCA Variance",
        "95%"
    )

    st.markdown("---")

    st.header("📌 Project Workflow")

    st.code("""
EM-DAT Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Feature Scaling
      │
      ▼
Principal Component Analysis
      │
      ▼
K-Means
GMM
DBSCAN
OPTICS
      │
      ▼
Cluster Evaluation
      │
      ▼
Flood Risk Interpretation
""")

    st.success(
        "K-Means achieved the best clustering performance."
    )

# -----------------------------
# DATASET PAGE
# -----------------------------
elif page=="📂 Dataset":

    st.title("📂 Dataset")

    st.write("""
Source:
EM-DAT International Disaster Database
""")

    st.markdown("""
### Dataset contains

- Total Deaths

- Total Affected

- Economic Damage

- Event Duration

- Flood Subtype

- Region

- Year
""")

    data_path="data/public_emdat_incl_hist_2026-06-22.xlsx"

    if os.path.exists(data_path):

        df=pd.read_excel(data_path)

        st.success("Dataset Loaded Successfully")

        st.dataframe(df.head())

        st.write("Shape:",df.shape)

        st.write("Columns")

        st.write(df.columns.tolist())

    else:

        st.warning("Dataset not found inside data folder.")

# ==========================================================
# VISUALIZATION PAGE
# ==========================================================
elif page=="📊 Visualizations":

    st.title("📊 Flood Risk Visualizations")

    st.write(
        """
        The following visualizations summarize the complete
        flood risk clustering workflow and results.
        """
    )

    figures = [

        ("Figure 1",
         "Feature Distributions",
         "fig1_emdat_feature_distributions.png"),

        ("Figure 2",
         "Global Flood Trends",
         "fig2_emdat_temporal_trends.png"),

        ("Figure 3",
         "Regional Impact Analysis",
         "fig3_emdat_regional_impact.png"),

        ("Figure 4",
         "Correlation Matrix",
         "fig4_emdat_correlation_matrix.png"),

        ("Figure 5",
         "PCA Scree Plot",
         "fig5_emdat_pca_scree.png"),

        ("Figure 6",
         "KMeans Hyperparameter Selection",
         "fig6_emdat_kmeans_selection.png"),

        ("Figure 7",
         "Gaussian Mixture Model",
         "fig7_emdat_gmm_selection.png"),

        ("Figure 8",
         "DBSCAN k-distance Plot",
         "fig8_emdat_dbscan_kdistance.png"),

        ("Figure 9",
         "KMeans Clusters",
         "fig9_emdat_kmeans_clusters.png"),

        ("Figure 10",
         "Gaussian Mixture Clusters",
         "fig10_emdat_gmm_clusters.png"),

        ("Figure 11",
         "DBSCAN Clusters",
         "fig11_emdat_dbscan_clusters.png"),

        ("Figure 12",
         "OPTICS Clusters",
         "fig12_emdat_optics_clusters.png"),

        ("Figure 13",
         "Model Comparison",
         "fig13_emdat_model_comparison.png"),

        ("Figure 14",
         "Cluster Profiles",
         "fig14_emdat_cluster_profiles.png"),

        ("Figure 15",
         "ANOVA Feature Importance",
         "fig15_emdat_anova_fscores.png"),

        ("Figure 16",
         "Regional Flood Risk",
         "fig16_emdat_regional_risk.png"),

        ("Figure 17",
         "Silhouette Plot",
         "fig17_emdat_silhouette_plot.png")

    ]

    for i in range(0, len(figures), 2):

        col1, col2 = st.columns(2)

        with col1:

            title, subtitle, file = figures[i]

            path = os.path.join("figures", file)

            if os.path.exists(path):

                st.subheader(title)

                st.caption(subtitle)

                image = Image.open(path)

                st.image(
                    image,
                    use_container_width=True
                )

            else:

                st.warning(f"{file} not found.")

        if i + 1 < len(figures):

            with col2:

                title, subtitle, file = figures[i + 1]

                path = os.path.join("figures", file)

                if os.path.exists(path):

                    st.subheader(title)

                    st.caption(subtitle)

                    image = Image.open(path)

                    st.image(
                        image,
                        use_container_width=True
                    )

                else:

                    st.warning(f"{file} not found.")

    st.success("All available visualizations displayed successfully.")

    # ==========================================================
# RESULTS PAGE
# ==========================================================
elif page == "📈 Results":

    st.title("📈 Results Dashboard")

    st.markdown("""
This section summarizes the major findings obtained from the clustering analysis.
""")

    st.divider()

    # -----------------------------------------------------
    # KPI Cards
    # -----------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Best Algorithm",
        "K-Means"
    )

    c2.metric(
        "Clusters",
        "2"
    )

    c3.metric(
        "PCA Variance",
        "95%"
    )

    c4.metric(
        "Figures",
        "17"
    )

    st.divider()

    # -----------------------------------------------------
    # Model Comparison
    # -----------------------------------------------------

    st.header("🏆 Model Performance Summary")

    performance = pd.DataFrame({

        "Algorithm":[
            "K-Means",
            "Gaussian Mixture Model",
            "DBSCAN",
            "OPTICS"
        ],

        "Performance":[
            "Best",
            "Good",
            "Moderate",
            "Weak"
        ],

        "Suitable":[
            "✅",
            "✅",
            "⚠️",
            "⚠️"
        ]

    })

    st.dataframe(
        performance,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------------------------------
    # Key Findings
    # -----------------------------------------------------

    st.header("🔍 Key Findings")

    st.success("""
✔ K-Means produced the best clustering performance.

✔ PCA retained approximately 95% of the original variance.

✔ Two natural flood-risk clusters were identified.

✔ Economic damage variables contributed most to cluster separation.

✔ Density-based algorithms (DBSCAN and OPTICS) were less effective for this dataset.
""")

    st.divider()

    # -----------------------------------------------------
    # Cluster Interpretation
    # -----------------------------------------------------

    st.header("🌍 Cluster Interpretation")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### Cluster 0

- Lower Flood Risk

- Lower deaths

- Lower affected population

- Lower economic damage

- More frequent events
""")

    with col2:

        st.warning("""
### Cluster 1

- Higher Flood Risk

- Higher deaths

- Higher affected population

- Higher economic damage

- Severe flood events
""")

    st.divider()

    # -----------------------------------------------------
    # Research Contributions
    # -----------------------------------------------------

    st.header("📚 Contributions")

    st.markdown("""

This project demonstrates:

- Feature engineering for disaster datasets.

- Principal Component Analysis for dimensionality reduction.

- Comparative evaluation of four clustering algorithms.

- Flood-risk categorization using unsupervised learning.

- Publication-quality visualizations.

""")

    st.divider()

    # -----------------------------------------------------
    # Future Work
    # -----------------------------------------------------

    st.header("🚀 Future Work")

    st.markdown("""

- Deep Clustering

- Autoencoder-based Clustering

- Explainable AI

- Satellite Data Integration

- Flood Forecasting

- Interactive Dashboard

""")

    st.success("Analysis completed successfully.")


# ==========================================================
# DOWNLOADS PAGE
# ==========================================================
elif page == "📥 Downloads":

    st.title("📥 Download Results")

    st.write(
        """
        Download the processed datasets and results generated
        during the flood risk clustering analysis.
        """
    )

    st.divider()

    files = [

        (
            "Flood Risk Clusters",
            "results/FloodRiskClusters.csv"
        ),

        (
            "Cluster Profile",
            "results/ClusterProfile.csv"
        ),

        (
            "ANOVA Feature Importance",
            "results/ANOVA_Feature_Importance.csv"
        ),

        (
            "Cluster Risk Mapping",
            "results/Table_Cluster_Risk_Mapping.csv"
        )

    ]

    for title, file in files:

        st.subheader(title)

        if os.path.exists(file):

            with open(file, "rb") as f:

                st.download_button(

                    label=f"Download {os.path.basename(file)}",

                    data=f,

                    file_name=os.path.basename(file),

                    mime="text/csv"

                )

            st.success("Available")

        else:

            st.error("File not found")

        st.divider()

    # -------------------------------------------------

    st.header("📒 Notebook")

    notebook = "Flood_Risk_Clustering_EMDAT.ipynb"

    if os.path.exists(notebook):

        with open(notebook, "rb") as f:

            st.download_button(

                label="Download Jupyter Notebook",

                data=f,

                file_name=notebook,

                mime="application/octet-stream"

            )

    else:

        st.warning("Notebook not found.")

    st.divider()

    st.header("📁 Repository Contents")

    folders = [

        "data",

        "figures",

        "results"

    ]

    for folder in folders:

        if os.path.exists(folder):

            st.subheader(folder)

            files = sorted(os.listdir(folder))

            for f in files:

                st.write("📄", f)

        else:

            st.warning(f"{folder} folder not found.")

# ==========================================================
# ABOUT PAGE
# ==========================================================
elif page == "👨‍💻 About":

    st.title("👨‍💻 About")

    st.markdown("""
## Flood Risk Clustering Using EM-DAT Data

This dashboard presents an unsupervised machine learning
framework for analysing historical flood events using the
EM-DAT International Disaster Database.

The project demonstrates:

- Data preprocessing
- Feature engineering
- Principal Component Analysis
- K-Means Clustering
- Gaussian Mixture Models
- DBSCAN
- OPTICS
- Cluster evaluation
- Publication-quality visualisations
""")

    st.divider()

    st.header("👨‍🎓 Author")

    st.markdown("""
**Anurag Yadav**

M.Tech in Artificial Intelligence & Machine Learning
""")

    st.divider()

    st.header("🔗 Links")

    st.markdown("""
**GitHub Repository**

https://github.com/AnuragYadav12/Flood-Risk-Clustering-EMDAT

**GitHub Profile**

https://github.com/AnuragYadav12

**LinkedIn**

https://linkedin.com/in/Anurag-Yadav
""")

    st.divider()

    st.header("📚 Citation")

    st.code("""

@misc{yadav2026,

 author={Anurag Yadav},

 title={Flood Risk Clustering Using EM-DAT Data},

 year={2026},

 publisher={GitHub}

}

""")

    st.divider()

    st.info(
        "Thank you for exploring this project."
    )

    st.caption(
        "Made with ❤️ using Streamlit"
    )