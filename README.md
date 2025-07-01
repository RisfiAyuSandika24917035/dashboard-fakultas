# Dashboard Fakultas Sains dan Teknologi – Universitas Kartama
Dashboard ini menggunakan **Streamlit** untuk memvisualisasikan data akademik Fakultas Sains dan Teknologi Universitas Kartama. Dashboard ini membantu pimpinan fakultas seperti Dekan, Wakil Dekan, dan Ketua Program Studi untuk mendapatkan insight dan mengambil keputusan.

# Struktur File

| Nama File               | Deskripsi                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `dashboard_fakultas.py`| Script utama untuk menjalankan aplikasi dashboard di Streamlit            |
| `data_dashboard.xlsx`  | Data simulasi yang digunakan untuk ditampilkan dalam dashboard             |
| `requirements.txt`     | Daftar pustaka Python yang dibutuhkan                                      |
| `README.md`            | Dokumentasi cara menjalankan proyek                                       |

# Cara Menjalankan Proyek Melalui Streamlit Cloud

1. Clone repository ini.
2. Buka [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Login dengan akun GitHub.
4. Klik **"New App"** → pilih repositori ini.
5. Isi:
   - **Main file path:** `dashboard_fakultas.py`
   - Klik **Deploy**


# Install dependency
pip install -r requirements.txt

# Jalankan Streamlit
streamlit run dashboard_fakultas.py
