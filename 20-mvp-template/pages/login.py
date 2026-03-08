"""
Página de Login

Aqui o usuário digita seu email para "entrar" no app.
Não verificamos senha nem banco de dados: apenas salvamos o email
no st.session_state para simular um login simples.
"""

import streamlit as st

st.set_page_config(page_title="Login - MVP Template", layout="wide")

st.title("Faça login")
st.write("Digite seu email para entrar no app. Esse é um login simplificado para aprendizado.")

st.divider()

# ----- 1. Coletar input -----
# Campo de texto para o usuário digitar o email.
# placeholder dá uma dica do formato esperado.
with st.form("form_login"):
    email = st.text_input(
        "Seu email:",
        placeholder="exemplo@email.com",
        key="email_login"
    )
    enviar = st.form_submit_button("Entrar")

# ----- 2. Processar dados -----
if enviar:
    # Validação: removemos espaços em branco e verificamos se não está vazio
    email_limpo = email.strip() if email else ""
    # Verificação básica: um email precisa ter exatamente um "@" e um "." depois do "@"
    email_valido = email_limpo.count("@") == 1 and "." in email_limpo.split("@")[-1]
    if not email_limpo:
        # 3. Exibir resultado (erro)
        st.error("Por favor, digite seu email antes de entrar.")
    elif not email_valido:
        st.error("Por favor, digite um email válido. Exemplo: nome@email.com")
    else:
        # Salvamos o email e o estado "logado" no session_state.
        # Assim as outras páginas sabem que o usuário está autenticado.
        st.session_state.email_usuario = email_limpo
        st.session_state.logado = True

        # ----- 3. Exibir resultado -----
        st.success("Login feito com sucesso! Redirecionando...")
        # Redirecionamos para o dashboard
        st.switch_page("pages/dashboard.py")
