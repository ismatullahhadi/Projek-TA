# from sqlalchemy import column
import streamlit as st
import plotly_express as px
import pandas as pd
# from torch import layout
from pathlib import Path
import plotly.graph_objects as go

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# Judul Halaman
st.set_page_config(
    page_title="Regresi Data ISPU",
    page_icon="📈",
)

# title of the app
st.title("Website Visualisasi Prediksi dan Forecasting Data ISPU dengan metode GPR")

# Add a sidebar
st.sidebar.subheader("Pengaturan Visualisasi")

# Setup selecting csv file
file_select = st.sidebar.selectbox(
    label="Pilih file",
    options=[

                "Prediksi DKI1 PM10", "Prediksi DKI1 SO2", "Prediksi DKI1 CO", "Prediksi DKI1 O3", "Prediksi DKI1 NO2", "Forecasting DKI1",
                "Prediksi DKI2 PM10", "Prediksi DKI2 SO2", "Prediksi DKI2 CO", "Prediksi DKI2 O3", "Prediksi DKI2 NO2", "Forecasting DKI2",
                "Prediksi DKI3 PM10", "Prediksi DKI3 SO2", "Prediksi DKI3 CO", "Prediksi DKI3 O3", "Prediksi DKI3 NO2", "Forecasting DKI3",
                "Prediksi DKI4 PM10", "Prediksi DKI4 SO2", "Prediksi DKI4 CO", "Prediksi DKI4 O3", "Prediksi DKI4 NO2", "Forecasting DKI4",
                "Prediksi DKI5 PM10", "Prediksi DKI5 SO2", "Prediksi DKI5 CO", "Prediksi DKI5 O3", "Prediksi DKI5 NO2", "Forecasting DKI5",
            ]
)

global df

# Pemilihan file prediksi atau forecasting
if file_select == "Prediksi DKI1 PM10":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI1_01_PM10.xlsx'
elif file_select == "Prediksi DKI1 SO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI1_02_SO2.xlsx'
elif file_select == "Prediksi DKI1 CO":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI1_03_CO.xlsx'
elif file_select == "Prediksi DKI1 O3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI1_04_O3.xlsx'
elif file_select == "Prediksi DKI1 NO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI1_05_NO2.xlsx'
elif file_select == "Forecasting DKI1":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/forecasting/DKI1_Forecasting.xlsx'
if file_select == "Prediksi DKI2 PM10":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI2_01_PM10.xlsx'
elif file_select == "Prediksi DKI2 SO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI2_02_SO2.xlsx'
elif file_select == "Prediksi DKI2 CO":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI2_03_CO.xlsx'
elif file_select == "Prediksi DKI2 O3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI2_04_O3.xlsx'
elif file_select == "Prediksi DKI2 NO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI2_05_NO2.xlsx'
elif file_select == "Forecasting DKI2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/forecasting/DKI2_Forecasting.xlsx'
if file_select == "Prediksi DKI3 PM10":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI3_01_PM10.xlsx'
elif file_select == "Prediksi DKI3 SO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI3_02_SO2.xlsx'
elif file_select == "Prediksi DKI3 CO":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI3_03_CO.xlsx'
elif file_select == "Prediksi DKI3 O3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI3_04_O3.xlsx'
elif file_select == "Prediksi DKI3 NO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI3_05_NO2.xlsx'
elif file_select == "Forecasting DKI3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/forecasting/DKI3_Forecasting.xlsx'
if file_select == "Prediksi DKI4 PM10":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI4_01_PM10.xlsx'
elif file_select == "Prediksi DKI4 SO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI4_02_SO2.xlsx'
elif file_select == "Prediksi DKI4 CO":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI4_03_CO.xlsx'
elif file_select == "Prediksi DKI4 O3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI4_04_O3.xlsx'
elif file_select == "Prediksi DKI4 NO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI4_05_NO2.xlsx'
elif file_select == "Forecasting DKI4":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/forecasting/DKI4_Forecasting.xlsx'
if file_select == "Prediksi DKI5 PM10":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI5_01_PM10.xlsx'
elif file_select == "Prediksi DKI5 SO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI5_02_SO2.xlsx'
elif file_select == "Prediksi DKI5 CO":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI5_03_CO.xlsx'
elif file_select == "Prediksi DKI5 O3":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI5_04_O3.xlsx'
elif file_select == "Prediksi DKI5 NO2":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/prediction/DKI5_05_NO2.xlsx'
elif file_select == "Forecasting DKI5":
    uploaded_file = Path(__file__).parents[2] / 'Web/files/forecasting/DKI5_Forecasting.xlsx'

# # Setup file upload
# uploaded_file = st.sidebar.file_uploader(
#                         label="Upload your CSV or Excel file. (200MB max)",
#                          type=['csv', 'xlsx'])

if uploaded_file is not None:
    # print(uploaded_file)
    # print("hello")

    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_csv(uploaded_file)

global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    date_column = list(df.select_dtypes(['datetime']).columns)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    # print(non_numeric_columns)
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

# Plotting
st.sidebar.subheader("Pengaturan Plot Garis")
try:
    # Select Box dan Multiselect untuk pemilihan data atau warna yang ingin ditampilkan
    x_values = st.sidebar.selectbox('X axis', options=date_column)
    y_values = st.sidebar.multiselect('Y axis', options=numeric_columns, default=numeric_columns)
    color_values = st.sidebar.multiselect("Warna Kategori ISPU", options=["Baik", "Sedang", "Tidak Sehat", "Sangat Tidak Sehat", "Berbahaya"], default=["Baik", "Sedang"])
    
    # Keterangan DKI1 sampai DKI5
    st.sidebar.markdown(
        """
            Keterangan:\n
            DKI1 :  Bundaran HI, Jakarta, DKI Jakarta\n
            DKI2 :  Kelapa Gading, Jakarta, DKI Jakarta\n
            DKI3 :  Jagakarsa, Jakarta, DKI Jakarta\n
            DKI4 :  Lubang Buaya, Jakarta, DKI Jakarta\n
            DKI5 :  Kebon Jeruk, Jakarta, DKI Jakarta
        """
    )
    # plot = px.line(data_frame=df, x=x_values, y=[y1_values, y2_values], color=color_value)
    plot1 = px.line(data_frame=df, x=x_values, y=y_values)

    # Pembuatan Data Frame Area Kategori ISPU
    area = {"Tanggal":df["Tanggal"], "Baik":50, "Sedang":50, "Tidak Sehat":100, "Sangat Tidak Sehat":100, "Berbahaya":100}
    df_area = pd.DataFrame(area)
    # st.write(df_area)
    plot2 = px.area(data_frame=df_area, x="Tanggal", y=color_values, color_discrete_sequence=["green", "blue", "orange", "red", "gray"])
    
    # Penggabungan Plot Line dan Area
    plot3 = go.Figure(data=plot1.data + plot2.data)
    st.plotly_chart(plot3)
except Exception as e:
    print(e)
