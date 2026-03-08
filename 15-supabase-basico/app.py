"""
Supabase básico no Streamlit

Este exemplo mostra como conectar o Streamlit a um banco de dados Supabase
e fazer as operações mais simples: adicionar registros (INSERT) e listar
todos os registros (SELECT).

Você vai aprender a usar a biblioteca supabase-py, criar um formulário
com campos de texto e número, e exibir os dados em uma tabela.
"""

import os
import streamlit as st
import pandas as pd
from services.database import buscar_registros, inserir_registro

# ----- Configuração da página -----
# Define o título que aparece na aba do navegador e usa layout largo
st.set_page_config(page_title="Supabase Básico", layout="wide")

# ----- Verificar se as credenciais existem -----
# O Supabase precisa de URL e chave de API. Sem elas, não conseguimos conectar.
# Aceitamos credenciais em st.secrets (secrets.toml) ou em variáveis de ambiente (.env)
url = None
key = None
try:
    if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
except (KeyError, AttributeError, TypeError):
    pass
if not url:
    url = os.environ.get("SUPABASE_URL")
if not key:
    key = os.environ.get("SUPABASE_KEY")
credenciais_ok = bool(url and key)

# Se as credenciais não estiverem configuradas, mostramos instruções
if not credenciais_ok:
    st.warning(
        "Para usar o Supabase, configure as credenciais no arquivo "
        "**.streamlit/secrets.toml** ou em **variáveis de ambiente** (SUPABASE_URL e SUPABASE_KEY). "
        "Veja o README para o passo a passo."
    )
    st.info(
        "Resumo: 1) Crie um projeto no Supabase (supabase.com). "
        "2) Crie a tabela 'registros' com os campos nome e valor. "
        "3) Copie a URL e a chave anon do projeto. "
        "4) Coloque em .streamlit/secrets.toml ou em variáveis de ambiente (SUPABASE_URL e SUPABASE_KEY)."
    )
    st.stop()

# ----- Título e introdução -----
st.title("Supabase Básico")
st.markdown(
    "Adicione registros com **nome** e **valor**. Eles serão salvos no Supabase "
    "e listados abaixo. Use o formulário e clique em **Salvar** para adicionar."
)

st.divider()

# 1. Coletar input
# ----- Formulário para adicionar registro -----
# Usamos st.columns para deixar os campos lado a lado (mais bonito)
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    # Campo de texto para o nome. Placeholder mostra um exemplo do que digitar.
    nome = st.text_input("Nome", placeholder="Ex: Produto A", key="nome_input")

with col2:
    # Campo numérico para o valor. min_value=0 evita números negativos.
    # step=0.01 permite casas decimais (ex: 19.99)
    valor = st.number_input("Valor", min_value=0.0, value=0.0, step=0.01, key="valor_input")

with col3:
    # Botão Salvar. Quando clicado, retorna True (senão False).
    # Alinhamos com o topo dos campos usando um pouco de espaço
    st.write("")  # Espaço para alinhar com os inputs
    salvar_clicado = st.button("Salvar", type="primary")

# 2. Processar dados
# ----- Processar quando o usuário clicar em Salvar -----
if salvar_clicado:
    # Validação: nome não pode estar vazio
    nome_limpo = nome.strip() if nome else ""
    if not nome_limpo:
        st.error("Por favor, digite um nome antes de salvar.")
    else:
        # Tenta inserir no banco. try/except para tratar erros (rede, permissão, etc.)
        try:
            sucesso = inserir_registro(nome_limpo, valor)
            if sucesso:
                st.success(f"Registro '{nome_limpo}' salvo com sucesso!")
                # st.rerun() recarrega a página para mostrar o novo registro na lista
                st.rerun()
            else:
                st.error("Não foi possível salvar. Verifique se a tabela existe e as credenciais estão corretas.")
        except Exception as erro:
            st.error(f"Erro ao salvar: {erro}")

st.divider()

# 3. Exibir resultado
# ----- Listagem de todos os registros -----
st.subheader("Registros salvos")
st.write("Abaixo aparecem todos os registros que estão no banco Supabase.")

# Chama a função que faz SELECT * na tabela registros
registros = buscar_registros()

if not registros:
    # Se a lista estiver vazia, pode ser que não há dados ou deu erro
    st.info("Nenhum registro encontrado. Adicione um usando o formulário acima.")
else:
    # Converte a lista de dicionários em DataFrame do pandas
    # Assim podemos exibir com st.dataframe (tabela interativa e bonita)
    tabela = pd.DataFrame(registros)

    # Reordenamos as colunas para mostrar nome e valor primeiro (id por último)
    if "id" in tabela.columns:
        colunas = [c for c in ["nome", "valor"] if c in tabela.columns]
        outras = [c for c in tabela.columns if c not in colunas]
        tabela = tabela[colunas + outras]

    # st.dataframe mostra uma tabela interativa: pode rolar, ordenar, etc.
    st.dataframe(tabela, use_container_width=True)
