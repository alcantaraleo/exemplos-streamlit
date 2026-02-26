# 08 – Dados e tabelas

Aqui você aprende a exibir **tabelas de dados** no Streamlit: **st.dataframe** (tabela interativa, que pode ordenar e rolar) e **st.table** (tabela estática). Usamos a biblioteca **pandas** para criar os dados.

## O que você vai aprender

- **st.dataframe** – Tabela interativa com muitas linhas/colunas.
- **st.table** – Tabela estática (todas as linhas visíveis de uma vez).
- **st.write** com DataFrame – O Streamlit também mostra tabelas automaticamente.
- Criar dados simples com **pandas** (listas em formato de tabela).

## Como executar

```bash
cd 08-dados-tabelas
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo com dataframe e table, comentado.

## Conceitos principais

- **DataFrame** é uma estrutura de dados em formato de tabela (linhas e colunas). O pandas é a biblioteca mais usada para isso em Python.
- **st.dataframe** é melhor quando a tabela é grande: o usuário pode rolar e ordenar.
- **st.table** é melhor quando a tabela é pequena e você quer que tudo apareça fixo na tela.

Documentação: [Data elements](https://docs.streamlit.io/develop/api-reference/data)
