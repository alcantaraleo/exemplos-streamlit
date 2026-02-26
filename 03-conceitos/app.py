"""
Conceitos do Streamlit – Sidebar e colunas

Este exemplo mostra:
1. Como usar a barra lateral (sidebar) para colocar controles
2. Como usar colunas para colocar elementos um ao lado do outro

A linguagem é simples e o código é comentado para facilitar o aprendizado.
"""

import streamlit as st

# ----- Título na página principal -----
st.title("Layout: Sidebar e colunas")

# ----- SIDEBAR (barra lateral) -----
# Tudo que colocamos em st.sidebar aparece na barra à esquerda da tela.
# Assim os controles não atrapalham o conteúdo principal.

# Selectbox na sidebar: o usuário escolhe uma opção
como_contato = st.sidebar.selectbox(
    "Como você prefere ser contactado?",
    ("E-mail", "Telefone fixo", "Celular"),
)

# Slider na sidebar: o usuário escolhe um intervalo de valores
intervalo = st.sidebar.slider(
    "Escolha um intervalo de valores",
    0.0,
    100.0,
    (25.0, 75.0),  # valor inicial do intervalo
)

# Mostramos na tela o que foi escolhido na sidebar
st.write("Você escolheu ser contactado por:", como_contato)
st.write("O intervalo escolhido foi:", intervalo)

# ----- COLUNAS -----
# st.columns(2) cria duas colunas. Podemos colocar widgets em cada uma.
# Assim ficam um ao lado do outro em vez de um embaixo do outro.
st.subheader("Elementos lado a lado (colunas)")

coluna_esquerda, coluna_direita = st.columns(2)

# Na coluna da esquerda: um botão
with coluna_esquerda:
    st.button("Clique aqui!")

# Na coluna da direita: opções de escolha (radio)
with coluna_direita:
    casa = st.radio(
        "Qual sua casa?",
        ("Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"),
    )
    st.write("Você está na casa:", casa)
