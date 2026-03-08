"""
App de Diário com Página Secreta (Easter Egg)

Este é o app principal que o usuário vê: um diário funcional onde
podemos escrever, salvar, editar e deletar entradas.
Porém... existe um segredo! Descubra clicando no ícone do caderno
várias vezes. Boa sorte!
"""

import streamlit as st
from datetime import datetime
from uuid import uuid4
from menu import menu

# Número de cliques necessários para descobrir a página secreta
# Altere aqui se quiser deixar mais fácil ou difícil!
CLIQUES_PARA_PAGINA_SECRETA = 5

# Configuração da página
st.set_page_config(page_title="Meu Diário", page_icon="📔", layout="wide")

# Inicializar o que precisamos na sessão (memória do app)
if "entradas" not in st.session_state:
    st.session_state.entradas = []

if "entrada_em_edicao" not in st.session_state:
    st.session_state.entrada_em_edicao = None

if "cliques_secretos" not in st.session_state:
    st.session_state.cliques_secretos = 0

# Quando precisamos limpar o campo (após salvar ou cancelar edição),
# definimos o valor da key fixa como vazio ANTES de criar o widget
if st.session_state.pop("limpar_texto", None):
    st.session_state["texto_entrada"] = ""

# Quando clicamos em "carregar" uma entrada, guardamos o texto aqui e rerunamos.
# Na próxima execução, colocamos no estado do widget ANTES dele ser criado.
if "carregar_texto" in st.session_state:
    st.session_state["texto_entrada"] = st.session_state.carregar_texto
    del st.session_state["carregar_texto"]

# Key fixa para o campo de texto do diário (evita acumular keys antigas no session_state)
chave_texto = "texto_entrada"

# Mostrar o menu na lateral (só "Meu Diário" aparece)
menu()

# Título com o ícone do caderno - ele esconde um segredo!
# Clicando várias vezes no 📓, algo especial acontece...
col_titulo, col_icone = st.columns([6, 1])
with col_titulo:
    st.title("Meu Diário")

with col_icone:
    # Este ícone de caderno parece inocente, mas...
    if st.button("📓", key="easter_egg", help="Clique para ver o caderno"):
        st.session_state.cliques_secretos += 1
        # Qualquer quantidade >= X cliques redireciona (evita cliques rápidos)
        if st.session_state.cliques_secretos >= CLIQUES_PARA_PAGINA_SECRETA:
            st.switch_page("pages/app_real.py")

# Área para escrever a entrada do diário
# Key fixa "texto_entrada" - o valor é pré-definido no início do script quando precisamos
# carregar texto de uma entrada existente ou limpar o campo após salvar
st.text_area(
    "O que você quer escrever hoje?",
    height=150,
    key=chave_texto,
    placeholder="Escreva aqui seus pensamentos, ideias, ou o que aconteceu no seu dia...",
)

# Botão que muda de nome: Salvar (criar) ou Atualizar (editar)
em_modo_edicao = st.session_state.entrada_em_edicao is not None

col_botao, _ = st.columns([1, 5])
with col_botao:
    if em_modo_edicao:
        if st.button("Atualizar", type="primary"):
            # Atualizar a entrada que está sendo editada - só atualiza se tiver texto
            texto_novo = st.session_state.get(chave_texto, "").strip()
            if texto_novo:
                for i, entrada in enumerate(st.session_state.entradas):
                    if entrada["id"] == st.session_state.entrada_em_edicao:
                        st.session_state.entradas[i]["texto"] = texto_novo
                        st.session_state.entradas[i]["data"] = datetime.now().strftime(
                            "%d/%m/%Y %H:%M"
                        )
                        break
                st.session_state.entrada_em_edicao = None
                st.session_state["limpar_texto"] = True
                st.rerun()
            else:
                st.warning("Digite algo antes de salvar!")
    else:
        if st.button("Salvar", type="primary"):
            # Criar nova entrada - só salva se tiver texto
            texto = st.session_state.get(chave_texto, "")
            if texto.strip():
                nova_entrada = {
                    # uuid4 garante ID único mesmo que duas entradas sejam salvas no mesmo segundo
                    "id": str(uuid4()),
                    "texto": texto.strip(),
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                }
                st.session_state.entradas.append(nova_entrada)
                st.session_state["limpar_texto"] = True
                st.rerun()
            else:
                st.warning("Digite algo antes de salvar!")

# Botão "Nova entrada" quando estamos editando - para voltar ao modo criar
if em_modo_edicao:
    if st.button("Cancelar edição"):
        st.session_state.entrada_em_edicao = None
        st.session_state["limpar_texto"] = True
        st.rerun()

st.divider()

# Lista de todas as entradas salvas
st.subheader("Suas entradas")

if not st.session_state.entradas:
    st.info("Ainda não tem nenhuma entrada, vamos criar uma!")
else:
    # Mostrar cada entrada com opção de carregar (editar) e deletar
    for entrada in reversed(st.session_state.entradas):
        # Pegar um pedaço do texto para mostrar na lista (preview)
        preview = entrada["texto"][:80] + "..." if len(entrada["texto"]) > 80 else entrada["texto"]
        data_str = entrada["data"]

        with st.container():
            col_conteudo, col_acoes = st.columns([5, 1])

            with col_conteudo:
                # Ao clicar, carrega a entrada para edição
                clicou_carregar = st.button(
                    f"📝 {preview}",
                    key=f"carregar_{entrada['id']}",
                    help=f"Clique para editar (salvo em {data_str})",
                )
                if clicou_carregar:
                    st.session_state.entrada_em_edicao = entrada["id"]
                    # Guardar para a próxima execução - lá colocamos no widget antes de criá-lo
                    st.session_state.carregar_texto = entrada["texto"]
                    st.rerun()

            with col_acoes:
                # Botão para deletar esta entrada
                if st.button("🗑️", key=f"deletar_{entrada['id']}", help="Deletar esta entrada"):
                    st.session_state.entradas = [
                        e for e in st.session_state.entradas if e["id"] != entrada["id"]
                    ]
                    if st.session_state.entrada_em_edicao == entrada["id"]:
                        st.session_state.entrada_em_edicao = None
                        st.session_state["limpar_texto"] = True
                    st.rerun()

            st.caption(f"Salvo em: {data_str}")
