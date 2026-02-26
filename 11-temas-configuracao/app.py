"""
Temas e configuração no Streamlit

Este exemplo mostra um app com tema personalizado (cores).
As cores são definidas no arquivo .streamlit/config.toml.
Aqui no código só mostramos conteúdo; o tema deixa a página mais atrativa.
"""

import streamlit as st

st.set_page_config(page_title="Temas e cores", layout="wide")
st.title("App com tema colorido")
st.write(
    "As cores deste app foram configuradas no arquivo **.streamlit/config.toml**. "
    "Assim o app fica mais divertido e fácil de identificar."
)
st.info(
    "Para mudar as cores, edite o arquivo config.toml na pasta .streamlit. "
    "Você pode escolher primaryColor, backgroundColor e outras opções."
)
