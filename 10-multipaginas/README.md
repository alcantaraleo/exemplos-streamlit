# 10 – Apps com várias páginas (multipage)

Aqui você aprende a criar um **app com várias páginas** no Streamlit. O Streamlit usa a **estrutura de pastas** para isso: cada arquivo `.py` dentro da pasta `pages/` vira uma página no menu lateral.

## O que você vai aprender

- Estrutura de pastas: um arquivo principal (por exemplo `app.py`) e uma pasta **pages/** com outros arquivos.
- Cada arquivo em **pages/** vira um link no menu lateral (sidebar).
- O nome do arquivo vira o nome da página (ex.: `pages/1_sobre.py` vira "Sobre").

## Como executar

```bash
cd 10-multipaginas
streamlit run app.py
```

Depois de rodar, veja o menu à esquerda: aparecerão as páginas "Sobre" e "Contato". Clique para navegar.

## Estrutura desta pasta

```
10-multipaginas/
  app.py          <- Página inicial (Home)
  pages/
    1_sobre.py     <- Página "Sobre"
    2_contato.py   <- Página "Contato"
  README.md
```

Regras importantes:
- A pasta deve se chamar **pages** (no plural).
- Os arquivos podem ter um número no início (ex.: `1_sobre.py`) para definir a ordem.
- O que vem depois do número ou do primeiro caractere vira o nome da página.

Documentação: [Multipage apps](https://docs.streamlit.io/develop/concepts/multipage-apps)
