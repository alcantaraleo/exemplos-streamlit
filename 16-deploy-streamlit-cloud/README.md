# 16 – Deploy no Streamlit Community Cloud

## Objetivo

Este exemplo ensina a **publicar seu app Streamlit na internet** usando o **Streamlit Community Cloud** (gratuito). O exemplo mostra como usar **st.secrets** para configurar credenciais e mensagens de forma segura, sem colocar no código.

## Conceitos ensinados

- Como subir seu projeto para o GitHub
- Como conectar o repositório ao Streamlit Community Cloud
- Como configurar secrets (credenciais, chaves) de forma segura
- Como usar `st.secrets` no código para ler configurações

## Como executar

Configure `.streamlit/secrets.toml` com suas credenciais (veja seção "Executar localmente" abaixo). Depois:

```bash
cd 16-deploy-streamlit-cloud
pip install -r requirements.txt
streamlit run app.py
```

## Passo a passo para deploy

### 1. Subir para o GitHub

1. Crie uma conta no [GitHub](https://github.com) (se ainda não tiver).
2. Crie um novo repositório no GitHub (botão **New**).
3. No seu computador, dentro da pasta do projeto, execute:

```bash
# Inicialize o Git (se ainda não fez)
git init

# Adicione os arquivos
git add .
git commit -m "Primeiro commit - app Streamlit"

# Conecte ao seu repositório no GitHub (troque SEU_USUARIO e SEU_REPOSITORIO)
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

# Envie o código
git push -u origin main
```

**Importante:** O Streamlit Community Cloud precisa que o arquivo principal do app e o `requirements.txt` estejam no repositório. Se seu app está na pasta `16-deploy-streamlit-cloud`, o caminho do arquivo será `16-deploy-streamlit-cloud/app.py`. O `requirements.txt` nesta pasta será usado automaticamente.

### 2. Conectar ao Streamlit Community Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io).
2. Faça login com sua conta do GitHub.
3. Clique em **"Create app"** (ou **"New app"**).
4. Preencha:
   - **Repository:** Seu usuário/repositório (ex: `meuusuario/meu-projeto-streamlit`).
   - **Branch:** `main` (ou `master`, dependendo do seu repositório).
   - **Main file path:** O caminho do arquivo principal. Para este exemplo: `16-deploy-streamlit-cloud/app.py`.
5. (Opcional) Em **App URL**, escolha um nome para a URL do seu app (ex: `meu-app-incrivel`).
6. Clique em **"Deploy!"**.

Aguarde alguns minutos. O Streamlit vai instalar as dependências e iniciar seu app. Quando terminar, você verá um link para acessar o app na internet.

### 3. Configurar secrets

Se seu app usa `st.secrets` (como este exemplo), você precisa configurar os secrets no Streamlit Cloud:

1. Durante o deploy: clique em **"Advanced settings"** antes de fazer deploy.
2. No campo **"Secrets"**, cole o conteúdo do seu arquivo `secrets.toml` (formato TOML). Exemplo:

```toml
MENSAGEM = "Olá do Streamlit Cloud! Meu app está no ar!"

[minha_config]
CHAVE_API = "sua-chave-aqui"
MODO_DEBUG = true
```

3. Clique em **"Save"** e depois em **"Deploy!"**.

**Se o app já está em deploy:** vá em [share.streamlit.io](https://share.streamlit.io) → clique nos três pontinhos ao lado do seu app → **Settings** → aba **Secrets** → edite e salve.

**Nunca** coloque o arquivo `secrets.toml` no Git. Ele contém informações sensíveis. Use o `.gitignore` para garantir que ele não seja enviado.

## Executar localmente (desenvolvimento)

1. Crie a pasta `.streamlit` dentro de `16-deploy-streamlit-cloud` (se não existir).
2. Copie o arquivo `secrets.example.toml` para `.streamlit/secrets.toml` e preencha com seus valores. Ou crie o arquivo `.streamlit/secrets.toml` manualmente com o conteúdo:

```toml
MENSAGEM = "Minha mensagem local"

[minha_config]
CHAVE_API = "chave-teste"
MODO_DEBUG = true
```

3. Execute:

```bash
cd 16-deploy-streamlit-cloud
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo com o passo a passo.
- **app.py** – App Streamlit que usa `st.secrets`.
- **requirements.txt** – Dependências necessárias para o deploy.
- **secrets.example.toml** – Modelo do arquivo de secrets (copie para `.streamlit/secrets.toml`).

## Referências

- [Deploy no Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
- [Gerenciamento de Secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)
