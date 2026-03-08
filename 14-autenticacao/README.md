# 14 – Login e senha (autenticação)

## Objetivo

Este exemplo ensina um **login simples** com usuário e senha no Streamlit. O app usa **Session State** para guardar se o usuário está "logado" ou não. As senhas são conferidas no próprio código (em um dicionário) – é um exemplo educativo. Em um app real, você não guardaria senhas no código; usaria um banco de dados ou um serviço de autenticação.

## Conceitos ensinados

- Usar **st.session_state** para guardar se o usuário está logado
- Formulário de login (usuário e senha)
- Mostrar conteúdo diferente para quem está logado e para quem não está
- Botão de "Sair" que limpa o estado de login

## Como executar

```bash
cd 14-autenticacao
pip install -r requirements.txt
streamlit run app.py
```

**Para testar:** use usuário `aluno` e senha `12345` (está no código como exemplo; em produção nunca faça isso).

## Conceitos principais

- **Session State** guarda informações que permanecem enquanto o usuário usa o app (entre reruns).
- Inicializamos `st.session_state.get("logado", False)` para saber se já fez login.
- Quando o usuário acerta usuário e senha, colocamos `st.session_state.logado = True` e o nome do usuário.
- Quando clica em "Sair", colocamos `st.session_state.logado = False` e fazemos `st.rerun()`.

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Login simples com session_state e um dicionário de usuários/senhas de exemplo.
- **requirements.txt** – Dependências do exemplo.

Este exemplo é mais avançado que os anteriores, mas a lógica continua simples e comentada para estudo.

Documentação: [Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
