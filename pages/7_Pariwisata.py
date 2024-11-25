import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.title('Statistik Pariwisata Kota Banjar')
st.subheader('', divider='rainbow')

data = pd.read_excel('data/pariwisata.xlsx')
data['Tahun'] = data['Tahun'].astype(str)

with st.expander('METODOLOGI'):
    tab1, tab2, tab3 = st.tabs(['Konsep', 'Definisi', 'Metode Penghitungan'])

kol1a, kol1b = st.columns(2)
with kol1a:
    with st.container(border=True):
        st.success('Tingkat Penghunian Kamar (TPK) Hotel Kota Banjar')
        grafik1 = px.bar(data, x='Kategori', y='TPK', barmode='group',
                         text='TPK', color='Tahun')
        
        # Menempatkan legenda di bawah grafik
        grafik1.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title_text=''
        ))
        
        st.plotly_chart(grafik1, use_container_width=True)

with kol1b:
    with st.container(border=True):
        st.info('Tingkat Pemakaian Tempat Tidur (TPTT) Hotel Kota Banjar')
        grafik2 = px.bar(data, x='Kategori', y='TPTT', barmode='group',
                          text='TPTT', color='Tahun')
        
        # Menempatkan legenda di bawah grafik
        grafik2.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title_text=''
        ))
        
        st.plotly_chart(grafik2, use_container_width=True)

with st.expander('Rata-rata Lama Menginap Tamu'):        
    kol2a, kol2b, kol2c = st.columns(3)
    with kol2a:
        with st.container(border=True):
            st.success('Rata-rata Lama Menginap Tamu Asing (RLMTA) di Hotel Kota Banjar')
            grafik3 = px.bar(data, x='Kategori', y='RLMTA', barmode='group',
                            text='RLMTA', color='Tahun')
            
            # Menempatkan legenda di bawah grafik
            grafik3.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik3, use_container_width=True)

    with kol2b:
        with st.container(border=True):
            st.info('Rata-rata Lama Menginap Tamu (RLMT) di Hotel Kota Banjar')
            grafik4 = px.bar(data, x='Kategori', y='RLMT', barmode='group',
                            text='RLMT', color='Tahun')
            
            # Menempatkan legenda di bawah grafik
            grafik4.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik4, use_container_width=True)

    with kol2c:
        with st.container(border=True):
            st.success('Rata-rata Lama Menginap Tamu Dalam Negeri (RLMTD) di Hotel Kota Banjar')
            grafik5 = px.bar(data, x='Kategori', y='RLMTD', barmode='group',
                            text='RLMTD', color='Tahun')
            
            # Menempatkan legenda di bawah grafik
            grafik5.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik5, use_container_width=True)

with st.expander('Jumlah Tamu'):
    kol3a, kol3b = st.columns(2)
    with kol3a:
        with st.container(border=True):
            st.success('Jumlah Tamu Asing - Hotel Kota Banjar')
            grafik6 = px.bar(data, x='Kategori', y='Tamu Asing', barmode='group',
                            text='Tamu Asing', color='Tahun')
            
            # Menempatkan legenda di bawah grafik
            grafik6.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik6, use_container_width=True)

    with kol3b:
        with st.container(border=True):
            st.info('Jumlah Tamu Dalam Negeri - Hotel Kota Banjar')
            grafik7 = px.bar(data, x='Kategori', y='Tamu Domestik', barmode='group',
                            text='Tamu Domestik', color='Tahun')
            
            # Menempatkan legenda di bawah grafik
            grafik7.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.3,
                xanchor="center",
                x=0.5,
                title_text=''
            ))
            
            st.plotly_chart(grafik7, use_container_width=True)
        
with st.expander('Lihat Tabel Lengkap'):
    st.warning('Statistik Pariwisata Kota Banjar')
    df = data.sort_values(by='Tahun', ascending=False)
    st.dataframe(df, hide_index=True, use_container_width=True)
    
st.subheader('', divider='rainbow')
st.caption(':orange[Statistik Daerah Kota Banjar]')
st.caption('Hak Cipta @ :green[BPS Kota Banjar]')