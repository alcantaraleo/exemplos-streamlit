# 05 – Widgets e entrada de dados

Aqui você aprende a usar **widgets** no Streamlit: botões, sliders, caixas de texto, selectbox, checkbox e radio. São os controles que o usuário usa para interagir com o app.

## O que você vai aprender

- **st.button** – Botão clicável.
- **st.slider** – Barra para escolher um número em um intervalo.
- **st.text_input** – Caixa para digitar texto (string).
- **st.number_input** – Caixa para digitar números.
- **st.selectbox** – Lista para escolher uma opção.
- **st.checkbox** – Caixa de marcar/desmarcar.
- **st.radio** – Escolher uma opção entre várias (botões de rádio).

## Como executar

```bash
cd 05-widgets-input
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo com vários widgets e comentários.

## Conceitos principais

- Cada widget retorna um valor (por exemplo, o texto digitado ou o número escolhido).
- Quando o usuário muda um widget, o Streamlit reroda o script e o valor da variável é atualizado.
- Podemos usar o valor para mostrar mensagens, fazer contas ou mostrar/ocultar partes da página.

Documentação: [Widgets](https://docs.streamlit.io/develop/api-reference/widgets)
