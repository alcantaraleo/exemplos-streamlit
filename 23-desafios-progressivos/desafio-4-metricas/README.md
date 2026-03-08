# Desafio 4 – Adicionar métricas

## Contexto

O **ODS 3** (Saúde e bem-estar) incentiva hábitos saudáveis e bem-estar em todas as idades. Visualizar a evolução dos dados em gráficos e métricas ajuda a entender padrões e definir metas — por exemplo, reduzir o consumo de água ou manter uma média diária.

Neste desafio, você vai **adicionar métricas e gráficos** ao seu app. As métricas podem ser: total de litros consumidos, média por dia, comparação entre períodos. Os gráficos ajudam a ver tendências: evolução ao longo do tempo, comparação entre dias da semana, etc. Use `st.metric`, `st.line_chart` e `st.bar_chart` do Streamlit.

## Requisitos técnicos mínimos

- Pelo menos **uma métrica** exibida (ex: total de litros, média diária, meta atingida)
- Pelo menos **um gráfico** (`st.line_chart` ou `st.bar_chart`) com dados reais do banco
- Os dados vêm do Supabase (ou da fonte que você usa no Desafio 3)
- Labels e títulos claros para que o usuário entenda o que está vendo

## Critérios de conclusão

- [ ] Há pelo menos uma métrica na tela (total, média ou similar)
- [ ] A métrica usa dados reais do banco/Supabase
- [ ] Há pelo menos um gráfico (linha ou barras)
- [ ] O gráfico usa dados reais (não inventados)
- [ ] Títulos e labels explicam o que cada elemento mostra
- [ ] Se não houver dados, o app trata com mensagem amigável (ex: "Nenhum registro ainda")

## Sugestão de extensão

- Adicionar **filtro por período** (última semana, último mês)
- Criar uma **meta** (ex: "Quero consumir menos de 100 litros por dia") e mostrar o progresso
- Usar bibliotecas como **Plotly** ou **Altair** para gráficos mais elaborados
- Mostrar comparação entre dias da semana ou horários de maior consumo

## Exemplos que ajudam

Consulte estes exemplos do repositório para implementar o desafio:

- [09-graficos](../../09-graficos) – `st.line_chart`, `st.bar_chart`, preparação de DataFrame para gráficos
- [22-exemplo-technovation](../../22-exemplo-technovation) – Dashboard com métricas (`calcular_total_desperdicado`), gráfico de evolução e uso de pandas para visualização
