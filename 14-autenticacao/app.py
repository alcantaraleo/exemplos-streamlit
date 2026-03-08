"""
Login e senha (autenticação) no Streamlit

Este exemplo mostra como fazer uma tela de login simples:
- O usuário digita nome e senha
- Conferimos se estão corretos (aqui usamos um dicionário no código só para exemplo)
- Se estiver certo, guardamos em st.session_state que ele está "logado"
- Assim mostramos uma página diferente para quem está logado

ATENÇÃO: Em um app real, nunca guarde senhas no código.
Use um banco de dados ou serviço de autenticação.
"""

import streamlit as st

st.set_page_config(page_title="Login", layout="wide")

# ----- Dicionário de exemplo: usuário -> senha -----
# Só para aprendizado! Em produção use banco de dados ou API segura.
usuarios_senhas = {
    "aluno": "12345",
    "professor": "senha456",
}

# ----- Inicializar Session State -----
# Session State guarda informações entre uma execução e outra do script.
# Se "logado" não existir ainda, usamos False (usuário não está logado).
if "logado" not in st.session_state:
    st.session_state.logado = False
if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = ""

# 1. Coletar input
# ----- Se NÃO está logado: mostrar formulário de login -----
if not st.session_state.logado:
    st.title("Faça login")
    st.write("Digite seu usuário e senha para entrar. (Exemplo: usuário **aluno**, senha **12345**)")

    with st.form("form_login"):
        usuario = st.text_input("Usuário:")
        senha = st.text_input("Senha:", type="password")
        enviar = st.form_submit_button("Entrar")

    if enviar:
        # 2. Processar dados
        # Verificar se o usuário existe e se a senha está correta
        if usuario in usuarios_senhas and usuarios_senhas[usuario] == senha:
            st.session_state.logado = True
            st.session_state.nome_usuario = usuario
            # 3. Exibir resultado
            st.success("Login feito com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos. Tente de novo.")

# 3. Exibir resultado
# ----- Se ESTÁ logado: mostrar conteúdo e botão Sair -----
else:
    st.title(f"Bem-vindo(a), {st.session_state.nome_usuario}!")
    st.success("Você está logado. Esta é a área restrita do app.")
    st.write("Aqui você pode colocar o conteúdo que só quem fez login pode ver.")

    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.nome_usuario = ""
        st.rerun()
