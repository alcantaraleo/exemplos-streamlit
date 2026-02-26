# 09 – Gráficos e mapas

Aqui você aprende a exibir **gráficos** e **mapas** no Streamlit: gráfico de linhas, gráfico de barras e mapa com pontos. Os dados são criados de forma simples com pandas para facilitar o entendimento.

## O que você vai aprender

- **st.line_chart** – Gráfico de linhas (ideal para ver evolução no tempo).
- **st.bar_chart** – Gráfico de barras (comparar valores).
- **st.map** – Mapa com pontos (latitude e longitude).
- Preparar dados em formato de tabela (DataFrame) para os gráficos.

## Como executar

```bash
cd 09-graficos
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo com line_chart, bar_chart e map, comentado.

## Conceitos principais

- Os gráficos do Streamlit recebem um **DataFrame** (tabela). Cada coluna pode ser uma série (linha ou conjunto de barras).
- Para **st.map**, precisamos de colunas chamadas **lat** (latitude) e **lon** (longitude).
- Os dados deste exemplo são inventados (números simples) para você ver o resultado rapidamente.

Documentação: [Charts](https://docs.streamlit.io/develop/api-reference/charts)
