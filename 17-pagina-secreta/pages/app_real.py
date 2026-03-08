"""
Página Secreta - App Real

Esta página não aparece no menu de navegação! Ela só pode ser acessada
quando o usuário descobre o easter egg: clicar várias vezes no ícone
do caderno 📓 na página do diário.

Você chegou aqui! Parabéns por ter encontrado o segredo!
"""

import streamlit as st
from menu import menu

# Configuração da página
st.set_page_config(page_title="Página Secreta", page_icon="🤫", layout="wide")

# Mostrar o menu (com link para voltar ao diário)
menu()

# Título e texto explicativo
st.title("🤫 Página Secreta!")
st.subheader("Você descobriu o easter egg!")

st.success(
    "Esta é a **página escondida** do app! Ela não aparece no menu de navegação "
    "e só pode ser acessada de um jeito especial: clicando várias vezes no ícone "
    "do caderno (📓) na página do diário. Você conseguiu! 🎉"
)

st.info(
    "Agora você está na área secreta. Use o botão SAIR abaixo para voltar "
    "ao diário. Ao sair, o contador de cliques é zerado - você precisará "
    "clicar no ícone do caderno novamente para voltar aqui."
)

# Botão SAIR dentro de um container com classe CSS específica
# para que o estilo vermelho não afete outros botões adicionados futuramente
container_sair = st.container()
with container_sair:
    st.markdown(
        """
        <style>
        /* Estiliza apenas o botão SAIR, dentro do container com a classe abaixo */
        .botao-sair-container .stButton > button {
            background-color: #DC3545 !important;
            color: white !important;
            font-weight: bold !important;
            text-transform: uppercase;
            border: none;
        }
        .botao-sair-container .stButton > button:hover {
            background-color: #c82333 !important;
            color: white !important;
        }
        </style>
        <div class="botao-sair-container">
        """,
        unsafe_allow_html=True,
    )

    if st.button("SAIR", type="primary", use_container_width=True):
        # Zerar o contador para que, ao voltar ao diário, o usuário precise
        # dos X cliques novamente para reacessar esta página
        if "cliques_secretos" in st.session_state:
            st.session_state.cliques_secretos = 0
        st.switch_page("app.py")

    st.markdown("</div>", unsafe_allow_html=True)
