"""
Aplicativo de teste – Instalação do Streamlit

Este arquivo é bem simples. Ele só mostra uma mensagem na tela
para você conferir se o Python e o Streamlit foram instalados corretamente.

Como rodar:
    streamlit run app.py
"""

import streamlit as st

# 3. Exibir resultado
# Título grande na página
st.title("Olá! Sua instalação funcionou!")

# Texto explicando o que aconteceu
st.write(
    "Se você está vendo esta mensagem, significa que o Python e o Streamlit "
    "estão instalados e funcionando. Você já pode explorar os outros exemplos!"
)

# Uma mensagem extra em formato de informação (caixa colorida)
st.info("Próximo passo: vá para a pasta 02-fundamentos e rode aquele exemplo.")
