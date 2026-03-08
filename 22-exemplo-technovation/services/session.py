"""
Funções para gerenciar o Session State do Streamlit.

Centralizamos aqui a inicialização dos dados de sessão para evitar:
- Duplicação de código em várias páginas
- Inconsistência (ex: uma página usar valor padrão diferente)
- Esquecer de inicializar em alguma página nova

O Session State é compartilhado entre todas as páginas do app multipage.
"""

import streamlit as st

# Chaves usadas no session_state para login
CHAVE_LOGADO = "logado"
CHAVE_NOME_USUARIO = "nome_usuario"


def garantir_sessao_inicializada():
    """
    Garante que as variáveis de login existem no session_state.
    Deve ser chamada no início de cada página que usa login.

    Se as chaves não existirem, inicializa com valores padrão
    (usuário não logado).
    """
    if CHAVE_LOGADO not in st.session_state:
        st.session_state[CHAVE_LOGADO] = False
    if CHAVE_NOME_USUARIO not in st.session_state:
        st.session_state[CHAVE_NOME_USUARIO] = ""


def fazer_logout():
    """
    Desloga o usuário, limpando os dados no session_state.
    """
    st.session_state[CHAVE_LOGADO] = False
    st.session_state[CHAVE_NOME_USUARIO] = ""
