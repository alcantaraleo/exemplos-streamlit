# 17 – App com Página Secreta (Easter Egg)

## Objetivo

Este exemplo ensina a criar um **app que esconde uma página especial**! Na tela, o usuário vê um diário normal onde pode escrever, salvar, editar e deletar entradas. Mas existe um segredo: clicando várias vezes em um elemento na interface, uma **página escondida** é revelada.

## Conceitos ensinados

- **Menu customizado**: Desabilitar o menu padrão e criar um menu que mostra só o que você quiser
- **Página invisível**: Uma página que não aparece no menu e só pode ser acessada de forma especial
- **Redirecionamento programático**: Usar `st.switch_page()` para ir de uma página a outra pelo código
- **Contagem de cliques**: Usar `st.session_state` para contar cliques e disparar uma ação
- **Easter egg**: Um elemento escondido na interface que recompensa quem descobre

## Como executar

```bash
cd 17-pagina-secreta
pip install -r requirements.txt
streamlit run app.py
```

## Como descobrir o segredo

1. Abra o app e use o diário normalmente (escreva, salve, edite entradas)
2. Procure um elemento que parece parte do design do diário...
3. Clique nele **várias vezes** (5 vezes)
4. Você será redirecionado para a página secreta!
5. Na página secreta, use o botão vermelho **SAIR** para voltar ao diário

## Estrutura desta pasta

```
17-pagina-secreta/
  app.py                    <- Página do diário (o que o usuário vê primeiro)
  menu.py                   <- Menu customizado (só mostra "Meu Diário")
  pages/
    app_real.py             <- Página secreta (não aparece no menu!)
  .streamlit/
    config.toml             <- Desabilita o menu nativo
  README.md
  requirements.txt
```

## Como funciona

- **config.toml**: `showSidebarNavigation = false` esconde o menu padrão do Streamlit
- **menu.py**: Cria um menu manual mostrando só o link "Meu Diário"
- **app.py**: Diário funcional + ícone que, ao receber X cliques, redireciona para a página secreta
- **pages/app_real.py**: Página que não tem link no menu; só é acessível pelo easter egg

O número de cliques necessários está em `app.py` na constante `CLIQUES_PARA_PAGINA_SECRETA` (padrão: 5).

## Observação

A página secreta pode ser acessada diretamente pela URL se alguém souber o endereço. Isso é normal para um easter egg — o objetivo é a diversão de descobrir, não segurança de dados.
