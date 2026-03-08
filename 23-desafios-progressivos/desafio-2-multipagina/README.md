# Desafio 2 – Transformar em multipágina

## Contexto

O **ODS 11** (Cidades e comunidades sustentáveis) incentiva cidades mais inclusivas, seguras e sustentáveis. Uma forma de contribuir é divulgar práticas de consumo responsável e economia de recursos, como água.

Neste desafio, você vai **transformar o app do Desafio 1** em um app com **várias páginas**. Em vez de tudo em uma tela só, você terá páginas separadas para: início, registro de consumo, histórico e dicas de economia de água. O Streamlit usa a pasta `pages/` para isso — cada arquivo `.py` vira um item no menu lateral.

## Requisitos técnicos mínimos

- Estrutura com pasta **pages/** e arquivos `.py` dentro
- Pelo menos **3 páginas**, por exemplo:
  - Página inicial (Home) com apresentação do app
  - Página de Registro (formulário para cadastrar consumo)
  - Página de Histórico (lista dos registros)
- Navegação funcionando pelo menu lateral
- Usar prefixos numéricos nos nomes dos arquivos (ex: `1_registro.py`, `2_historico.py`) para definir a ordem

## Critérios de conclusão

- [ ] O app tem pelo menos 3 páginas distintas
- [ ] O menu lateral mostra os links para cada página
- [ ] A navegação entre as páginas funciona ao clicar nos links
- [ ] A página de registro mantém a lógica do Desafio 1 (formulário + salvar)
- [ ] O histórico mostra os registros feitos na sessão
- [ ] O fluxo entre as páginas faz sentido para o usuário

## Sugestão de extensão

- Adicionar uma página de **Dicas** com orientações para economia de água
- Implementar **login simples** (veja [14-autenticacao](../../14-autenticacao)) para proteger algumas páginas
- Personalizar o visual com temas (veja [11-temas-configuracao](../../11-temas-configuracao))

## Exemplos que ajudam

Consulte estes exemplos do repositório para implementar o desafio:

- [10-multipaginas](../../10-multipaginas) – Estrutura de pastas, `pages/`, ordem das páginas e navegação no menu lateral
