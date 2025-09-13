import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from sklearn.datasets import load_wine


data = sns.load_dataset("titanic")
st.dataframe(data.head())

fig,ax = plt.subplots(1,2, figsize=(10,5))
sns.scatterplot(data=data,ax=ax[0],x="age",y="fare")
ax[0].set(
    title="Dispersion de propinas en relacion a la edad",
    xlabel = "Edad",
    ylabel = "Tarifa"
)

sns.lineplot(data=data,ax=ax[1],x="survived",y="sex")
ax[1].set(
    title="Dispersion de propinas en relacion a la edad",
    xlabel = "vivo",
    ylabel = "sexo"
)

st.pyplot(fig)
