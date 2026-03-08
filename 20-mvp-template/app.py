"""
Template MVP - Página inicial (Home)

Este é o arquivo principal do app. Ele verifica se o usuário está logado.
Se não estiver, redireciona para a página de login.
Se estiver, mostra uma mensagem de boas-vindas e indica como ir ao Dashboard.
"""

from dotenv import load_dotenv

import streamlit as st

# Carrega variáveis do arquivo .env (se existir) para SUPABASE_URL e SUPABASE_KEY
load_dotenv()

# ----- Configuração da página -----
# Define o título que aparece na aba do navegador e usa layout largo
st.set_page_config(page_title="MVP Template", layout="wide")

# 1. Coletar input
# ----- Estado da sessão -----
# Inicializamos o Session State: aqui guardamos se o usuário está logado e qual o email.
# Session State é como uma "memória" do app que dura enquanto o usuário navega.
if "logado" not in st.session_state:
    st.session_state.logado = False
if "email_usuario" not in st.session_state:
    st.session_state.email_usuario = ""

# 2. Processar dados
# Se o usuário NÃO está logado, redirecionamos para a página de login.
# st.switch_page troca para outra página do app (como se clicasse no menu).
if not st.session_state.logado:
    st.switch_page("pages/login.py")

# 3. Exibir resultado
# Se chegou aqui, o usuário está logado. Mostramos boas-vindas.
st.title("Bem-vindo ao MVP Template!")
st.success(f"Olá, {st.session_state.get('email_usuario', 'usuário')}! Você está logado.")
st.markdown(
    "Use o **menu à esquerda** para navegar:\n"
    "- **Dashboard**: adicionar, listar e excluir itens no banco de dados.\n"
    "- **Sobre**: informações sobre este app."
)
st.info("Este é um template para seus projetos. Personalize conforme sua necessidade!")
