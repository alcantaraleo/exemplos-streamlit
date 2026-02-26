"""
Google Sheets como banco de dados no Streamlit

Este exemplo mostra como conectar a uma planilha do Google Sheets
e exibir os dados na tela. Para funcionar, você precisa:
1. Configurar uma conta de serviço no Google Cloud
2. Ativar a API Google Sheets
3. Compartilhar a planilha com o e-mail da conta de serviço
4. Guardar as credenciais em .streamlit/secrets.toml

Por simplicidade, aqui só mostramos a estrutura do código e exibimos
uma mensagem quando as credenciais não estão configuradas.
Quando estiver tudo configurado, use gspread para abrir a planilha
e ler as linhas. Veja o README para o passo a passo.
"""

import streamlit as st

st.set_page_config(page_title="Google Sheets", layout="wide")
st.title("Google Sheets como banco de dados")

st.write(
    "Neste exemplo você aprende a **ler** e **escrever** dados em uma "
    "planilha do Google Sheets a partir do Streamlit."
)

# ----- Verificar se as credenciais existem -----
# Em um app real, você usaria st.secrets para acessar as chaves do Google.
# Como não temos as credenciais aqui, mostramos instruções.
if "google_sheets" not in st.secrets:
    st.warning(
        "Para usar o Google Sheets, configure as credenciais no arquivo "
        "**.streamlit/secrets.toml**. Veja o README desta pasta para o passo a passo."
    )
    st.info(
        "Resumo: 1) Crie um projeto no Google Cloud. "
        "2) Ative a API Google Sheets. "
        "3) Crie uma conta de serviço e baixe o JSON. "
        "4) Compartilhe a planilha com o e-mail da conta de serviço. "
        "5) Coloque as credenciais no secrets.toml."
    )
else:
    # Quando as credenciais estiverem configuradas, aqui você usaria
    # gspread para abrir a planilha e ler os dados. Exemplo:
    # import gspread
    # gc = gspread.service_account_from_dict(st.secrets["google_sheets"])
    # planilha = gc.open("Nome da sua planilha").sheet1
    # dados = planilha.get_all_records()
    # st.dataframe(pd.DataFrame(dados))
    st.success("Credenciais encontradas! Aqui você colocaria o código para ler a planilha (veja comentários no app.py).")
