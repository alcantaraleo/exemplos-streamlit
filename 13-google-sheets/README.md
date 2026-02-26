# 13 – Google Sheets como banco de dados

Aqui você aprende a **ler e escrever dados** em um **Google Sheets** usando o Streamlit. O exemplo usa a biblioteca **gspread** e credenciais de serviço (arquivo JSON). A lógica é explicada passo a passo para ficar fácil de entender.

## O que você vai aprender

- Como configurar o acesso ao Google Sheets (conta de serviço e arquivo JSON de credenciais).
- Ler dados de uma planilha (lista de linhas).
- Escrever dados em uma planilha (append de uma nova linha).
- Usar **st.secrets** para guardar credenciais sem colocar no código.

## Pré-requisitos

1. Ter uma conta Google.
2. Criar um projeto no Google Cloud e ativar a API Google Sheets.
3. Criar uma conta de serviço e baixar o arquivo JSON de credenciais.
4. Compartilhar a planilha com o e-mail da conta de serviço (ex.: xxx@xxx.iam.gserviceaccount.com).

Passo a passo detalhado está na documentação do gspread e do Google Cloud. No Streamlit, você pode guardar o conteúdo do JSON em **.streamlit/secrets.toml** (veja exemplo no README ou na doc do Streamlit: [Connections and secrets](https://docs.streamlit.io/develop/concepts/connections)).

## Como executar

```bash
cd 13-google-sheets
pip install -r requirements.txt
```

Antes de rodar, configure o arquivo **.streamlit/secrets.toml** com as credenciais do Google (ou variáveis de ambiente). Depois:

```bash
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo que lê e mostra dados da planilha; comentários explicam onde fazer a escrita.
- **requirements.txt** – gspread e dependências.

## Estrutura do secrets (exemplo)

No arquivo `.streamlit/secrets.toml` (não commitar no Git), você pode colocar as credenciais no formato que o gspread aceita, ou usar o formato de "connections" do Streamlit. Veja a documentação oficial do [Streamlit - Connections](https://docs.streamlit.io/develop/concepts/connections) para o formato exato.
