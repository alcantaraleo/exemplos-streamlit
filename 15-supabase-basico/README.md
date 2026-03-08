# 15 – Supabase básico

Aqui você aprende a **conectar o Streamlit a um banco de dados** usando o **Supabase**. O exemplo mostra como **salvar** (INSERT) e **listar** (SELECT) registros com nome e valor. Tudo explicado passo a passo para ficar fácil de entender.

## O que você vai aprender

- Como configurar o acesso ao Supabase (URL e chave da API).
- Como fazer SELECT para buscar dados da tabela.
- Como fazer INSERT para adicionar novos registros.
- Usar **st.secrets** para guardar credenciais sem colocar no código.
- Tratar erros com try/except de forma simples.

## Pré-requisitos

1. Ter uma conta no [Supabase](https://supabase.com) (é grátis).
2. Criar um novo projeto no Supabase.
3. Criar a tabela `registros` no banco de dados.

## Como criar a tabela no Supabase

1. Abra o painel do seu projeto no Supabase.
2. Vá em **SQL Editor**.
3. Cole o código abaixo e clique em **Run**:

```sql
CREATE TABLE registros (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL,
  valor NUMERIC NOT NULL
);
```

4. Pronto! A tabela `registros` foi criada com as colunas `id`, `nome` e `valor`.

**Importante:** Para este exemplo funcionar sem configurar RLS (Row Level Security), você pode desativar o RLS para a tabela `registros` no Supabase, ou usar a chave **service_role** em vez da anon. No painel: Table Editor > registros > desabilitar RLS. Veja a documentação do Supabase se precisar de ajuda.

## Como configurar as credenciais

As credenciais (URL e chave) **não podem** ficar no código. Use um dos métodos abaixo:

### Opção 1: secrets.toml (recomendado para Streamlit)

1. Crie a pasta `.streamlit` dentro de `15-supabase-basico`, se ainda não existir.
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

Você pode usar o arquivo `.env` (copie de `.env.example`) e carregar com `python-dotenv` antes de rodar. O exemplo também lê `SUPABASE_URL` e `SUPABASE_KEY` de variáveis de ambiente do sistema.

## Como executar

```bash
cd 15-supabase-basico
pip install -r requirements.txt
streamlit run app.py
```

O app vai abrir no navegador. Você verá:
- Um formulário para digitar **nome** e **valor**
- Um botão **Salvar** para adicionar ao banco
- Uma lista com todos os registros salvos

## Estrutura desta pasta

- **README.md** – Este arquivo com as instruções.
- **app.py** – Interface Streamlit (formulário e listagem).
- **services/database.py** – Funções que conectam ao Supabase e fazem SELECT/INSERT.
- **requirements.txt** – Dependências (streamlit, supabase, pandas).
- **.env.example** – Exemplo das variáveis necessárias (para referência).

## Próximos passos

Depois de entender este exemplo, você pode:
- Adicionar um botão para **excluir** registros (DELETE).
- Adicionar **edição** de registros (UPDATE).
- Aprender sobre RLS (Row Level Security) para deixar o banco mais seguro.
