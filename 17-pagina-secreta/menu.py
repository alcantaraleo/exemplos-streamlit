"""
Menu customizado do app de diário

Como desabilitamos o menu nativo no config.toml, precisamos criar
nosso próprio menu na sidebar. Este menu mostra apenas o link para
o diário - a página secreta NÃO aparece aqui!
"""

import streamlit as st


def menu():
    """
    Renderiza o menu na sidebar.
    Mostra apenas o link para "Meu Diário" - a página secreta
    fica invisível e só pode ser acessada pelo easter egg.
    """
    st.sidebar.page_link("app.py", label="Meu Diário", icon="📔")
