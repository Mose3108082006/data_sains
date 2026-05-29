import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="ImuniScan Digital", page_icon="💉", layout="centered")

# CSS Profesional
st.markdown("""
    <style>
    .main-container { background-color: #f0f2f6; }
    .card {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        text-align: center;
        border: 1px solid #e1e4e8;
    }
    .emoji-circle { font-size: 60px; margin-bottom: 15px; }
    .name-title { font-size: 1.6rem; font-weight: 700; color: #1a1a1a; margin-bottom: 5px; }
    .label-text { font-size: 0.85rem; color: #888; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 20px; }
    .value-text { font-size: 1.3rem; font-weight: 600; color: #2d3436; }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>ImuniScan Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #636e72;'>Sistem Verifikasi Imunisasi Terintegrasi</p>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()
    
    # Pembersihan format tanggal saat memuat data (Opsional jika kolom sudah terbaca sebagai datetime)
    df['Tanggal Lahir'] = pd.to_datetime(df['Tanggal Lahir']).dt.strftime('%d-%m-%Y')

    query_params = st.query_params
    id_scan = query_params.get("id", [None])
    
    id_input = id_scan if id_scan else st.text_input("🔍 Masukkan ID Bayi:")

    if id_input:
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            nama = hasil.iloc[0]['Nama Bayi']
            tgl_lahir = hasil.iloc[0]['Tanggal Lahir']
            
            # Tampilan kartu ID digital yang bersih
            st.markdown(f"""
                <div class="card">
                    <div class="emoji-circle">👶</div>
                    <div class="name-title">{nama}</div>
                    <div class="label-text">Tanggal Lahir</div>
                    <div class="value-text">{tgl_lahir}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("✅ Identitas Terverifikasi")
        else:
            st.error("❌ Data tidak ditemukan. Pastikan ID benar.")
            
except Exception as e:
    st.error("Terjadi kendala pada sistem.")
