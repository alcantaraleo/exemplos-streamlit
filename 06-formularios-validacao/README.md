# 06 – Formulários e validação

## Objetivo

Este exemplo ensina a usar **formulários** no Streamlit com `st.form`: vários campos agrupados que só são enviados quando o usuário clica em um botão. Também vemos como fazer **validação** simples (verificar se os campos foram preenchidos corretamente).

## Conceitos ensinados

- **st.form** – Agrupar campos em um formulário
- **st.form_submit_button** – Botão para enviar o formulário
- Validação simples: verificar se o texto não está vazio, se o número está no intervalo esperado, etc.
- Exibir mensagens de erro ou sucesso com **st.error** e **st.success**

## Como executar

```bash
cd 06-formularios-validacao
pip install -r requirements.txt
streamlit run app.py
```

## Conceito principal

Dentro de um `st.form`, os widgets não atualizam a tela a cada mudança. Só quando o usuário clica no botão de enviar é que o script processa os valores. Isso evita que a página fique rerodando o tempo todo enquanto a pessoa preenche.

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Formulário de cadastro com validação e comentários.
- **requirements.txt** – Dependências do exemplo.

Documentação: [st.form](https://docs.streamlit.io/develop/api-reference/state/st.form)
