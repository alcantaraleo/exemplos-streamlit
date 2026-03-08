"""
Página de Login

Aqui o usuário digita nome e senha para entrar no app.
Usamos um dicionário simples só para o exemplo (usuários fixos no código).

ATENÇÃO: Em um app real, NUNCA guarde senhas no código.
Use um banco de dados ou serviço de autenticação seguro.
"""

import streamlit as st
from services.session import (
    garantir_sessao_inicializada,
    fazer_logout,
    CHAVE_LOGADO,
    CHAVE_NOME_USUARIO,
)

# ----- Dicionário de exemplo: usuário -> senha -----
# Só para aprendizado! Em produção use banco de dados ou API segura.
# Esses são os usuários que podem entrar no app.
usuarios_senhas = {
    "aluno": "12345",
    "familia": "ods12",
    "professor": "senha456",
}

# ----- Garantir que Session State existe -----
garantir_sessao_inicializada()

# ----- Título -----
st.title("🔐 Login")
st.markdown(
    "Digite seu **usuário** e **senha** para entrar. "
    "(Exemplo: usuário **aluno**, senha **12345**)"
)

st.divider()

# ----- Se NÃO está logado: mostrar formulário -----
if not st.session_state[CHAVE_LOGADO]:
    with st.form("form_login"):
        usuario = st.text_input("Usuário:", placeholder="Ex: aluno")
        senha = st.text_input("Senha:", type="password", placeholder="•••••")
        enviar = st.form_submit_button("Entrar")

    if enviar:
        # Verificar se o usuário existe e se a senha está correta
        if usuario in usuarios_senhas and usuarios_senhas[usuario] == senha:
            st.session_state[CHAVE_LOGADO] = True
            st.session_state[CHAVE_NOME_USUARIO] = usuario
            st.success("✅ Login feito com sucesso! Vá ao Dashboard para registrar desperdícios.")
            st.rerun()
        else:
            st.error("❌ Usuário ou senha incorretos. Tente de novo.")

# ----- Se ESTÁ logado: mostrar mensagem e botão Sair -----
else:
    st.success(f"Você está logado como **{st.session_state[CHAVE_NOME_USUARIO]}**.")
    st.info("Vá ao **Dashboard** no menu para registrar alimentos desperdiçados.")

    if st.button("Sair", type="secondary"):
        fazer_logout()
        st.rerun()
