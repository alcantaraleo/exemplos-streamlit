"""
Exemplo pronto para deploy no Streamlit Community Cloud

Este exemplo mostra como usar st.secrets para guardar configurações e
credenciais de forma segura ao fazer deploy na nuvem. Os secrets nunca
ficam no código nem no repositório Git.

Você vai aprender:
- Como ler valores do st.secrets
- Como verificar se um secret existe antes de usar
- Como organizar secrets em seções (TOML)
"""

import streamlit as st

# ----- Configuração da página -----
# Define o título e layout para ficar bonito no navegador
st.set_page_config(
    page_title="Deploy no Streamlit Community Cloud",
    page_icon="☁️",
    layout="centered",
)

# ----- Título e introdução -----
st.title("☁️ Exemplo de Deploy no Streamlit Community Cloud")
st.markdown(
    "Este app demonstra o uso de **st.secrets** para configurar sua "
    "aplicação de forma segura na nuvem."
)

st.divider()

# ----- Exemplo 1: Ler um secret simples -----
# st.secrets funciona como um dicionário. Podemos acessar por chave ou por atributo.
# Por exemplo: st.secrets["MENSAGEM"] ou st.secrets.MENSAGEM

st.subheader("🔐 Como os secrets aparecem no app")

# Verificamos se a chave existe antes de usar, para evitar erro caso não esteja configurada
if "MENSAGEM" in st.secrets:
    mensagem = st.secrets["MENSAGEM"]
    st.success(f"**Secret configurado!** Sua mensagem personalizada é: _{mensagem}_")
else:
    st.info(
        "💡 O secret **MENSAGEM** ainda não foi configurado. "
        "Configure no painel do Streamlit Cloud ou no arquivo .streamlit/secrets.toml para desenvolvimento local."
    )
    # Usamos um valor padrão quando o secret não existe
    mensagem = "Olá, mundo! (valor padrão)"

st.divider()

# ----- Exemplo 2: Secrets em seções (TOML) -----
# Podemos organizar secrets em seções. Exemplo em secrets.toml:
#
# [minha_config]
# CHAVE_API = "abc123"
# MODO_DEBUG = true

st.subheader("📂 Secrets organizados em seções")

if "minha_config" in st.secrets:
    config = st.secrets["minha_config"]
    st.write("Secrets da seção **minha_config** encontrados:")

    # Mostramos os nomes das chaves (não os valores, por segurança!)
    try:
        chaves = list(config.keys())
    except (AttributeError, TypeError):
        chaves = []
    for chave in chaves:
        st.write(f"- `{chave}`: ✓ configurado")
else:
    st.info(
        "💡 A seção **minha_config** ainda não foi configurada. "
        "No secrets.toml, você pode criar:\n\n"
        "```toml\n[minha_config]\nCHAVE_API = \"sua-chave\"\nMODO_DEBUG = true\n```"
    )

st.divider()

# ----- Exemplo 3: Valor usado no app -----
# Aqui usamos a mensagem (do secret ou padrão) para exibir algo dinâmico
st.subheader("🎨 Uso prático no app")

st.write("A mensagem configurada será exibida aqui:")
st.markdown(f"### {mensagem}")

st.divider()

# ----- Instruções para deploy -----
st.subheader("📋 Próximos passos para deploy")

st.markdown("""
1. **Subir para GitHub** – Envie seu repositório para o GitHub.
2. **Conectar ao Streamlit Cloud** – Acesse [share.streamlit.io](https://share.streamlit.io) e conecte seu repositório.
3. **Configurar secrets** – Clique em "Advanced settings" antes ou durante o deploy e cole o conteúdo do seu `secrets.toml`.
4. Pronto! Seu app estará no ar. 🚀

Veja o **README.md** desta pasta para o passo a passo detalhado.
""")
