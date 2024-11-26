import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(layout='wide')

st.title(':orange[STATISTIK] :blue[KEPENDUDUKAN] :green[KOTA BANJAR]')

st.subheader('', divider='rainbow')

# Menampilkan grafik tahunan
with st.container(border=True):
    # URL API Open Data
    url = "https://data.jabarprov.go.id/api-backend//bigdata/disdukcapil_2/od_17892_jml_penduduk__jk_kabupatenkota?limit=100&skip=0&where=%7B%22nama_kabupaten_kota%22%3A%5B%22KOTA+BANJAR%22%5D%7D"

    # Fungsi untuk mengambil data
    response = requests.get(url)
    data = response.json()

    # Mengubah data menjadi pandas dataframe
    df = pd.DataFrame(data['data'])

    df_total = df.groupby(['nama_kabupaten_kota', 'tahun'])['jumlah_penduduk'].sum().reset_index()

    st.subheader('Perkembangan Jumlah Penduduk Kota Banjar')
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Total', 'Jenis Kelamin', 'Status Kawin', 'Kecamatan', 'Desa/Kelurahan', 'Umur'])
    
    fig1 = px.bar(df_total, x='tahun', y='jumlah_penduduk', text='jumlah_penduduk')
    fig2 = px.bar(df, x='tahun', y='jumlah_penduduk', color='jenis_kelamin', 
                  text='jumlah_penduduk')
    
    # Menempatkan legenda di bawah grafik
    fig2.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        title_text=''
    ))
    
    with tab1:
        st.plotly_chart(fig1, use_container_width=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset/jumlah-penduduk-berdasarkan-jenis-kelamin-dan-kabupatenkota-di-jawa-barat')

    with tab2:
        st.plotly_chart(fig2, use_container_width=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset/jumlah-penduduk-berdasarkan-jenis-kelamin-dan-kabupatenkota-di-jawa-barat')

    
    # PENDUDUK STATUS KAWIN        
    with tab3:
        st.subheader('Penduduk Kota Banjar menurut Status Kawin')
        url4 = 'https://data.jabarprov.go.id/api-backend//bigdata/disdukcapil_2/od_15135_jumlah_penduduk_berdasarkan_status_perkawinan_v1?limit=3000&skip=0&where=%7B%22nama_kabupaten_kota%22%3A%5B%22KOTA+BANJAR%22%5D%7D'

        response4 = requests.get(url4)
        data4 = response4.json()
        
        df4 = pd.DataFrame(data4['data'])
        
        fig4 = px.bar(df4, x='tahun', y='jumlah_penduduk', text='jumlah_penduduk', 
                      color='status_kawin')
        
        # Menempatkan legenda di bawah grafik
        fig4.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title_text=''
        ))
        
        st.plotly_chart(fig4, use_container_width=True, hide_index=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df4, use_container_width=True, hide_index=True)
            st.caption('Sumber: https://opendata.jabarprov.go.id/id/dataset/jumlah-penduduk-berdasarkan-status-perkawinan-di-jawa-barat')
    
    # PENDUDUK KELURAHAN DAN JENIS KELAMIN
    url5 = 'https://opendata.banjarkota.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jmlh-pnddk-mnrt-jns-klmn-pr-ds-klrhn-kt-bnjr?sort=id%3Aasc&page=1&per_page=600&where=%7B%7D&where_or=%7B%7D'
    
    # Fungsi untuk mengambil data
    response5 = requests.get(url5)
    data5 = response5.json()

    # Mengubah data menjadi pandas dataframe
    df5 = pd.DataFrame(data5['data'])
    
    # PENDUDUK MENURUT KECAMATAN
    with tab4:
        st.subheader('Penduduk Kota Banjar menurut kecamatan')
        
        df5a = df5.groupby(['kemendagri_nama_kecamatan', 'tahun'])['jumlah_penduduk'].sum().reset_index()
        
        fig5 = px.bar(df5a, x='tahun', y='jumlah_penduduk', text='jumlah_penduduk', 
                      color='kemendagri_nama_kecamatan')
        
        # Menempatkan legenda di bawah grafik
        fig5.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title_text=''
        ))
        
        st.plotly_chart(fig5, use_container_width=True, hide_index=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df5a, use_container_width=True, hide_index=True)
            st.caption('Sumber: https://opendata.banjarkota.go.id/dataset/jumlah-penduduk-menurut-jenis-kelamin-per-desa-kelurahan-kota-banjar')
    
    # PENDUDUK MENURUT DESA
    with tab5:
        st.subheader('Penduduk Kota Banjar menurut desa/kelurahan')
        
        df6 = df5.groupby(['kemendagri_nama_kecamatan', 'kemendagri_nama_desa_kelurahan', 'tahun'])['jumlah_penduduk'].sum().reset_index()
        
        fig6 = px.bar(df6, x='tahun', y='jumlah_penduduk', text='jumlah_penduduk', 
                      color='kemendagri_nama_desa_kelurahan')
        
        # Menempatkan legenda di bawah grafik
        fig6.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            title_text=''
        ))
        
        st.plotly_chart(fig6, use_container_width=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df6, use_container_width=True, hide_index=True)
            st.caption('Sumber: https://opendata.banjarkota.go.id/dataset/jumlah-penduduk-menurut-jenis-kelamin-per-desa-kelurahan-kota-banjar')
    
    # PENDUDUK UMUR
    with tab6:
        url3 = 'https://opendata.banjarkota.go.id/api/bigdata/dinas_kependudukan_dan_pencatatan_sipil/jumlah_penduduk_menurut_kelompok_umur_jk_di_kota_banjar'
        
        # Fungsi untuk mendapatkan data dari setiap halaman
        def get_data(url, page):
            response = requests.get(url, params={'page': page})
            return response.json()

        # Menggabungkan semua data dari setiap halaman
        all_data = []
        page = 1
        while True:
            data = get_data(url3, page)
            all_data.extend(data['data'])
            if not data['pagination']['has_next']:
                break
            page += 1

        df3 = pd.DataFrame(all_data)
        
        df3['kelompok_umur'] = df3['kelompok_umur'].replace({'0 – 4':'00 - 04', '5 – 9':'05 - 09'})
        df3 = df3.sort_values(by=['tahun', 'kelompok_umur'], ascending=[False, True])
        
        tahun = df3['tahun'].unique()
        
        pilihan = st.selectbox('Filter Tahun', tahun)
        
        if pilihan:
            st.subheader(f'Penduduk Kota Banjar menurut Kelompok Umur Tahun {pilihan}')
        
            df_tahun = df3[df3['tahun'] == pilihan]
            piramida = df_tahun.pivot_table(index='kelompok_umur', columns='jenis_kelamin', values='jumlah_penduduk')
            piramida = piramida.reset_index()
            
            piramida['LAKI-LAKI'] = -piramida['LAKI-LAKI']
            
            kol1, kol2 = st.columns(2)
            with kol1:
                grafik = px.bar(piramida, x=['LAKI-LAKI', 'PEREMPUAN'], y='kelompok_umur')
                
                # Menempatkan legenda di bawah grafik
                grafik.update_layout(legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=-0.3,
                    xanchor="center",
                    x=0.5,
                    title_text=''
                ))
                st.plotly_chart(grafik, use_container_width=True)
            
            with kol2:
                fig3 = px.sunburst(df_tahun, path=['nama_kabupaten_kota', 'kelompok_umur', 'jenis_kelamin'],
                            values='jumlah_penduduk')

                st.plotly_chart(fig3, use_container_width=True)
                
            fig3a = px.treemap(df_tahun, path=['nama_kabupaten_kota', 'kelompok_umur', 'jenis_kelamin'],
                            values='jumlah_penduduk')

            st.plotly_chart(fig3a, use_container_width=True)
        
        with st.expander('Lihat Tabel'):
            st.dataframe(df3, use_container_width=True, hide_index=True)

            st.caption('Sumber: https://opendata.banjarkota.go.id/dataset/jumlah-penduduk-menurut-kelompok-umur-dan-jenis-kelamin-di-kota-banjar')
    
     
    
    
st.subheader('', divider='rainbow')
st.caption(':orange[Statistik Daerah Kota Banjar]')
st.caption('Hak Cipta @ :green[BPS Kota Banjar]')