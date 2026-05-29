import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="ImuniScan Digital", page_icon="💉", layout="centered")

# CSS Profesional untuk tampilan modern
st.markdown("""
    <style>
    .card {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 8px solid #2ecc71;
    }
    .emoji-circle { font-size: 50px; margin-bottom: 10px; }
    .name-title { font-size: 1.5rem; font-weight: 800; color: #2c3e50; margin-bottom: 5px; }
    .label-text { font-size: 0.8rem; color: #95a5a6; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; }
    .value-text { font-size: 1.2rem; font-weight: 600; color: #34495e; }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown("<h1 style='text-align: center;'>ImuniScan Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Sistem Verifikasi Imunisasi Terintegrasi</p>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Pastikan file Excel ada di folder yang sama dengan app.py
    return pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)

try:
    df = load_data()
    
    # Mengambil ID dari URL (QR Code) atau Input Manual
    query_params = st.query_params
    id_dari_link = query_params.get("id", [None])
    id_input = id_dari_link if id_dari_link else st.text_input("🔍 Masukkan ID Bayi:")

    if id_input:
        # Konversi kolom ke string agar pencarian ID akurat
        hasil = df[df['No'].astype(str) == str(id_input).strip()]
        
        if not hasil.empty:
            nama = hasil.iloc[0]['Nama Bayi']
            
            # AMBIL TANGGAL DAN BUANG JAMNYA
            # Kita konversi ke string dulu, lalu ambil bagian sebelum spasi (YYYY-MM-DD)
            tgl_mentah = str(hasil.iloc[0]['Tanggal Lahir'])
            tgl_bersih = tgl_mentah.split(' ')[0] 
            
            # Tampilkan kartu
            st.markdown(f"""
                <div class="card">
                    <div class="emoji-circle">👶</div>
                    <div class="name-title">{nama}</div>
                    <div class="label-text">Tanggal Lahir</div>
                    <div class="value-text">{tgl_bersih}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.success("✅ Identitas Terverifikasi")
        else:
            st.error("❌ Data tidak ditemukan. Periksa kembali ID Anda.")
            
except Exception:
    st.error("⚠️ Terjadi kesalahan. Pastikan format file Excel benar.")
