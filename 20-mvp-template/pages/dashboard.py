"""
Página do Dashboard

Aqui o usuário logado pode:
- Inserir novos itens no banco
- Listar todos os itens
- Deletar itens

Se não estiver logado, o app redireciona para a página de login.
"""

import streamlit as st
import pandas as pd
from services.database import buscar_itens, inserir_item, deletar_item, credenciais_configuradas

st.set_page_config(page_title="Dashboard - MVP Template", layout="wide")

# ----- Proteção: verificar se está logado -----
# Se o usuário não está logado, redirecionamos para o login.
if not st.session_state.get("logado", False):
    st.switch_page("pages/login.py")

# ----- Verificar credenciais do Supabase -----
# Usamos a função do database.py para evitar duplicar a lógica.
if not credenciais_configuradas():
    st.warning(
        "Configure as credenciais no arquivo **.streamlit/secrets.toml** ou em variáveis "
        "de ambiente (SUPABASE_URL e SUPABASE_KEY). Veja o README."
    )
    st.stop()

# ----- Cabeçalho -----
st.title("Dashboard")
st.write(f"Olá, **{st.session_state.get('email_usuario', 'usuário')}**! Aqui você gerencia os itens.")
st.divider()

# ========== SEÇÃO: INSERIR ITEM ==========
st.subheader("Inserir item")

# ----- 1. Coletar input -----
nome_novo = st.text_input("Nome do item", placeholder="Ex: Minha tarefa", key="nome_inserir")
salvar_clicado = st.button("Salvar", type="primary", key="btn_salvar")

# ----- 2. Processar dados -----
if salvar_clicado:
    nome_limpo = nome_novo.strip() if nome_novo else ""
    if not nome_limpo:
        # ----- 3. Exibir resultado (erro) -----
        st.error("Por favor, digite um nome antes de salvar.")
    else:
        sucesso = inserir_item(nome_limpo)
        if sucesso:
            # ----- 3. Exibir resultado (sucesso) -----
            st.success(f"Item '{nome_limpo}' salvo com sucesso!")
            st.rerun()
        else:
            st.error("Não foi possível salvar. Verifique a tabela e as credenciais.")

st.divider()

# ========== SEÇÃO: LISTAR ITENS ==========
st.subheader("Listar itens")

# ----- 1. Coletar input -----
# Nesta seção não há input do usuário; buscamos os dados do banco.

# ----- 2. Processar dados -----
# Fazemos UMA busca e reutilizamos o resultado em "Listar" e "Deletar".
itens = buscar_itens()

# ----- 3. Exibir resultado -----
if not itens:
    st.info("Nenhum item encontrado. Adicione um usando o formulário acima.")
else:
    tabela = pd.DataFrame(itens)
    # Colocamos "nome" como primeira coluna, depois as demais (ex: "id")
    # Verificamos se a coluna "nome" existe antes de reordenar
    if "nome" in tabela.columns:
        colunas_ordenadas = ["nome"] + [c for c in tabela.columns if c != "nome"]
        tabela = tabela[colunas_ordenadas]
    st.dataframe(tabela, use_container_width=True)

st.divider()

# ========== SEÇÃO: DELETAR ITEM ==========
st.subheader("Deletar item")

# ----- 1. Coletar input -----
# Reutilizamos a lista já buscada acima (sem nova chamada ao banco).
if itens:
    # Cada item aparece com um botão "Excluir" ao lado.
    # Quando o usuário clica, chamamos deletar_item com o id daquele item.
    for item in itens:
        col_nome, col_botao = st.columns([3, 1])
        with col_nome:
            st.write(f"**{item.get('nome', item.get('id', ''))}**")
        with col_botao:
            # O key precisa ser único; usamos o id do item
            if st.button("Excluir", key=f"excluir_{item['id']}"):
                # ----- 2. Processar dados -----
                sucesso = deletar_item(item["id"])
                # ----- 3. Exibir resultado -----
                if sucesso:
                    st.success("Item excluído!")
                    st.rerun()
                else:
                    st.error("Não foi possível excluir.")
else:
    st.info("Não há itens para excluir.")

st.divider()

# ----- Botão Sair -----
if st.button("Sair", key="btn_sair"):
    st.session_state.logado = False
    st.session_state.email_usuario = ""
    st.switch_page("pages/login.py")
