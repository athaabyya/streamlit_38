import streamlit as st

st.set_page_config(
    page_title="Data Scientist Portfolio",
    layout="wide"
)

st.sidebar.title("Navigasi")

page = st.sidebar.radio(
    "Pilih halaman",
    ["Tentang Saya", "Proyek", "Kontak"]
)

if page == "Tentang Saya":
    import tentang
    tentang.about_me()

elif page == "Proyek":
    import proyek
    proyek.tampilkan_proyek()

elif page == "Kontak":
    import kontak
    kontak.munculkan_kontak()