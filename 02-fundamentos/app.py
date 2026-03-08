"""
Fundamentos do Streamlit – Primeiro app completo

Este exemplo mostra:
1. Como exibir texto com st.write
2. Como usar "magic" (variável sozinha na linha)
3. Como mostrar uma tabela (DataFrame)

Referência: https://docs.streamlit.io/get-started/fundamentals/main-concepts
"""

import streamlit as st
import pandas as pd

# 1. Exibir texto inicial
# ----- Título da página -----
# st.title mostra um título grande no topo do app
st.title("Meu primeiro app Streamlit")

# ----- Exibindo texto com st.write -----
# st.write é uma função que mostra quase qualquer coisa na tela:
# texto, números, tabelas, gráficos. O Streamlit escolhe o melhor jeito de exibir.
st.write("Aqui está nossa primeira tentativa de usar dados para criar uma tabela:")

# 2. Processar dados
# ----- Criando uma tabela (DataFrame) -----
# DataFrame é uma tabela com colunas e linhas. Aqui criamos uma bem simples.
# Coluna 1: números de 1 a 4. Coluna 2: números 10, 20, 30, 40.
df = pd.DataFrame(
    {
        "primeira coluna": [1, 2, 3, 4],
        "segunda coluna": [10, 20, 30, 40],
    }
)

# 3. Exibir resultado
# ----- "Magic" do Streamlit -----
# Quando você coloca uma variável sozinha em uma linha (como "df" abaixo),
# o Streamlit automaticamente mostra ela na tela, como se fosse st.write(df).
# Isso se chama "magic" e deixa o código mais curto e fácil de ler.
df

# ----- Outra forma de mostrar a mesma tabela -----
# Aqui usamos st.write de propósito para mostrar que o resultado é o mesmo.
st.write("A mesma tabela, agora usando st.write:")
st.write(df)
