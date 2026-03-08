# Desafio 1 – App local sem banco

## Contexto

O **ODS 6** (Água potável e saneamento) da ONU visa garantir água limpa e saneamento para todos. Um jeito de contribuir é acompanhar o próprio consumo de água em casa ou na escola.

Neste desafio, você vai criar um app simples em **uma única página** para registrar o consumo diário de água (em litros). Os dados podem ficar na memória (`st.session_state`) ou em uma lista em Python — **não use banco de dados** ainda. O foco é fazer um fluxo básico funcionar: formulário, validação e listagem na tela.

## Requisitos técnicos mínimos

- Um formulário com pelo menos:
  - Data (ou dia atual)
  - Quantidade em litros
  - Botão para salvar
- Uma lista ou tabela exibindo os registros feitos na sessão
- Uso de `st.session_state` para manter os dados enquanto o app está rodando
- Layout organizado (títulos, seções, divisórias)

## Critérios de conclusão

- [ ] O formulário aceita data e litros e tem um botão "Salvar"
- [ ] Ao clicar em "Salvar", o novo registro aparece na lista
- [ ] A lista mostra todos os registros da sessão (mesmo que vazia no início)
- [ ] O app roda sem erro (`streamlit run app.py`)
- [ ] A interface tem título e organização visual básica

## Sugestão de extensão

- Salvar os registros em um arquivo **CSV** ao fechar ou em um botão "Exportar"
- Adicionar edição e exclusão de registros
- Calcular o total de litros consumidos e exibir na tela

## Exemplos que ajudam

Consulte estes exemplos do repositório para implementar o desafio:

- [02-fundamentos](../../02-fundamentos) – Primeiro app e conceitos básicos
- [04-texto-e-exibicao](../../04-texto-e-exibicao) – Títulos, texto, markdown e exibição de informações
- [05-widgets-input](../../05-widgets-input) – Botões, sliders, caixas de texto e outros controles
- [06-formularios-validacao](../../06-formularios-validacao) – Formulários e validação de dados
- [08-dados-tabelas](../../08-dados-tabelas) – Tabelas e dados com `st.dataframe` e `st.table`
