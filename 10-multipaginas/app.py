"""
App com várias páginas (multipage)

Este é o arquivo principal. Ele é a página inicial (Home) do app.
As outras páginas ficam na pasta "pages/". O Streamlit coloca
links para cada arquivo da pasta "pages/" no menu lateral.
"""

import streamlit as st

st.set_page_config(page_title="App multipáginas", layout="wide")

# 3. Exibir resultado
st.title("Página inicial")
st.write(
    "Bem-vindo! Este app tem várias páginas. "
    "Olhe no menu à esquerda: você verá **Sobre** e **Contato**. "
    "Clique em cada um para ir para essa página."
)
st.info("A pasta 'pages/' contém os arquivos que viram páginas no menu.")
