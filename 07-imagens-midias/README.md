# 07 – Imagens e mídias

Aqui você aprende a exibir **imagens**, **áudio** e **vídeo** no Streamlit usando `st.image`, `st.audio` e `st.video`. O exemplo usa URLs ou arquivos locais e mostra como adicionar legendas.

## O que você vai aprender

- **st.image** – Mostrar uma imagem (arquivo local ou URL).
- **st.audio** – Reproduzir áudio.
- **st.video** – Reproduzir vídeo.
- Uso de legendas (caption) para explicar o conteúdo.

## Como executar

```bash
cd 07-imagens-midias
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo com imagem (URL pública), comentado.
- **pasta_imagens/** – Pasta onde você pode colocar imagens locais para testar (opcional).

Para testar com arquivo local, coloque uma imagem (por exemplo `foto.png`) na pasta `07-imagens-midias` e no código use: `st.image("foto.png", caption="Minha foto")`.

## Referência

[API – Media elements](https://docs.streamlit.io/develop/api-reference/media)
