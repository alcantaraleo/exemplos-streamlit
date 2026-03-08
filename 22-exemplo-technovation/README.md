# 22 – Exemplo Technovation – ODS 12 (Redução de desperdício alimentar)

## Objetivo

Este é um **exemplo completo** de app Streamlit alinhado ao **ODS 12** (Consumo e Produção Responsáveis) da ONU. O foco é a **redução do desperdício de alimentos**. Ideal para equipes do **Technovation** e para quem quer aprender a criar apps que ajudam a resolver problemas reais do mundo.

## Conceitos ensinados

- Como criar um app com **várias páginas** (Login, Dashboard, Sobre)
- Como fazer um **login simples** (usando Session State)
- Como **salvar dados** em um banco SQLite (arquivo local, sem instalação)
- Como **registrar e listar** alimentos desperdiçados
- Como mostrar **métricas** e **gráficos** com os dados
- Como organizar o código com **separação de responsabilidades**

## Como executar

```bash
cd 22-exemplo-technovation
pip install -r requirements.txt
streamlit run app.py
```

O app vai abrir no navegador. Use o menu à esquerda para navegar.

**Pré-requisitos:** Python 3.8 ou superior. O SQLite já vem com o Python.

### Login (para testar)

- **Usuário:** aluno
- **Senha:** 12345

(Outros usuários: familia/senha ods12, professor/senha senha456)

## Estrutura do projeto

```
22-exemplo-technovation/
├── app.py              # Página inicial (Home)
├── pages/
│   ├── 1_Login.py      # Página de login
│   ├── 2_Dashboard.py  # Registro, listagem, métrica e gráfico
│   └── 3_Sobre.py      # Explicação sobre ODS 12 e o problema
├── services/
│   ├── database.py     # Funções de banco de dados (SQLite)
│   └── session.py      # Gerenciamento centralizado do Session State (login)
├── README.md           # Este arquivo
└── requirements.txt    # Dependências do projeto
```

## Funcionalidades (MVP)

1. **Login simples** – Entrar com usuário e senha (exemplo didático).
2. **Registro de desperdício** – Nome do alimento + quantidade.
3. **Listagem** – Ver todos os registros salvos.
4. **Métrica total** – Soma de tudo que foi desperdiçado.
5. **Gráfico de evolução** – Linha mostrando o desperdício ao longo do tempo.
6. **Página "Sobre"** – Explica a ligação com o ODS 12.

## Onde os dados são salvos?

Os dados são salvos em um arquivo chamado **desperdicio.db** na mesma pasta do projeto. Esse arquivo é criado automaticamente na primeira vez que você registra um alimento. É um banco SQLite – simples e não precisa de servidor.

## Por que SQLite e não Supabase?

Outros exemplos deste repositório (como o **15-supabase-basico**) usam **Supabase** – um banco de dados na nuvem. Para este projeto Technovation, escolhemos **SQLite** por motivos didáticos e práticos:

| Aspecto                 | SQLite (usado aqui)                      | Supabase (outros exemplos)                      |
| ----------------------- | ---------------------------------------- | ----------------------------------------------- |
| **Configuração**        | Nenhuma. Já vem com o Python.            | Exige conta, projeto, URL e chave da API.       |
| **Objetivo do exemplo** | MVP rápido para equipes iniciantes.      | Aprender integração com banco na nuvem.         |
| **Uso offline**         | Funciona sem internet.                   | Precisa de conexão.                             |
| **Quando usar**         | Protótipos, projetos locais, uma pessoa. | Apps com vários usuários, dados compartilhados. |
| **Próximo passo**       | Migrar para Supabase para escalar.       | —                                               |

**Resumo:** SQLite permite que qualquer equipe rode o app imediatamente, sem criar conta nem configurar credenciais. Depois de dominar o fluxo (registrar, listar, gráficos), as equipes podem evoluir para Supabase – como mostrado no exemplo 15.

## Próximos passos (ideias para evoluir)

- Adicionar **unidade** (gramas, kg, unidades) ao registrar.
- Permitir **excluir** ou **editar** registros.
- Adicionar **metas** (ex: "Quero reduzir 20% este mês").
- Conectar a um banco na nuvem (Supabase) para várias pessoas usarem.

## Sobre o Technovation

O Technovation é um programa que ensina meninas a criar soluções com tecnologia (apps, IA) para problemas reais. Este exemplo serve como referência para as equipes construírem seus próprios projetos alinhados aos ODS.

---

**ODS 12** – Assegurar padrões de consumo e de produção sustentáveis.
