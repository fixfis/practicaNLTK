import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.datasets import load_wine
import kagglehub

st.title("calif2")

col1, col2 = st.columns(2)


data = sns.load_dataset("penguins")
data.dropna(inplace=True)
fig, ax = plt.subplots(1,3,figsize=(13,5))
sns.barplot(data=data, ax=ax[0], x="species",y="body_mass_g")
with col1:
    st.write("Specie-bodymass-mean")
    st.dataframe(data)


df = data["island"].value_counts()
labels= ["Biscoe","Dream","Torgersen"]
ax[1].pie(df,labels=labels)
with col2:
    st.write("Pastel")
    st.write(df)



ax[2] =sns.histplot(data=data,x="flipper_length_mm")
st.pyplot(fig)


st.title("calif seaborn")

data = sns.load_dataset("penguins")
data.dropna(inplace=True)
fig, ax = plt.subplots(1,3,figsize=(18,5))


sns.scatterplot(data=data, x="bill_length_mm", y="bill_depth_mm", hue="species",ax=ax[0])

sns.boxplot(data=data, x="body_mass_g", y="sex",ax=ax[1])

sns.lineplot(data=data, x="body_mass_g", y="sex",ax=ax[2])


col1, col2,col3 = st.columns(3)
with col1:
    st.write("-	Crear un gráfico de dispersión (scatterplot) entre bill_length_mm y bill_depth_mm, diferenciando por especie.")
with col2:
    st.write("-	Crear un gráfico de cajas (boxplot) de la masa corporal (body_mass_g) por sexo. ")
with col3:
    st.write("-	Crear un gráfico de líneas (lineplot) de la masa corporal (body_mass_g) por sexo.")



st.pyplot(fig)



with st.form("prat"):
    lista = list(set(data["species"]))
    option = st.selectbox("Seleccione",options=lista)
    if st.form_submit_button("ver"):
        data = data[data["species"] == option]
        st.dataframe(data)
        fig, ax = plt.subplots(figsize=(18, 5))
        sns.barplot(data=data, x="bill_length_mm", y="bill_depth_mm")
        st.pyplot(fig)



