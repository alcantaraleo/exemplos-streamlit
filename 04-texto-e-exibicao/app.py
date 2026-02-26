"""
Texto e exibição no Streamlit

Este exemplo mostra as principais formas de exibir texto na tela:
título, cabeçalhos, markdown, texto simples, legenda e divisor.
Usamos cores e organização para deixar a página atrativa.
"""

import streamlit as st

# ----- Configuração da página (opcional) -----
# Deixamos a página em modo "wide" para usar mais espaço na tela
st.set_page_config(page_title="Texto e exibição", layout="wide")

# ----- TÍTULO -----
# st.title mostra o título principal da página (fonte grande)
st.title("Aprendendo a exibir texto no Streamlit")

# ----- MARKDOWN -----
# st.markdown permite usar formatação: **negrito**, *itálico*, listas, links.
# É como escrever em um arquivo .md (Markdown).
st.markdown(
    "Aqui usamos **negrito** e *itálico*. "
    "Podemos também fazer [links](https://docs.streamlit.io) para a documentação."
)

# Linha horizontal para separar as seções
st.divider()

# ----- HEADER E SUBHEADER -----
# header = título de seção (tamanho médio)
# subheader = subtítulo (um pouco menor)
st.header("Seção 1: Cabeçalhos")
st.subheader("Este é um subheader")

# ----- TEXTO SIMPLES (st.text) -----
# st.text mostra texto em fonte fixa, sem formatação. Bom para código ou dados simples.
st.header("Seção 2: Texto simples")
st.text("Este é um texto em fonte fixa. Útil para mostrar códigos ou valores.")

# ----- CAPTION (legenda) -----
# st.caption mostra texto pequeno, como uma legenda ou nota de rodapé.
st.caption("Esta é uma legenda: texto pequeno para explicar algo sem ocupar muito espaço.")

st.divider()

# ----- WRITE -----
# st.write mostra quase qualquer coisa: texto, número, lista.
# O Streamlit decide como exibir.
st.header("Seção 3: st.write")
st.write("Podemos escrever texto normal com st.write.")
st.write("Também podemos mostrar números:", 42, "e listas:", [1, 2, 3])

# ----- RESUMO VISUAL -----
# Usamos uma caixa colorida (st.info) para resumir o que aprendemos.
st.divider()
st.info(
    "Resumo: use st.title para o título, st.header/subheader para seções, "
    "st.markdown para formatação, st.text para texto fixo e st.write para texto e dados."
)
