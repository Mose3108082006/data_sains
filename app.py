import streamlit as st
import pandas as pd

# Styling agar tampilan lebih rapi dan profesional
st.set_page_config(page_title="Data Imunisasi", page_icon="💉")

st.title("💉 Data Imunisasi Bayi")
st.markdown("---")

@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()

    # Mengambil ID dari link QR
    query_params = st.query_params
    id_dari_link = query_params.get("id", [None])
    
    if id_dari_link:
        id_input = id_dari_link
    else:
        id_input = st.text_input("🔍 Masukkan ID Bayi:")

    if id_input:
        # Pencarian data
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            st.success("✅ Data Berhasil Ditemukan")
            
            # MENGAMBIL HANYA KOLOM TERTENTU (Sesuaikan nama kolom dengan Excel Anda)
            # Pastikan nama kolom 'Nama Bayi' dan 'Tanggal Lahir' ada di Excel
            data_tampil = hasil[['Nama Bayi', 'Tanggal Lahir']]
            
            # Menampilkan dengan kartu yang rapi
            st.markdown("### Informasi Bayi")
            st.table(data_tampil.reset_index(drop=True))
            
            st.info("Informasi lain disembunyikan untuk menjaga privasi.")
        else:
            st.error("❌ ID tidak ditemukan. Periksa kembali ID Anda.")
            
except Exception as e:
    st.error(f"Sistem sedang sibuk: {e}")
