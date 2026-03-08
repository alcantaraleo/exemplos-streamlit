"""
Chat e LLMs no Streamlit

Este exemplo mostra a estrutura de um app de chat:
- Caixa para o usuário digitar (st.chat_input)
- Exibição de mensagens do usuário e da assistente (st.chat_message)
- Histórico das mensagens guardado em uma lista

Por enquanto a "assistente" só responde com uma frase fixa.
Para usar um LLM de verdade (ex.: OpenAI), você troca a parte que
gera a resposta pela chamada à API. Veja o README para mais detalhes.
"""

import streamlit as st

st.set_page_config(page_title="Chat com LLM", layout="wide")
st.title("App de chat")

# 3. Exibir resultado
# ----- Histórico de mensagens -----
# Guardamos as mensagens em uma lista. Cada item é um dicionário com
# "role" (quem falou: "user" ou "assistant") e "content" (o texto).
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# ----- Mostrar as mensagens antigas na tela -----
for msg in st.session_state.mensagens:
    # st.chat_message exibe uma mensagem com "avatar" de usuário ou assistente
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 1. Coletar input
# ----- Caixa para digitar nova mensagem -----
# st.chat_input mostra o campo de texto na parte de baixo da tela.
# Quando o usuário envia, o texto vem em "prompt".
prompt = st.chat_input("Digite sua mensagem aqui...")

if prompt:
    # 2. Processar dados
    # 1) Adicionar a mensagem do usuário ao histórico
    st.session_state.mensagens.append({"role": "user", "content": prompt})

    # 2) Gerar a resposta da assistente
    # Aqui usamos uma resposta fixa para o exemplo funcionar sem API.
    # Para usar um LLM de verdade, substitua esta linha por uma chamada à API
    # (ex.: OpenAI) e use o texto retornado como "resposta".
    resposta = (
        "Olá! Sou uma assistente de exemplo. "
        "Para respostas reais, conecte um LLM (veja o README). "
        f"Você disse: {prompt}"
    )

    # 3) Adicionar a resposta da assistente ao histórico
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})

    # 4) Rerun para atualizar a tela com as novas mensagens
    st.rerun()
