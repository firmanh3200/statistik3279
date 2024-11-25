import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly_express as px
import requests

st.set_page_config(layout='wide')

url = 'https://data.jabarprov.go.id/api-backend//bigdata/disnakertrans/od_19868_daftar_upah_minimum_kabupatenkota_di_drh_prov_jaba_v1?limit=50&skip=0&where=%7B%22nama_kabupaten_kota%22%3A%5B%22KOTA+BANJAR%22%5D%7D'

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data['data'])


# Pilihan tema warna
warna_options = {
    'Viridis_r': px.colors.sequential.Viridis_r,
    'Viridis': px.colors.sequential.Viridis,
    'Greens': px.colors.sequential.Greens,
    'Inferno': px.colors.sequential.Inferno,
    'Blues': px.colors.sequential.Blues,
    'Reds': px.colors.sequential.Reds,
    'YlGnBu': px.colors.sequential.YlGnBu,
    'YlOrRd': px.colors.sequential.YlOrRd,
    'RdBu': px.colors.diverging.RdBu,
    'Spectral': px.colors.diverging.Spectral
}

st.title("Upah Minimum Kota Banjar")
st.subheader("", divider='rainbow')

with st.container(border=True):
    fig = px.bar(df, x='tahun', y='besaran_upah_minimum', text='besaran_upah_minimum')

    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander('Lihat Tabel'):
        st.dataframe(df, hide_index=True, use_container_width=True)
        st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset/daftar-upah-minimum-kabupatenkota-di-daerah-provinsi-jawa-barat')
st.subheader("", divider='rainbow')
st.caption(':orange[Statistik Daerah Kota Banjar]')
st.caption('Hak Cipta @ :green[Badan Pusat Statistik Kota Banjar]')
