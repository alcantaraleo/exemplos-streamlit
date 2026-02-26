"""
Página "Sobre" do app multipáginas

Este arquivo está na pasta pages/. Por isso ele aparece como uma
opção no menu lateral. O nome "1_sobre" vira "Sobre" no menu.
O número 1 define a ordem (primeira página na lista).
"""

import streamlit as st

st.title("Sobre")
st.write("Esta é a página Sobre. Aqui você pode colocar informações sobre o seu app.")
st.write("Por exemplo: quem fez, para que serve, versão, etc.")
