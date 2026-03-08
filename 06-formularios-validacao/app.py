"""
Formulários e validação no Streamlit

Este exemplo mostra como criar um formulário com st.form
e como validar os dados digitados pelo usuário (por exemplo:
verificar se o nome não está vazio e se a idade é um número válido).
"""

import streamlit as st

st.set_page_config(page_title="Formulários", layout="wide")
st.title("Formulário com validação")

st.markdown(
    "Preencha os campos abaixo e clique em **Enviar**. "
    "Só quando você clicar no botão é que os dados serão processados."
)

# 1. Coletar input
# ----- FORMULÁRIO -----
# Tudo que está dentro do "with st.form(...)" faz parte do mesmo formulário.
# Os valores só são lidos quando o usuário clica no botão de enviar.
with st.form("formulario_cadastro"):
    # Campos do formulário
    nome = st.text_input("Seu nome:", placeholder="Ex: João")
    idade = st.number_input("Sua idade:", min_value=0, max_value=120, value=10)
    gosta_streamlit = st.checkbox("Gosto de programar com Streamlit!")

    # Botão de enviar. Só existe dentro de um form.
    enviado = st.form_submit_button("Enviar")

# 2. Processar dados
# ----- PROCESSAR APÓS O ENVIO -----
# O código abaixo só roda quando o usuário clicou em "Enviar".
if enviado:
    # Validação 1: nome não pode estar vazio
    nome_limpo = nome.strip() if nome else ""
    if not nome_limpo:
        # 3. Exibir resultado
        st.error("Por favor, digite seu nome.")
    else:
        # Validação 2: idade deve ser maior que 0 (já garantido pelo number_input, mas podemos checar)
        if idade <= 0:
            st.error("Por favor, digite uma idade válida.")
        else:
            # Tudo certo: mostramos uma mensagem de sucesso
            st.success(f"Olá, {nome_limpo}! Você tem {idade} anos.")
            if gosta_streamlit:
                st.balloons()
                st.write("Que legal que você gosta de Streamlit!")
