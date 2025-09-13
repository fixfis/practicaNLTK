#Para correr en la web de streamlit es este comando.(python -m streamlit run app.py)
#Importar las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.datasets import load_wine # Vinos

#
st.title("Matplotlib")

#Datos
X = ["Python", "JavaScript", "Php", "Laravel", "C#"]
Y = [25,40,22,28,30]

#Graficamos => plot
fig,ax= plt.subplots()
ax.plot(X,Y, marker="o", color="blue", label="Cursos")
ax.set(
    title="Participantes en los cursos digitales",
    xlabel = "Cursos",
    ylabel = "Cantidad"
)
ax.legend()
st.pyplot(fig) #Mostrar en streamlit -> web

################# CARGAR EL ARCHIVO ###################
st.title("Datos masivos - Matplotlib")
data_cargar = st.file_uploader("Elegir el archivo a cargar", type=["xlsx"])
#Verificamos si hay un archivo
if data_cargar is not None:
    data = pd.read_excel(data_cargar, sheet_name=0)
    st.dataframe(data)
#Grafico sactter = dispersion
    fig,ax = plt.subplots()
    ax.scatter(data["edad"],data["glucosa"],label="glu")
    ax.scatter(data["edad"],data["presion_arterial"],label="par")
    ax.set(
        title = "IMC de una Persona",
        xlabel = "Edad",
        ylabel = "glu/par"
    )
    ax.legend()
    st.pyplot(fig)

    #Grafico de barras
    fig,ax = plt.subplots()
    ax.bar(data["edad"],data["glucosa"])
    ax.set(
        title = "Edad/ Glucosa",
        xlabel = "Edad",
        ylabel = "Glucosa"
    )
    st.pyplot(fig)

    #Graficos de circular
    fig,ax = plt.subplots()
    ax.pie(data["diabetes"])
    st.pyplot(fig)

############### DATASET ######################
data = load_wine()
#st.dataframe(data.data)
#st.dataframe(data.target)
#Grafico
fig,ax = plt.subplots()
ax.plot(data.data,label= data.feature_names)
ax.legend()
st.pyplot(fig)


################## SEABORN ####################
#cargar un dataset

data1 = sns.load_dataset("tips")
st.title("SEABORN - DATASET tips")
#Cargar los datos
st.dataframe(data1.head())
#Mostrar graficos scatterplot
fig,ax = plt.subplots()
sns.scatterplot(x="total_bill",y="tip",hue="sex",data=data1,ax=ax)
ax.set(
    title ="Dispersion de propinas en relacion a la factura",
    xlabel = "Total de factura",
    ylabel = "Propina"
)
st.pyplot(fig)

fig = plt.boxplot(data1.total_bill)
st.pyplot(fig)


