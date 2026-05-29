import streamlit as st
import pandas as pd

st.title("Sistem Informasi Imunisasi")

# 1. Load data
@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

df = load_data()

# 2. Input Pencarian
id_input = st.text_input("Masukkan ID Bayi:")

if id_input:
    # Cari data
    hasil = df[df['No'].astype(str) == id_input]
    
    if not hasil.empty:
        st.success("Data Ditemukan!")
        st.write(hasil) # Menampilkan data bayi
    else:
        st.error("ID tidak ditemukan.")