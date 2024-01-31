import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

dataframe = pd.read_csv('bd.csv', sep=';', decimal=',' , encoding='latin-1', index_col=0)



st.set_page_config(
    page_title="Psicologa Natalia",
    page_icon=":bar_chart",
    layout="wide",
    initial_sidebar_state='collapsed'
)

dataframe.reset_index(inplace=True)

MES = st.sidebar.multiselect(
    key=1,
    label="MES",
    options=dataframe['MES'].unique(),
    default=dataframe['MES'].unique()
)

CATEGORIA = st.sidebar.multiselect(
    key=2,
    label="CATEGORIA",
    options=dataframe['CATEGORIA'].unique(),
    default=dataframe['CATEGORIA'].unique()
)

ITEM = st.sidebar.multiselect(
    key=3,
    label="ITEM",
    options=dataframe['ITEM'].unique(),
    default=dataframe['ITEM'].unique()
)

dataframe = dataframe.query("MES == @MES and CATEGORIA == @CATEGORIA and ITEM == @ITEM")



st.header(":bar_chart: Controle de Consultas e Despesas")
st.markdown("""---""")

col1, col2 = st.columns(2)

total_saida = round(dataframe["SAIDA"].sum(),2)
total_entrada = round(dataframe["ENTRADA"].sum(),2)

grafico = (dataframe.groupby("MES").sum(numeric_only=True)
           [["SAIDA"]].sort_values("MES"))

#####Grafico#####
linha = px.area(
    grafico,

)
#################

col1.metric("Total Entrada", total_entrada)
col2.metric("Total da Saida", total_saida)

st.plotly_chart(linha)

st.dataframe(dataframe)
