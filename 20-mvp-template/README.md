# 20 – Template MVP

Template base reutilizável para projetos finais das equipes. Um MVP completo com **login simples** (apenas email), **dashboard** com inserir, listar e deletar itens, e **conexão com Supabase**. Tudo explicado passo a passo para ser fácil de entender e modificar.

## O que você vai aprender

- Login simples usando email salvo em `st.session_state`.
- Redirecionamento: se não estiver logado, ir para a página de login.
- Dashboard com: inserir item, listar itens, deletar item.
- Conexão com Supabase e lógica de banco separada em `services/database.py`.
- Estrutura multipágina no Streamlit.

## Pré-requisitos

1. Ter uma conta no [Supabase](https://supabase.com) (é grátis).
2. Criar um novo projeto no Supabase.
3. Criar a tabela `itens` no banco de dados.

## Como criar a tabela no Supabase

1. Abra o painel do seu projeto no Supabase.
2. Vá em **SQL Editor**.
3. Cole o código abaixo e clique em **Run**:

```sql
CREATE TABLE itens (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL
);
```

4. Pronto! A tabela `itens` foi criada com as colunas `id` e `nome`.

**Importante:** Para este exemplo funcionar sem configurar RLS (Row Level Security), você pode desativar o RLS para a tabela `itens` no Supabase, ou usar a chave **service_role** em vez da anon. No painel: Table Editor > itens > desabilitar RLS.

## Como configurar as credenciais

As credenciais (URL e chave) **não podem** ficar no código. Use um dos métodos abaixo:

### Opção 1: secrets.toml (recomendado para Streamlit)

1. Crie a pasta `.streamlit` dentro de `20-mvp-template`, se ainda não existir.
2. Crie o arquivo `.streamlit/secrets.toml` (não commite no Git!).
3. Adicione o conteúdo abaixo, trocando pelos seus valores reais:

```toml
SUPABASE_URL = "https://seu-projeto.supabase.co"
SUPABASE_KEY = "sua-chave-anon-ou-service-role"
```

Onde encontrar:
- **SUPABASE_URL:** Painel do projeto > Settings > API > **Project URL**
- **SUPABASE_KEY:** Painel do projeto > Settings > API > **anon public** (ou **service_role** se desativou o RLS)

### Opção 2: Variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais. O app usa `python-dotenv` para carregar o `.env` automaticamente ao iniciar (em `app.py`). As variáveis `SUPABASE_URL` e `SUPABASE_KEY` ficam disponíveis para toda a aplicação.

## Como executar

```bash
cd 20-mvp-template
pip install -r requirements.txt
streamlit run app.py
```

O app vai abrir no navegador. Você verá:
- Se não estiver logado: redirecionamento para a página de **Login**.
- Na página **Login**: digite seu email e clique em **Entrar**.
- Depois do login: acesse o **Dashboard** pelo menu lateral para inserir, listar e excluir itens.
- A página **Sobre** é pública e pode ser acessada sem login.

## Estrutura desta pasta

- **README.md** – Este arquivo com as instruções.
- **app.py** – Página inicial; redireciona para login ou mostra boas-vindas.
- **pages/login.py** – Formulário de login (apenas email).
- **pages/dashboard.py** – Inserir, listar e deletar itens (página protegida).
- **pages/sobre.py** – Informações sobre o app (página pública).
- **services/database.py** – Funções que conectam ao Supabase e fazem SELECT, INSERT e DELETE.
- **requirements.txt** – Dependências (streamlit, supabase, pandas, python-dotenv).
- **.env.example** – Exemplo das variáveis necessárias (para referência).

## Próximos passos

Depois de entender este template, você pode:
- Adicionar **edição** de itens (UPDATE).
- Associar itens ao usuário (coluna `email` na tabela).
- Aprender sobre RLS (Row Level Security) para deixar o banco mais seguro.
- Personalizar as páginas com o tema do seu projeto.
