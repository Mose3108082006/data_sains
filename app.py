import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="ImuniScan Digital", page_icon="💉", layout="centered")

# CSS Profesional dengan efek modern
st.markdown("""
    <style>
    .main-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 20px;
    }
    .profile-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 8px solid #2ecc71;
    }
    .profile-icon { font-size: 50px; margin-bottom: 10px; }
    .name-text { font-size: 1.8rem; font-weight: 800; color: #2c3e50; margin: 0; }
    .label-text { font-size: 0.9rem; color: #7f8c8d; text-transform: uppercase; letter-spacing: 1px; margin-top: 15px; }
    .value-text { font-size: 1.2rem; font-weight: 600; color: #34495e; }
    </style>
""", unsafe_allow_html=True)

st.title("🏥 ImuniScan Pro")
st.caption("Sistem Informasi Layanan Imunisasi Terintegrasi")

@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()
    query_params = st.query_params
    id_scan = query_params.get("id", [None])
    
    id_input = id_scan if id_scan else st.text_input("🔍 Masukkan ID Bayi:")

    if id_input:
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            nama = hasil.iloc[0]['Nama Bayi']
            tgl_lahir = hasil.iloc[0]['Tanggal Lahir']
            
            # Tampilan kartu ID digital
            st.markdown(f"""
                <div class="profile-card">
                    <div class="profile-icon">👶</div>
                    <p class="name-text">{nama}</p>
                    <hr>
                    <div class="label-text">Tanggal Lahir</div>
                    <div class="value-text">{tgl_lahir}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("✅ Data Terverifikasi")
        else:
            st.error("❌ Data tidak ditemukan.")
            
except Exception as e:
    st.error("Terjadi kendala pada sistem.")
