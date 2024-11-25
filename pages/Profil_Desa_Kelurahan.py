import streamlit as st
import pandas as pd
import requests
import lxml

# Function to fetch data from URL based on selected code
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_html(response.text)  # Read HTML tables from the response
        return data[0]  # Assuming the data is in the first table
    else:
        st.error("Gagal mengambil data. Status code: {}".format(response.status_code))
        return None

def kamus():
    mfd3200 = pd.read_csv('data/mfd2023.csv', sep=',', encoding='utf-8')
    
    mendagri = pd.read_csv('data/kdkec_mendagri.csv', sep=',', encoding='utf-8')
    
    return mfd3200, mendagri
mfd3200, mendagri = kamus()

# Main Streamlit app
def main():
    st.header("DATA POKOK DESA/KELURAHAN", divider='rainbow')
    st.success("Sumber: e-prodeskel Kemendagri")
    with st.expander("Referensi IDDESA"):
        mfd2 = pd.read_csv('data/mfd_23_1_32.csv', 
                            dtype={'kdkab':'str', 'kdkec':'str', 'kddesa':'str', 'iddesa':'str'})
        mfd32 = mfd2[mfd2['kdkab'] == '79']
        
        kolom1, kolom2 = st.columns(2)
        with kolom1:
            datakab = mfd32['nmkab'].unique().tolist()
            kabterpilih = st.selectbox("Filter Kabupaten/Kota", datakab, key='namakabkot')
        with kolom2:
            datakec = mfd32[mfd32['nmkab'] == kabterpilih]['nmkec'].unique().tolist()
            kecterpilih = st.selectbox("Filter Kecamatan", datakec, key='namakec')
        if kolom1 and kolom2:
            with st.container(border=True):
                tabelmfd = mfd32[(mfd32['nmkab'] == kabterpilih) & (mfd32['nmkec'] == kecterpilih)]
                st.dataframe (tabelmfd, hide_index=True, use_container_width=True)
    
    st.subheader("", divider='green')
            
    with st.container(border=True):
        kol1, kol2, kol3 = st.columns(3)
        with kol1:
            mfd = mfd3200[mfd3200['idkab'] == 3279]
            kabkot = mfd['idkab'].unique().tolist()
            kabterpilih1 = st.selectbox("Filter IDKAB", kabkot, key='kabkot1')
        with kol2:
            kec = mfd[mfd['idkab'] == kabterpilih1]['idkec'].unique().tolist()
            kecterpilih1 = st.selectbox("Filter IDKEC", kec, key='kec1')
        with kol3:
            desa = mfd[mfd['idkec'] == kecterpilih1]['iddesa'].unique().tolist()
            desaterpilih = st.selectbox("Filter IDDESA", desa, key='desa1')    
            
        if kol1 and kol2 and kol3:
            url = f"https://e-prodeskel.kemendagri.go.id/datapokok/data.php?kodesa={desaterpilih}"

            # Fetch data based on selected code
            tables = pd.read_html(url)

            df0 = tables[0]
            df1 = tables[1]
            df2 = tables[2]
            df3 = tables[3]
            #df4 = tables[4]

            tabel0 = pd.DataFrame(df0)
            tabel1 = pd.DataFrame(df1)
            tabel2 = pd.DataFrame(df2)
            tabel3 = pd.DataFrame(df3)
            #tabel4 = pd.DataFrame(df4)

            gabungan = pd.concat([tabel0, tabel1, tabel2, tabel3], axis=1)
            
            st.dataframe(tabel0, use_container_width=True, hide_index=True)
            st.dataframe(tabel1, use_container_width=True, hide_index=True)
            st.dataframe(tabel2, use_container_width=True, hide_index=True)
            st.dataframe(tabel3, use_container_width=True, hide_index=True)
            #st.dataframe(tabel4, use_container_width=True, hide_index=True)
    
    st.link_button("Lihat Sumber Data", url=f"https://e-prodeskel.kemendagri.go.id/datapokok/data.php?kodesa={desaterpilih}")


    st.subheader('', divider='rainbow')
    st.caption(':orange[Statistik Daerah Kota Banjar]')
    st.caption('Hak Cipta @ :green[BPS Kota Banjar]')

if __name__ == '__main__':
    main()
