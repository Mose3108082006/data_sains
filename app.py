import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="ImuniScan - Info Bayi", page_icon="👶")

# CSS Kustom untuk tampilan Profesional
st.markdown("""
    <style>
    .card {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #4CAF50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .header-text { color: #2e7d32; font-weight: bold; }
    .label { font-size: 0.9rem; color: #666; }
    .value { font-size: 1.4rem; color: #333; font-weight: 600; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("👶 ImuniScan Digital")
st.write("Sistem Informasi Imunisasi Terintegrasi")

@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()
    
    # Ambil ID dari QR
    query_params = st.query_params
    id_scan = query_params.get("id", [None])
    
    # Input area
    id_input = id_scan if id_scan else st.text_input("🔍 Masukkan ID Bayi untuk cek data:")

    if id_input:
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            nama = hasil.iloc[0]['Nama Bayi']
            tgl_lahir = hasil.iloc[0]['Tanggal Lahir']
            
            # Tampilan kartu (Card) Profesional
            st.markdown(f"""
                <div class="card">
                    <h3 class="header-text">Informasi Pasien</h3>
                    <div class="label">Nama Lengkap</div>
                    <div class="value">{nama}</div>
                    <div class="label">Tanggal Lahir</div>
                    <div class="value">{tgl_lahir}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("Data diverifikasi oleh sistem.")
        else:
            st.error("Data tidak ditemukan.")
            
except Exception as e:
    st.error("Terjadi kendala sistem.")
