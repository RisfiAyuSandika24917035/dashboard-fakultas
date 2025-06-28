import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

st.set_page_config(layout="wide")
st.title("Dashboard Fakultas Universitas")

# Load Excel
xlsx = pd.ExcelFile("data_dashboard.xlsx")

# Baca semua sheet
df_aktif = pd.read_excel(xlsx, "Mahasiswa Aktif")
df_lulusan = pd.read_excel(xlsx, "Lulusan per Semester")
df_waktu = pd.read_excel(xlsx, "Waktu Tempuh Studi")
df_akreditasi = pd.read_excel(xlsx, "Status Akreditasi")
df_prodi = pd.read_excel(xlsx, "Prodi Aktif")
df_distribusi = pd.read_excel(xlsx, "Distribusi Mahasiswa")
df_kuesioner = pd.read_excel(xlsx, "Kuesioner Dosen")

# Sidebar: filter tahun
tahun_opsi = sorted(df_aktif["Tahun"].dropna().unique())
tahun_pilih = st.sidebar.selectbox("Pilih Tahun", tahun_opsi)

# === Jumlah Mahasiswa Aktif ===
st.subheader("Jumlah Mahasiswa Aktif per Program Studi")
aktif = df_aktif[df_aktif["Tahun"] == tahun_pilih]
st.bar_chart(data=aktif, x="Program Studi", y="Jumlah Mahasiswa")

# === Lulusan per Semester ===
st.subheader("Jumlah Lulusan per Semester")
lulusan = df_lulusan[df_lulusan["Tahun"] == tahun_pilih]
st.line_chart(data=lulusan, x="Program Studi", y="Jumlah Lulusan")

# === Waktu Tempuh Studi ===
st.subheader("Rata-rata Waktu Tempuh Studi Mahasiswa")

df_waktu["Waktu Tempuh (Tahun)"] = df_waktu["Rata-rata Tahun"] + (df_waktu["Rata-rata Bulan"] / 12)
tabel = df_waktu[["Program Studi", "Jenjang", "Waktu Tempuh (Tahun)"]]
st.dataframe(tabel.style.background_gradient(subset=["Waktu Tempuh (Tahun)"], cmap="Blues"))

# === Status Akreditasi ===
st.subheader("Status Akreditasi Program Studi")
st.dataframe(df_akreditasi)

# === Jumlah Prodi Aktif ===
st.subheader("Jumlah Program Studi Aktif per Jenjang")
st.bar_chart(data=df_prodi, x="Jenjang", y="Jumlah Prodi Aktif")

# === Distribusi Mahasiswa ===
st.subheader("Distribusi Mahasiswa per Jenjang dan Tahun")
distribusi = df_distribusi[df_distribusi["Tahun"] == tahun_pilih]
fig_pie = px.pie(
    distribusi,
    names="Jenjang",
    values="Jumlah Mahasiswa",
    title=f"Distribusi Mahasiswa Tahun {tahun_pilih}",
    hole=0.4
)
st.plotly_chart(fig_pie, use_container_width=True)

# === Kuesioner Dosen ===
st.subheader("Rata-rata Skor Penilaian Dosen oleh Mahasiswa")
kues = df_kuesioner[df_kuesioner["Tahun"] == tahun_pilih].copy()
kues["Rata-rata Skor Penilaian Dosen (1-5)"] = (
    kues["Rata-rata Skor Penilaian Dosen (1-5)"]
    .astype(str).str.replace(",", ".").astype(float)
)

prodi_list = kues["Program Studi"].unique().tolist()
prodi_pilih = st.selectbox("Pilih Program Studi", ["Semua"] + prodi_list)

if prodi_pilih != "Semua":
    kues = kues[kues["Program Studi"] == prodi_pilih]

chart = alt.Chart(kues).mark_bar().encode(
    x=alt.X("Rata-rata Skor Penilaian Dosen (1-5):Q", scale=alt.Scale(domain=[1, 5])),
    y=alt.Y("Program Studi:N", sort='-x')
).properties(width=700)

st.altair_chart(chart, use_container_width=True)

st.caption("Sumber data: Simulasi internal")
