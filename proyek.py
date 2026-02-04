import streamlit as st
import pandas as pd

def tampilkan_proyek():
    st.title("📊 Customer Purchase Behavior Analysis")
    st.caption("Shopping Trends Dataset | EDA & RFM Analysis")

    # ======================
    # PROJECT OVERVIEW
    # ======================
    st.markdown("""
    Project ini bertujuan untuk memahami **perilaku pembelian pelanggan**
    berdasarkan data transaksi *Shopping Trends*.
    Analisis dilakukan menggunakan Exploratory Data Analysis (EDA)
    dan segmentasi pelanggan berbasis RFM.
    """)

    # ======================
    # BUSINESS PROBLEM
    # ======================
    st.subheader("🧩 Business Problem")
    st.markdown("""
    Perusahaan memiliki data transaksi dalam jumlah besar,
    namun kesulitan memahami pola perilaku pelanggan,
    segmen bernilai tinggi, dan preferensi produk.
    """)

    # ======================
    # DATASET OVERVIEW
    # ======================
    st.subheader("📁 Dataset Overview")
    col1, col2 = st.columns(2)
    col1.metric("Total Transaksi", "3.900")
    col1.metric("Jenis Data", "Customer Transaction")
    col2.metric("Sumber Data", "Kaggle (Synthetic)")
    col2.metric("Tools", "Python & Power BI")

    # ======================
    # ANALYSIS APPROACH
    # ======================
    st.subheader("🔍 Analysis Approach")
    st.markdown("""
    Analisis dilakukan dengan:
    - Exploratory Data Analysis (EDA)
    - Analisis deskriptif
    - RFM Analysis (Recency, Frequency, Monetary)
    """)

    # ======================
    # TEMUAN 1 - RFM
    # ======================
    st.subheader("📌 Temuan 1: Segmentasi Pelanggan (RFM)")

    rfm_data = pd.DataFrame({
        "Segment": [
            "Regular Customer",
            "Loyal Customer",
            "Big Spender",
            "High Value Customer"
        ],
        "Persentase (%)": [36.3, 23.7, 23.7, 16.3]
    })

    st.bar_chart(rfm_data.set_index("Segment"))

    st.markdown("""
    Mayoritas pelanggan berada pada segmen **Regular Customer**.
    Meskipun jumlah **High Value Customer** lebih kecil,
    segmen ini memberikan kontribusi nilai pembelian yang tinggi.
    """)

    # ======================
    # TEMUAN 2 - KATEGORI PRODUK
    # ======================
    st.subheader("📌 Temuan 2: Kategori Produk Paling Diminati")

    category_data = pd.DataFrame({
        "Category": ["Clothing", "Accessories", "Footwear", "Outerwear"],
        "Jumlah Pelanggan": [1900, 1300, 500, 200]
    })

    st.bar_chart(category_data.set_index("Category"))

    st.markdown("""
    Kategori **Clothing** menjadi kategori produk paling diminati,
    diikuti oleh **Accessories**.
    Ini menunjukkan fokus pelanggan pada produk fashion.
    """)

    # ======================
    # TEMUAN 3 - GENDER & KATEGORI
    # ======================
    st.subheader("📌 Temuan 3: Pembelian Berdasarkan Gender & Kategori")

    gender_category = pd.DataFrame({
        "Category": ["Clothing", "Accessories", "Footwear", "Outerwear"],
        "Male": [1100, 750, 300, 120],
        "Female": [800, 550, 200, 80]
    }).set_index("Category")

    st.bar_chart(gender_category)

    st.markdown("""
    Terdapat perbedaan pola pembelian antara pelanggan pria dan wanita
    di tiap kategori produk, dengan dominasi pelanggan pria
    pada sebagian besar kategori.
    """)

    # ======================
    # TEMUAN 4 - WARNA PRODUK
    # ======================
    st.subheader("📌 Temuan 4: Preferensi Warna Produk")

    color_data = pd.DataFrame({
        "Color": ["Yellow", "Teal", "Violet", "Turquoise", "White"],
        "Total Purchase": [210, 190, 175, 160, 150]
    })

    st.bar_chart(color_data.set_index("Color"))

    st.markdown("""
    Warna **Yellow, Teal, Violet, Turquoise, dan White**
    memiliki tingkat pembelian tertinggi,
    khususnya pada kategori Clothing dan Accessories.
    """)

    # ======================
    # TEMUAN 5 - SEGMENTASI PER KATEGORI
    # ======================
    st.subheader("📌 Temuan 5: Segmentasi Pelanggan per Kategori Produk")

    segment_category = pd.DataFrame({
        "Category": ["Clothing", "Accessories", "Footwear", "Outerwear"],
        "Regular": [700, 500, 150, 65],
        "Loyal": [600, 400, 140, 60],
        "High Value": [400, 300, 120, 40]
    }).set_index("Category")

    st.bar_chart(segment_category)

    st.markdown("""
    Kategori **Clothing** mendominasi seluruh segmen pelanggan,
    terutama pada Regular dan Loyal Customer.
    """)

    # ======================
    # RECOMMENDATIONS
    # ======================
    st.subheader("💡 Actionable Business Recommendations")

    st.markdown("""
    1. Fokus retensi pada **High Value Customer**
    2. Prioritaskan kategori **Clothing & Accessories**
    3. Terapkan strategi pemasaran berbasis segmentasi RFM
    4. Optimalkan metode pembayaran non-tunai
    5. Sesuaikan stok berdasarkan preferensi warna pelanggan
    """)

    st.success("""
    Analisis ini menunjukkan bagaimana data transaksi
    dapat diubah menjadi insight bisnis yang
    relevan dan dapat ditindaklanjuti.
    """)