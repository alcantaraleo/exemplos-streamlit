# 02 – Fundamentos do Streamlit

Aqui você aprende os **conceitos básicos** do Streamlit: como um app é estruturado, como rodar com `streamlit run`, e como exibir texto e dados na tela usando `st.write` e "magic".

## O que você vai aprender

- Como rodar um app Streamlit.
- O que é **magic** (escrever na tela sem chamar função).
- Como usar **st.write** para mostrar texto, números e tabelas.
- Como o Streamlit **reroda** o script quando algo muda.

## Como executar

Na pasta do projeto, abra o terminal e digite:

```bash
cd 02-fundamentos
streamlit run app.py
```

O navegador abrirá o app. Se você mudar o código e salvar, o Streamlit pode perguntar se quer "Rerun" – clique para ver as mudanças.

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Código do exemplo com comentários explicando cada parte.

## Conceitos principais

1. **Rodar o app:** `streamlit run app.py` sobe um servidor e abre o app no navegador.
2. **Magic:** Se você colocar uma variável sozinha em uma linha (por exemplo `df`), o Streamlit mostra ela na tela automaticamente.
3. **st.write:** Mostra quase qualquer coisa: texto, número, tabela, gráfico. É a função "canivete suíço" do Streamlit.
4. **Rerun:** Quando o usuário interage (por exemplo, clica em um botão), o Streamlit roda o script de novo do começo ao fim.

Documentação oficial: [Fundamentals – Main concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
