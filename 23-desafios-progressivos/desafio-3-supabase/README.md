# Desafio 3 – Conectar Supabase

## Objetivo

**Conectar seu app ao Supabase** — um banco de dados na nuvem — conectado ao **ODS 13** (Ação contra a mudança global do clima). Os dados persistirão mesmo depois que você fecha o navegador e poderão ser acessados por mais de uma pessoa. Você vai criar uma tabela no Supabase, configurar credenciais com segurança e trocar a lógica em memória por funções que fazem `INSERT` e `SELECT` no banco.

## Conceitos ensinados

- Configuração do Supabase e credenciais (st.secrets)
- INSERT e SELECT em banco de dados na nuvem
- Tratamento de erros de conexão

## Como executar

Depois de implementar o app e configurar as credenciais em `.streamlit/secrets.toml`:

```bash
cd 23-desafios-progressivos/desafio-3-supabase
pip install -r ../../15-supabase-basico/requirements.txt
streamlit run app.py
```

_Pré-requisito: conta no [Supabase](https://supabase.com). Use o requirements.txt do exemplo [15-supabase-basico](../../15-supabase-basico) para as dependências._

## Contexto

O **ODS 13** (Ação contra a mudança global do clima) trata de mitigar os efeitos das mudanças climáticas. Acompanhar consumo de água e outros recursos ajuda a reduzir desperdício e pegada ambiental.

## Requisitos técnicos mínimos

- Conta no [Supabase](https://supabase.com) (plano gratuito)
- Tabela criada no Supabase com colunas adequadas (ex: id, data, litros, usuario)
- Arquivo `services/database.py` (ou similar) com funções de inserir e buscar registros
- Uso de `st.secrets` ou arquivo `.env` para guardar `SUPABASE_URL` e `SUPABASE_KEY` (sem colocar no código)
- O app lê e salva os dados no Supabase em vez de usar apenas `st.session_state`

## Critérios de conclusão

- [ ] A tabela existe no Supabase e tem as colunas necessárias
- [ ] As credenciais estão em `secrets.toml` ou `.env`, não no código
- [ ] Ao salvar um registro, o dado aparece no Supabase (Table Editor)
- [ ] Ao recarregar o app ou abrir em outra aba, os dados continuam lá
- [ ] A listagem busca os dados do Supabase corretamente
- [ ] O app trata erros básicos (ex: credenciais ausentes, conexão falha)

## Sugestão de extensão

- Adicionar função para **excluir** registros (DELETE)
- Adicionar **edição** de registros (UPDATE)
- Associar registros ao usuário (coluna `email` ou `usuario_id`)
- Aprender sobre RLS (Row Level Security) para deixar o banco mais seguro

## Exemplos que ajudam

Consulte estes exemplos do repositório para implementar o desafio:

- [15-supabase-basico](../../15-supabase-basico) – Configuração do Supabase, SELECT, INSERT, `st.secrets` e tratamento de erros
- [20-mvp-template](../../20-mvp-template) – Estrutura completa com `services/database.py`, Supabase e organização do projeto
