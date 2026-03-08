"""
App principal - ODS 12: Redução de desperdício alimentar

Este é o arquivo principal do app. Ele é a página inicial (Home).
As outras páginas ficam na pasta "pages/". O Streamlit mostra links
para cada arquivo da pasta "pages/" no menu lateral.

Este projeto é um exemplo para o Technovation, alinhado aos Objetivos
de Desenvolvimento Sustentável (ODS) da ONU - em especial o ODS 12.
"""

import streamlit as st
from services.session import garantir_sessao_inicializada, CHAVE_LOGADO, CHAVE_NOME_USUARIO

# ----- Configuração da página -----
# page_title: texto que aparece na aba do navegador
# page_icon: emoji ou ícone (🌍 = planeta, ligado à sustentabilidade)
# layout: "wide" = usa toda a largura da tela
st.set_page_config(
    page_title="ODS 12 - Redução de Desperdício",
    page_icon="🌍",
    layout="wide",
)

# ----- Inicializar Session State -----
garantir_sessao_inicializada()

# ----- Página inicial -----
st.title("🌍 Redução de Desperdício Alimentar")
st.markdown(
    "**Bem-vindo(a)!** Este app ajuda a registrar e acompanhar o desperdício "
    "de alimentos em casa ou na escola. Ele está alinhado ao **ODS 12** "
    "da ONU (Objetivos de Desenvolvimento Sustentável)."
)

st.divider()

# Mensagem diferente para quem está logado ou não
if st.session_state[CHAVE_LOGADO]:
    st.success(f"Olá, **{st.session_state[CHAVE_NOME_USUARIO]}**! Você está logado.")
    st.info(
        "👉 Use o menu à esquerda para ir ao **Dashboard** (registrar desperdícios) "
        "ou à página **Sobre o Problema** (entender a ligação com o ODS 12)."
    )
else:
    st.warning("Você ainda não fez login.")
    st.info(
        "Clique no botão abaixo para fazer login. "
        "Depois você poderá registrar alimentos desperdiçados no **Dashboard**."
    )
    st.page_link("pages/1_Login.py", label="Ir para Login 🔐", icon="🔐")

st.divider()
st.caption(
    "Projeto exemplo para Technovation • ODS 12 - Consumo e Produção Responsáveis"
)
