"""
Gráficos e mapas no Streamlit

Este exemplo mostra como criar:
- Gráfico de linhas (st.line_chart)
- Gráfico de barras (st.bar_chart)
- Mapa com pontos (st.map)

Usamos dados simples em formato de tabela (DataFrame) para ficar fácil de entender.
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gráficos e mapas", layout="wide")
st.title("Gráficos e mapas")

# ----- Dados para os gráficos -----
# Criamos uma tabela com números. Cada coluna vira uma série no gráfico.
# Os números representam valores em diferentes "momentos" (linhas).
dados_linhas = pd.DataFrame(
    {
        "Vendas": [10, 25, 30, 45, 50],
        "Despesas": [8, 20, 22, 35, 40],
        "Lucro": [2, 5, 8, 10, 10],
    }
)

# ----- Gráfico de linhas -----
st.header("Gráfico de linhas")
st.write(
    "O gráfico de linhas mostra como os valores mudam. "
    "Cada coluna da tabela vira uma linha no gráfico."
)
st.line_chart(dados_linhas)

st.divider()

# ----- Gráfico de barras -----
st.header("Gráfico de barras")
st.write("O gráfico de barras compara valores. Aqui usamos os mesmos dados em formato de barras.")
st.bar_chart(dados_linhas)

st.divider()

# ----- Mapa -----
# Para o mapa, precisamos de colunas "lat" (latitude) e "lon" (longitude).
# Cada linha é um ponto no mapa. Os valores abaixo são exemplos (região de São Paulo).
st.header("Mapa com pontos")
st.write(
    "O mapa mostra pontos usando latitude (lat) e longitude (lon). "
    "Aqui colocamos alguns pontos de exemplo perto de São Paulo."
)
mapa_dados = pd.DataFrame(
    {
        "lat": [-23.55, -23.56, -23.54],
        "lon": [-46.63, -46.64, -46.62],
    }
)
st.map(mapa_dados)
