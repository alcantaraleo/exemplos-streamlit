# 03 – Conceitos do Streamlit

Aqui você aprende **conceitos importantes** do Streamlit: como organizar a tela com **sidebar** e **colunas**, e um pouco sobre o **modelo de execução** (o script roda de cima para baixo e pode rodar de novo quando o usuário interage).

## O que você vai aprender

- **Sidebar (barra lateral):** Colocar controles (slider, selectbox) na lateral da página.
- **Colunas:** Colocar elementos um ao lado do outro com `st.columns`.
- **Modelo de execução:** O app é um script Python que roda do início ao fim; quando algo muda (código ou interação), ele pode rodar de novo.

## Como executar

```bash
cd 03-conceitos
streamlit run app.py
```

## Estrutura desta pasta

- **README.md** – Este arquivo.
- **app.py** – Exemplo com sidebar e colunas, comentado.

## Conceitos principais

1. **st.sidebar:** Tudo que você coloca em `st.sidebar` aparece na barra à esquerda (por exemplo: `st.sidebar.slider`, `st.sidebar.selectbox`).
2. **st.columns:** Cria colunas para organizar widgets na mesma linha (ex.: duas colunas com `st.columns(2)`).
3. **Execução:** O script roda do topo até o final. Quando o usuário mexe em um widget, o Streamlit reroda o script e os valores dos widgets são atualizados.

Documentação: [Concepts – Architecture and execution](https://docs.streamlit.io/develop/concepts/architecture), [Layout](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar).
