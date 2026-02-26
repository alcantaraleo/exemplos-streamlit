"""
Dados e tabelas no Streamlit

Este exemplo mostra como exibir tabelas na tela usando:
- st.dataframe (tabela interativa)
- st.table (tabela estática)
Criamos os dados com a biblioteca pandas (DataFrame).
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dados e tabelas", layout="wide")
st.title("Exibindo tabelas de dados")

# ----- Criando dados simples com pandas -----
# DataFrame é como uma planilha: tem colunas e linhas.
# Aqui criamos uma tabela com nomes de alunos e notas.
dados = {
    "Aluno": ["Ana", "Bruno", "Carla", "Diego", "Elena"],
    "Nota 1": [8.5, 7.0, 9.0, 6.5, 8.0],
    "Nota 2": [9.0, 8.0, 8.5, 7.0, 9.5],
}
tabela = pd.DataFrame(dados)

# ----- st.dataframe -----
# Tabela interativa: o usuário pode rolar, ordenar clicando no nome da coluna, etc.
st.header("Tabela interativa (st.dataframe)")
st.write("Você pode clicar no nome da coluna para ordenar e rolar se tiver muitas linhas.")
st.dataframe(tabela, use_container_width=True)

st.divider()

# ----- st.table -----
# Tabela estática: tudo aparece de uma vez, sem rolagem interna.
# Bom para tabelas pequenas.
st.header("Tabela estática (st.table)")
st.write("Esta tabela é fixa: todas as linhas aparecem de uma vez.")
st.table(tabela)

st.divider()

# ----- st.write com DataFrame -----
# O Streamlit também mostra um DataFrame se passarmos para st.write.
# Ele escolhe uma forma bonita de exibir (geralmente como tabela interativa).
st.header("Tabela com st.write")
st.write("Quando passamos uma tabela para st.write, o Streamlit exibe automaticamente:")
st.write(tabela)
