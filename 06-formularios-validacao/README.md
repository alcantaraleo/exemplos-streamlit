# 06 – Formulários e validação

Aqui você aprende a usar **formulários** no Streamlit com `st.form`: vários campos agrupados que só são enviados quando o usuário clica em um botão. Também vemos como fazer **validação** simples (verificar se os campos foram preenchidos corretamente).

## O que você vai aprender

- **st.form** – Agrupar campos em um formulário.
- **st.form_submit_button** – Botão para enviar o formulário.
- Validação simples: verificar se o texto não está vazio, se o número está no intervalo esperado, etc.
- Exibir mensagens de erro ou sucesso com **st.error** e **st.success**.

## Como executar

```bash
cd 06-formularios-validacao
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Formulário de cadastro com validação e comentários.

## Conceito principal

Dentro de um `st.form`, os widgets não atualizam a tela a cada mudança. Só quando o usuário clica no botão de enviar é que o script processa os valores. Isso evita que a página fique rerodando o tempo todo enquanto a pessoa preenche.

Documentação: [st.form](https://docs.streamlit.io/develop/api-reference/state/st.form)
