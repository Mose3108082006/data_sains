import pandas as pd
import qrcode
import os

# 1. Load data Excel
df = pd.read_excel('Data Identitas Bayi dan kehaidran imunisasi.xlsx', skiprows=5)
FOLDER_QR = 'QR_Codes'
BASE_URL = "https://datasains.streamlit.app/" 

if not os.path.exists(FOLDER_QR):
    os.makedirs(FOLDER_QR)

print("Membuat QR Code unik (berdasarkan ID saja)...")

for index, row in df.iterrows():
    # Pastikan 'No' di Excel adalah kolom ID Anda
    id_bayi = str(row['No']).replace('.0', '') # Menghapus .0 jika muncul di ID
    
    # Lewati jika ID kosong atau tidak valid
    if id_bayi == 'nan' or id_bayi == 'None':
        continue
        
    # Link unik
    link_unik = f"{BASE_URL}?id={id_bayi}"
    
    # Buat QR
    img = qrcode.make(link_unik)
    
    # Simpan hanya dengan nomor ID
    nama_file = f"{FOLDER_QR}/QR_{id_bayi}.png"
    img.save(nama_file)
    print(f"Berhasil: {nama_file}")

print("\nSelesai! Semua QR Code (berdasarkan nomor ID) sudah siap di folder 'QR_Codes'.")
