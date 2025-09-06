from os import write

import numpy as np
import nltk
import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator

nltk.download("punkt")
nltk.download("stopwords")
nltk.download('vader_lexicon')  ##SENTIMIETONS

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Practica")
st.write("pepe")
st.form(key="form", clear_on_submit=True)
options = ['Escribir', 'Hablar', 'Manual']

sia = SentimentIntensityAnalyzer()


def soutpolarity(s):
    st.write("sent token")
    st.write(sent_tokenize(s))
    st.write("word token")
    st.write(word_tokenize(s))
    st.write("sentimientos token")
    rs = sia.polarity_scores(s)
    st.write(rs)
    num = rs["compound"]
    if num>0.5:
        st.write("Compund positivo")
    elif num < 0.5:
        st.write("Compund negativo")
    else:
        st.write("Compund neutro")
def customsoutpolarity(s,f):
    f.write("sent token")
    f.write(sent_tokenize(s))
    f.write("word token")
    f.write(word_tokenize(s))
    f.write("sentimientos token")
    rs = sia.polarity_scores(s)
    f.write(rs)
    num = rs["compound"]
    if num>0.5:
        st.write("Compund positivo")
    elif num < 0.5:
        st.write("Compund negativo")
    else:
        st.write("Compund neutro")
# Estado persistente para no perder la pantalla tras click en otros botones
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "option" not in st.session_state:
    st.session_state.option = None

with st.form(key="practica"):
    option = st.selectbox("selecciona una opcion", options)

    acepta = st.form_submit_button("aceptar")
    if acepta:
        st.session_state.accepted = True
        st.session_state.option = option

if st.session_state.accepted:

    txt = st.empty()
    if st.session_state.option == 'Escribir':

        fieldstr = txt.text_area(key="es", label="Escriba", width=400, height=20)
        btn = st.empty()
        if btn.button("Hecho"):
            btn.write("Procesando")
            traduccion = GoogleTranslator(source="es", target="en").translate(fieldstr)
            st.session_state.traduccion = traduccion
            btn.text_area(key="en", label="Traduccion", width=400, height=20, value=st.session_state.traduccion)


            soutpolarity(traduccion)

    elif st.session_state.option == 'Hablar':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            txt.write("Escuchando...")
            audio = r.listen(source)
            txt.write("Procesando...")
            audiostr = r.recognize_google(audio, language="es-ES")
            txt.write(audiostr)
            traduccion = GoogleTranslator(source="es", target="en").translate(audiostr)
            st.write(traduccion)
            soutpolarity(traduccion)
    else :
        col1, col2, col3 = st.columns(3)
        data = [
            "Estoy feliz por tu éxito, aunque siento un poco de envidia.",
            "Me duele que te hayas ido, pero entiendo que era lo mejor para ti.",
            "Me encanta trabajar en este proyecto, aunque me siento agotado."
        ]
        customsoutpolarity(data[0],col1)
        customsoutpolarity(data[1],col2)
        customsoutpolarity(data[2],col3)
