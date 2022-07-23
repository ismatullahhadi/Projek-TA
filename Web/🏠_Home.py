import streamlit as st
from PIL import Image
# from xarray import align
from pathlib import Path

st.set_page_config(
    page_title="Halaman Utama",
    page_icon="🏠",
)

st.title("Selamat datang")

st.sidebar.info("Pilih fitur.")

st.markdown(
    """
    <div style='text-align: justify;'>
    Aplikasi ini dibuat dengan menggunakan streamlit untuk melakukan visualisasi regresi dan klasifikasi Data ISPU.
    
    Data ISPU juga bisa diakses di [halaman resmi.](https://ispu.menlhk.go.id/map.html)
    </div>
""", unsafe_allow_html=True
)

st.header("Apa itu ISPU?")

st.markdown(
    """
        <div style='text-align: justify;'>
        Menurut Peraturan Menteri Lingkungan Hidup dan Kehutanan Nomor P.14/Menlhk/Setjen/Kum.1/7/2020 tentang Indeks Standar Pencemar Udara, 
        <b>ISPU</b> merupakan angka tanpa satuan yang menggambarkan kondisi kualitas udara ambien di lokasi tertentu, yang didasarkan pada dampak terhadap 
        kesehatan manusia, nilai estetik, dan makhluk hidup lainnya. Adapun parameter ISPU meliputi Hidrokarbon (HC), Karbon monoksida (CO), Sulfur dioksida (SO2), 
        Nitrogen dioksida (NO2), Ozon (O3), dan Partikulat (PM10 dan PM2,5).
        </div>
    """, unsafe_allow_html=True
)

# tabel_kategori_ispu = Image.open('images/Tabel_kategori_indeks_ISPU.png')
tabel_kategori_ispu = Image.open(Path(__file__).parents[1] / 'Web/images/Tabel_kategori_indeks_ISPU.png')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(tabel_kategori_ispu, caption='Tabel Kategori Indeks ISPU')

with col3:
    st.write("")

st.markdown(
    """
        <div style='text-align: justify;'>
        Hasil perhitungan ISPU parameter PM2.5 disampaikan kepada publik tiap jam selama 24 jam. Sedangkan hasil perhitungan ISPU parameter PM10, NO2, SO2, CO, O3, 
        dan HC disampaikan kepada publik paling sedikit 2 (dua) kali dalam 1 (satu) hari pada pukul 09.00 dan 15.00. Tabel konversi nilai konsentrasi parameter ISPU 
        dan cara perhitungan sebagai berikut:
        </div>
    """, unsafe_allow_html=True
)

# konversi_nilai_konsentrasi = Image.open('./images/Konversi_nilai_konsentrasi.png')
konversi_nilai_konsentrasi = Image.open(Path(__file__).parents[1] / 'Web/images/Konversi_nilai_konsentrasi.png')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image(konversi_nilai_konsentrasi, caption='Konversi Nilai Konsentrasi')

with col3:
    st.write("")

st.markdown(
    """
        <div style='text-align: justify;'>
        Perhitungan ISPU dilakukan berdasarkan nilai ISPU batas atas, ISPU batas bawah, ambien batas atas, ambien batas bawah, dan konsentrasi ambien hasil pengukuran. 
        Persamaan matematika perhitungan ISPU sebagai berikut:
        </div>
    """, unsafe_allow_html=True
)

# rumus_ISPU = Image.open('./images/rumus_ISPU.png')
rumus_ISPU = Image.open(Path(__file__).parents[1] / 'Web/images/rumus_ISPU.png')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    st.image(rumus_ISPU)

with col3:
    st.write("")

st.markdown(
    """
        Keterangan:

        I = ISPU terhitung
        
        Ia = ISPU batas atas

        Ib = ISPU batas bawah

        Xa = Konsentrasi ambien batas atas (µg/m3)

        Xb = Konsentrasi ambien batas bawah (µg/m3)

        Xx = Konsentrasi ambien nyata hasil pengukuran (µg/m3)
    """
)