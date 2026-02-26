"""
Widgets e entrada de dados no Streamlit

Este exemplo mostra os principais widgets:
botão, slider, caixa de texto, selectbox, checkbox e radio.
Cada um guarda um valor que podemos usar no resto do código.
"""

import streamlit as st

st.set_page_config(page_title="Widgets", layout="wide")
st.title("Widgets – controles para o usuário")

# ----- CAIXA DE TEXTO (text_input) -----
# O usuário digita um texto. O valor fica na variável "nome".
nome = st.text_input("Digite seu nome:", placeholder="Ex: Maria")

if nome:
    st.success(f"Olá, {nome}! Bem-vindo(a) ao app.")

st.divider()

# ----- SLIDER -----
# O usuário arrasta a barra para escolher um número entre 0 e 100.
# O valor inicial é 50.
numero = st.slider("Escolha um número de 0 a 100:", 0, 100, 50)
st.write("O número escolhido foi:", numero, "e o dobro é", numero * 2)

st.divider()

# ----- SELECTBOX -----
# Lista de opções. O usuário escolhe uma.
fruta = st.selectbox(
    "Qual sua fruta favorita?",
    ("Maçã", "Banana", "Laranja", "Uva", "Morango"),
)
st.write("Você escolheu:", fruta)

st.divider()

# ----- CHECKBOX -----
# Caixa de marcar/desmarcar. Retorna True ou False.
mostrar_mensagem = st.checkbox("Quero ver uma mensagem especial")

if mostrar_mensagem:
    st.balloons()  # Animação de balões na tela
    st.write("Você marcou a caixa! Aqui está sua mensagem especial.")

st.divider()

# ----- RADIO -----
# Escolher uma opção entre várias (só uma por vez).
cor_favorita = st.radio(
    "Qual sua cor favorita?",
    ("Vermelho", "Azul", "Verde", "Amarelo"),
    horizontal=True,  # opções na horizontal
)
st.write("Sua cor favorita é:", cor_favorita)

st.divider()

# ----- BOTÃO -----
# Quando o usuário clica, podemos executar uma ação.
# O valor de "clicou" é True apenas no momento do clique.
clicou = st.button("Clique aqui para ver um emoji")

if clicou:
    st.write("🎉 Você clicou no botão!")
