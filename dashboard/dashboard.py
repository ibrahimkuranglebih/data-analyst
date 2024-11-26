import pandas as pd
import numpy as num
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st


st.title("Analisis Data Air Quality Dataset :cityscape:")

#gathering data
df_aothi = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
df_changping = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv')
df_dingling = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv')
df_dongsi = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv')
df_guanyuan = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv')
df_gucheng = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv')
df_huairou = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv')
df_nongzhanguan = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv')
df_shunyi = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv')
df_tiantan = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv')
df_wanliu = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv')
df_wanshouxigong = pd.read_csv('../Air-quality-dataset/PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv')

#asessing data

#cleaning data
df_aothi.drop_duplicates(inplace=True)
print(df_aothi.duplicated().sum())

df_aothi.isna().sum()
df_aothi.fillna(value=0, inplace=True)
df_aothi.isna().sum()

df_changping.drop_duplicates(inplace=True)
print(df_changping.duplicated().sum())

df_changping.isna().sum()
df_changping.fillna(value=0, inplace=True)
df_changping.isna().sum()

df_dingling.drop_duplicates(inplace=True)
print(df_dingling.duplicated().sum())

df_dingling.isna().sum()
df_dingling.fillna(value=0, inplace=True)
df_dingling.isna().sum()

df_dongsi.drop_duplicates(inplace=True)
print(df_dongsi.duplicated().sum())

df_dongsi.isna().sum()
df_dongsi.fillna(value=0, inplace=True)
df_dongsi.isna().sum()

df_guanyuan.drop_duplicates(inplace=True)
print(df_guanyuan.duplicated().sum())

df_guanyuan.isna().sum()
df_guanyuan.fillna(value=0, inplace=True)
df_guanyuan.isna().sum()

df_gucheng.drop_duplicates(inplace=True)
print(df_gucheng.duplicated().sum())

df_gucheng.isna().sum()
df_gucheng.fillna(value=0, inplace=True)
df_gucheng.isna().sum()

df_huairou.drop_duplicates(inplace=True)
print(df_huairou.duplicated().sum())

df_huairou.isna().sum()
df_huairou.fillna(value=0, inplace=True)
df_huairou.isna().sum()

df_nongzhanguan.drop_duplicates(inplace=True)
print(df_nongzhanguan.duplicated().sum())

df_nongzhanguan.isna().sum()
df_nongzhanguan.fillna(value=0, inplace=True)
df_nongzhanguan.isna().sum()

df_shunyi.drop_duplicates(inplace=True)
print(df_shunyi.duplicated().sum())

df_shunyi.isna().sum()
df_shunyi.fillna(value=0, inplace=True)
df_shunyi.isna().sum()

df_tiantan.drop_duplicates(inplace=True)
print(df_tiantan.duplicated().sum())

df_tiantan.isna().sum()
df_tiantan.fillna(value=0, inplace=True)
df_tiantan.isna().sum()

df_wanliu.drop_duplicates(inplace=True)
print(df_wanliu.duplicated().sum())

df_wanliu.isna().sum()
df_wanliu.fillna(value=0, inplace=True)

df_wanliu.isna().sum()

df_wanshouxigong.drop_duplicates(inplace=True)
print(df_wanshouxigong.duplicated().sum())

df_wanshouxigong.isna().sum()
df_wanshouxigong.fillna(value=0, inplace=True)
df_wanshouxigong.isna().sum()


tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1 :
    st.header("Jenis Polutan Tertinggi di Tiap Kota")
    col1,col2 = st.columns(2)
    colors = ["#D3D3D3", "#D3D3D3","#D3D3D3","#D3D3D3", "#90CAF9", "#D3D3D3"]
    with col1 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_aothi_poluted = df_aothi[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Aotizhongxin",  fontsize=40)
        sns.barplot(
        data=df_aothi_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col2 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_changping_poluted = df_changping[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Changping", fontsize=40)
        sns.barplot(
        data=df_changping_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    col3,col4 = st.columns(2)
    with col3 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_dingling_poluted = df_dingling[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Dingling", fontsize=40)
        sns.barplot(
        data=df_dingling_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col4 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_dongsi_poluted = df_dongsi[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Dongsi", fontsize=40)
        sns.barplot(
        data=df_dongsi_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    col5,col6 = st.columns(2)

    with col5 : 
        fig, ax = plt.subplots(figsize=(20, 10))
        df_guanyuan_poluted = df_guanyuan[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Guanyuan", fontsize=40)
        sns.barplot(
        data=df_guanyuan_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col6 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_gucheng_poluted = df_gucheng[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Gucheng", fontsize=40)
        sns.barplot(
        data=df_gucheng_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)

    col7,col8 = st.columns(2)
    with col7 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_huairou_poluted = df_huairou[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Huairou", fontsize=40)
        sns.barplot(
        data=df_huairou_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col8 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_nongzhanguan_poluted = df_nongzhanguan[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Nongzhanguan", fontsize=40)
        sns.barplot(
        data=df_nongzhanguan_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    col9,col10 = st.columns(2)

    with col9 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_shunyi_poluted = df_shunyi[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Shunyi", fontsize=40)
        sns.barplot(
        data=df_shunyi_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col10 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_tiantan_poluted = df_tiantan[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Tiantan", fontsize=40)
        sns.barplot(
        data=df_tiantan_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    col11,col12 = st.columns(2)
    with col11 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_wanliu_poluted = df_wanliu[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Wanliu", fontsize=40)
        sns.barplot(
        data=df_wanliu_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with col12 :
        fig, ax = plt.subplots(figsize=(20, 10))
        df_wanshouxigong_poluted = df_wanshouxigong[['PM2.5', 'PM10','SO2','NO2','CO','O3']]
        ax.set_title("Polutan Terbanyak di Kota Wanshouxigong", fontsize=40)
        sns.barplot(
        data=df_wanshouxigong_poluted,
        palette = colors,
        ax = ax
        )
        ax.set_ylabel(None)
        ax.set_xlabel(None)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        st.pyplot(fig)
        
    with st.expander("Kesimpulan Pertanyaan 1") :
        st.write(
            "Polusi terbanyak di tiap kota yaitu Karbon Monoksida (CO)"
        )
        
with tab2 :
    st.header("Grafik Perkembangan Tiap Polutan di Kota Aotizhongxin Tiap Tahun")

    pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

    grouped_data = df_aothi.groupby('year')[pollutants].mean()

    fig, ax = plt.subplots(figsize=(12, 6))

    for pollutant in pollutants:
        ax.plot(grouped_data.index, grouped_data[pollutant], marker='o', label=pollutant)

    ax.set_title('Rata-Rata Tiap Polutan per Tahun di Kota Aotizhongxin', fontsize=16)
    ax.set_xlabel('Tahun', fontsize=14)
    ax.set_ylabel('Konsentrasi Rata-Rata', fontsize=14)
    ax.legend(title="Polutan")
    ax.grid(True)
    st.pyplot(fig)

    with st.expander("Kesimpulan Pertanyaan 2"):
        st.write(
            "Polutan yang mengalami perkembangan Peningkatan tertinggi di Kota Aotizhongxin yaitu Karbon Monoksida (CO) pada tahun 2016 ke 2017."
        )