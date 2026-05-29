import streamlit as st
import pandas as pd

st.title("Sistem Informasi Imunisasi")

# Load data dengan caching agar cepat
@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()

    # Mengambil ID dari link QR yang di-scan
    query_params = st.query_params
    id_dari_link = query_params.get("id", [None])
    
    # Jika ada ID di link, langsung cari. Jika tidak, tampilkan input box
    if id_dari_link:
        id_input = id_dari_link
    else:
        id_input = st.text_input("Masukkan ID Bayi:")

    if id_input:
        # Pencarian data
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            st.success(f"Data Ditemukan untuk ID: {id_input}")
            st.table(hasil)
        else:
            st.error("ID tidak ditemukan.")
            
except Exception as e:
    st.error(f"Error memuat data: {e}")
