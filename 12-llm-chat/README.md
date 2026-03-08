# 12 – Uso com LLMs e chat

## Objetivo

Este exemplo ensina a criar um **app de chat** que pode ser conectado a um **LLM** (modelo de linguagem, como os que respondem em texto). O exemplo usa a estrutura de chat do Streamlit (**st.chat_message**, **st.chat_input**) e mostra como exibir mensagens do usuário e da "assistente". A lógica é simples: por padrão a "assistente" só repete uma resposta fixa; no README explicamos como trocar por uma API de LLM (por exemplo OpenAI) quando você tiver uma chave de API.

## Conceitos ensinados

- **st.chat_message** – Exibir uma mensagem no chat (como "user" ou "assistant")
- **st.chat_input** – Caixa de texto para o usuário digitar e enviar mensagens
- Como guardar o histórico de mensagens (lista) e mostrar na tela
- Onde encaixar uma chamada a um LLM (ex.: OpenAI) quando quiser respostas reais

## Como executar

```bash
cd 12-llm-chat
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Chat simples com resposta fixa; comentários indicam onde colocar a chamada ao LLM.
- **requirements.txt** – Dependências (opcional; só precisa se for usar uma API de LLM).

## Usar um LLM de verdade

Para conectar a um serviço como OpenAI, você precisará de uma chave de API. Guarde-a em um arquivo **.streamlit/secrets.toml** (não commite no Git) ou use variável de ambiente. No código, onde hoje está a resposta fixa, você chama a API do LLM e usa o texto retornado como resposta da assistente. A documentação do Streamlit tem tutoriais: [Chat and LLM apps](https://docs.streamlit.io/develop/tutorials/llms).
