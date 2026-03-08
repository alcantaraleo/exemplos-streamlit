# 11 – Temas e configuração

## Objetivo

Este exemplo ensina a deixar o app **colorido e com a sua cara**: temas claro/escuro e cores. O Streamlit permite configurar isso no arquivo **.streamlit/config.toml** ou diretamente nas configurações ao rodar o app (menu ⋮ > Settings > Theme).

## Conceitos ensinados

- Onde fica a configuração de tema: pasta **.streamlit** e arquivo **config.toml**
- Como definir cores principais (primaryColor, backgroundColor, etc.)
- Como o app fica mais atrativo para o público (crianças e adolescentes) com cores escolhidas

## Como executar

```bash
cd 11-temas-configuracao
pip install -r requirements.txt
streamlit run app.py
```

Para ver o tema personalizado, o arquivo **.streamlit/config.toml** já deve estar na pasta. Se não aparecer as cores, vá em **Settings** (menu ⋮) > **Theme** e escolha "Custom theme" ou edite o config.toml.

## Estrutura desta pasta

```
11-temas-configuracao/
  app.py
  .streamlit/
    config.toml   <- Cores e tema
  README.md
  requirements.txt
```

Documentação: [Configuration and theming](https://docs.streamlit.io/develop/concepts/configuration)
