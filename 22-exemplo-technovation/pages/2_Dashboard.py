"""
Página do Dashboard - Registro e visualização de desperdício

Aqui o usuário logado pode:
1. Registrar um alimento desperdiçado (nome + quantidade)
2. Ver a lista de todos os registros
3. Ver o total desperdiçado (métrica)
4. Ver um gráfico de evolução ao longo do tempo

Se não estiver logado, redireciona para fazer login.
"""

import streamlit as st
import pandas as pd
from services.database import (
    inserir_registro,
    buscar_todos_registros,
    calcular_total_desperdiçado,
    buscar_dados_para_grafico,
)
from services.session import garantir_sessao_inicializada, CHAVE_LOGADO, CHAVE_NOME_USUARIO

# ----- Verificar se está logado -----
garantir_sessao_inicializada()

if not st.session_state[CHAVE_LOGADO]:
    st.warning("⚠️ Você precisa fazer **login** para acessar o Dashboard.")
    st.info("Clique no botão abaixo para ir à página de login.")
    # st.page_link permite navegação direta para outra página
    st.page_link("pages/1_Login.py", label="Ir para Login 🔐", icon="🔐")
    st.stop()

# ----- Título -----
st.title("📊 Dashboard - Registro de Desperdício")
st.markdown(f"Olá, **{st.session_state[CHAVE_NOME_USUARIO]}**! Aqui você registra e acompanha o desperdício de alimentos.")

st.divider()

# ==================== FUNCIONALIDADE 1: Registrar alimento ====================
st.subheader("🥗 Registrar alimento desperdiçado")

# Usamos colunas para deixar os campos lado a lado (interface mais limpa)
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    nome_alimento = st.text_input(
        "Nome do alimento",
        placeholder="Ex: banana, arroz, pão...",
        key="nome_alimento",
    )

with col2:
    # quantidade em gramas ou unidades - o usuário escolhe a unidade
    quantidade = st.number_input(
        "Quantidade",
        min_value=0.1,
        value=1.0,
        step=0.5,
        help="Em gramas, unidades, etc. Ex: 500 para 500g",
        key="quantidade",
    )

with col3:
    st.write("")  # Espaço para alinhar o botão
    botao_salvar = st.button("💾 Salvar", type="primary")

if botao_salvar:
    nome_limpo = nome_alimento.strip() if nome_alimento else ""
    if not nome_limpo:
        st.error("Por favor, digite o nome do alimento.")
    else:
        sucesso = inserir_registro(nome_limpo, quantidade)
        if sucesso:
            st.success(f"✅ Registrado: **{nome_limpo}** - {quantidade} unidades/gramas")
            st.rerun()
        else:
            st.error("Não foi possível salvar. Tente novamente.")

st.divider()

# ==================== FUNCIONALIDADE 2: Métrica total ====================
total = calcular_total_desperdiçado()

# Métricas em destaque - st.metric mostra um número grande com um rótulo
col_metrica, _, _ = st.columns(3)
with col_metrica:
    st.metric(
        label="📦 Total desperdiçado",
        value=f"{total:,.1f}",
        help="Soma de todas as quantidades registradas (unidades ou gramas)",
    )

st.divider()

# ==================== FUNCIONALIDADE 3: Listagem dos registros ====================
st.subheader("📋 Lista de registros")

registros = buscar_todos_registros()

if not registros:
    st.info("Nenhum registro ainda. Adicione um alimento acima!")
else:
    # Converter para DataFrame do pandas para exibir tabela bonita
    tabela = pd.DataFrame(registros)

    # Reordenar colunas: nome e quantidade primeiro
    colunas_ordem = ["nome", "quantidade", "data"]
    colunas_existentes = [c for c in colunas_ordem if c in tabela.columns]
    tabela = tabela[colunas_existentes]

    st.dataframe(tabela, use_container_width=True)

st.divider()

# ==================== FUNCIONALIDADE 4: Gráfico de evolução ====================
st.subheader("📈 Evolução do desperdício")

dados_grafico = buscar_dados_para_grafico()

if not dados_grafico:
    st.info("Adicione registros para ver o gráfico de evolução.")
else:
    # Converter para formato que o st.line_chart entende
    # DataFrame com data como índice e "Total" como coluna numérica
    df_grafico = pd.DataFrame(dados_grafico)
    df_grafico = df_grafico.rename(columns={"total": "Total desperdiçado"})
    df_grafico = df_grafico.set_index("data")

    st.line_chart(df_grafico)
