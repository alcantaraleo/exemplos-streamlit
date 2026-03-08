"""
Página Sobre

Esta página é pública: qualquer pessoa pode acessá-la, mesmo sem login.
Aqui ficam informações sobre o app, quem fez, versão, etc.
"""

import streamlit as st

st.set_page_config(page_title="Sobre - MVP Template", layout="wide")

st.title("Sobre")
st.write("Esta é a página **Sobre** do template MVP.")
st.markdown(
    "Aqui você pode colocar:\n"
    "- **Quem desenvolveu** o projeto\n"
    "- **Para que serve** o app\n"
    "- **Versão** do software\n"
    "- **Contato** ou links úteis"
)
st.info("Personalize este conteúdo para o seu projeto!")
st.divider()
st.write("Template MVP - exemplo educativo para crianças e adolescentes.")
