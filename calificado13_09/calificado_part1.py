import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.datasets import load_wine
import kagglehub

st.title("Datos masivos - Matplotlib")
data_cargar = st.file_uploader("Elegir el archivo a cargar", type=["xlsx"])
data = None
if data_cargar is not None:
    data = pd.read_excel(data_cargar, sheet_name=0)
    data.dropna(inplace=True)
    st.dataframe(data)
#Verificamos si hay un archivo
x = st.text_input("X")
y = st.text_input("Y")
boton=st.button("Continuar")
if boton and data_cargar is not None:
    if x in data.columns and y in data.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=data, ax=ax, x=x, y=y)
        st.pyplot(fig)
    else:
        st.error("One or both column names are not in the dataset. Please check column names.")

