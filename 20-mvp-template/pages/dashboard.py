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
# Se o usuário não está logado, mostramos link para o login.
# Usamos st.page_link em vez de st.switch_page (bug #11115: switch_page perde session_state).
if not st.session_state.get("logado", False):
    st.warning("Você precisa fazer login para acessar o dashboard.")
    st.page_link("pages/login.py", label="Ir para o Login", icon=":material/login:")
    st.stop()

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
            # Limpa o campo de texto para que o usuário possa inserir outro item.
            if "nome_inserir" in st.session_state:
                del st.session_state["nome_inserir"]
            st.rerun()
        else:
            st.error("Não foi possível salvar. Verifique a tabela e as credenciais.")

st.divider()

# ========== SEÇÃO: LISTAR ITENS ==========
st.subheader("Listar itens")

# ----- 1. Coletar input -----
# Nesta seção não há input do usuário; buscamos os dados do banco.

# ----- 2. Processar dados -----
itens = buscar_itens()

# ----- 3. Exibir resultado -----
if not itens:
    st.info("Nenhum item encontrado. Adicione um usando o formulário acima.")
else:
    tabela = pd.DataFrame(itens)
    if "id" in tabela.columns:
        colunas = [c for c in ["nome"] if c in tabela.columns]
        outras = [c for c in tabela.columns if c not in colunas]
        tabela = tabela[colunas + outras]
    st.dataframe(tabela, use_container_width=True)

st.divider()

# ========== SEÇÃO: DELETAR ITEM ==========
st.subheader("Deletar item")

# ----- 1. Coletar input -----
# Buscamos os itens de novo para o selectbox de exclusão
itens_para_deletar = buscar_itens()
if itens_para_deletar:
    # Cada item aparece com um botão "Excluir" ao lado.
    # Quando o usuário clica, chamamos deletar_item com o id daquele item.
    for item in itens_para_deletar:
        item_id = item.get("id")
        if item_id is None:
            continue  # Item sem id (dados malformados); pula para evitar KeyError
        col_nome, col_botao = st.columns([3, 1])
        with col_nome:
            st.write(f"**{item.get('nome', str(item_id))}**")
        with col_botao:
            # O key precisa ser único; usamos o id do item
            if st.button("Excluir", key=f"excluir_{item_id}"):
                # ----- 2. Processar dados -----
                sucesso = deletar_item(item_id)
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
    # st.rerun() faz a verificação "logado" acima rodar de novo; exibe o page_link para login.
    # Evitamos st.switch_page (bug #11115: perde session_state).
    st.rerun()
