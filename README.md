# Exemplos de Streamlit – TechSchool

Este repositório contém **exemplos de aplicações em Streamlit** para ensinar programação para crianças e adolescentes (8 a 18 anos). Cada exemplo fica em uma pasta separada, com código comentado e documentação em português.

## Estrutura do projeto

Cada pasta tem um número e um nome que indica o tema:

| Pasta                                                  | Conteúdo                                                                                              |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| [01-instalacao](01-instalacao)                         | Como instalar Python e o Streamlit                                                                    |
| [02-fundamentos](02-fundamentos)                       | Primeiro app e conceitos básicos                                                                      |
| [03-conceitos](03-conceitos)                           | Modelo de execução, layout e organização                                                              |
| [04-texto-e-exibicao](04-texto-e-exibicao)             | Títulos, texto, markdown e exibição de informações                                                    |
| [05-widgets-input](05-widgets-input)                   | Botões, sliders, caixas de texto e outros controles                                                   |
| [06-formularios-validacao](06-formularios-validacao)   | Formulários e validação de dados                                                                      |
| [07-imagens-midias](07-imagens-midias)                 | Imagens, áudio e vídeo                                                                                |
| [08-dados-tabelas](08-dados-tabelas)                   | Tabelas e dados                                                                                       |
| [09-graficos](09-graficos)                             | Gráficos e mapas                                                                                      |
| [10-multipaginas](10-multipaginas)                     | Apps com várias páginas                                                                               |
| [11-temas-configuracao](11-temas-configuracao)         | Cores, temas e configuração                                                                           |
| [12-llm-chat](12-llm-chat)                             | Uso com LLMs e chat                                                                                   |
| [13-google-sheets](13-google-sheets)                   | Usar Google Sheets como banco de dados                                                                |
| [14-autenticacao](14-autenticacao)                     | Login e senha (exemplo mais avançado)                                                                 |
| [15-supabase-basico](15-supabase-basico)               | Conectar ao Supabase (banco de dados na nuvem)                                                        |
| [16-deploy-streamlit-cloud](16-deploy-streamlit-cloud) | Deploy na internet com Streamlit Community Cloud                                                      |
| [20-mvp-template](20-mvp-template)                     | Template MVP com login, dashboard e Supabase                                                          |
| [22-exemplo-technovation](22-exemplo-technovation)     | Exemplo ODS 12 – Redução de desperdício alimentar                                                     |
| [23-desafios-progressivos](23-desafios-progressivos)   | Conjunto de 5 desafios progressivos com temas ODS (app local, multipágina, Supabase, métricas, pitch) |

## Como usar

1. **Instalação:** Siga o [01-instalacao/README.md](01-instalacao/README.md) para instalar Python e o Streamlit.
2. **Rodar um exemplo:** Entre na pasta do exemplo, instale as dependências e execute:
   ```bash
   cd 02-fundamentos
   pip install -r requirements.txt
   streamlit run app.py
   ```
3. O navegador abrirá o app. Cada pasta tem seu próprio **README.md** (Objetivo, Conceitos ensinados, Como executar) e **requirements.txt** com as dependências necessárias.

## O que é o requirements.txt?

O **requirements.txt** é um arquivo de texto que lista as **bibliotecas** (peças de código prontas) que um exemplo precisa para funcionar. Pense nele como uma "lista de compras": em vez de procurar cada biblioteca na internet, você usa um único comando e o Python instala tudo de uma vez.

- **Para que serve:** Garante que seu computador tenha as mesmas bibliotecas que o exemplo usa (por exemplo, Streamlit para criar o app, pandas para trabalhar com tabelas).
- **Como usar:** Dentro da pasta do exemplo, execute `pip install -r requirements.txt` antes de rodar o app. O comando lê a lista e instala cada item automaticamente.
- **Onde fica:** Cada pasta de exemplo tem seu próprio **requirements.txt**, porque alguns exemplos precisam de bibliotecas extras (como Supabase ou Google Sheets).

## Desafios individuais

Dentro de [23-desafios-progressivos](23-desafios-progressivos) há 5 desafios para praticar:

| Desafio   | Tema                 | Link                                                                    |
| --------- | -------------------- | ----------------------------------------------------------------------- |
| Desafio 1 | App local (ODS 6)    | [desafio-1-app-local](23-desafios-progressivos/desafio-1-app-local)     |
| Desafio 2 | Multipágina (ODS 11) | [desafio-2-multipagina](23-desafios-progressivos/desafio-2-multipagina) |
| Desafio 3 | Supabase (ODS 13)    | [desafio-3-supabase](23-desafios-progressivos/desafio-3-supabase)       |
| Desafio 4 | Métricas (ODS 3)     | [desafio-4-metricas](23-desafios-progressivos/desafio-4-metricas)       |
| Desafio 5 | Pitch (ODS 4)        | [desafio-5-pitch](23-desafios-progressivos/desafio-5-pitch)             |

## Documentação do Streamlit

Os exemplos seguem a documentação oficial: [https://docs.streamlit.io/](https://docs.streamlit.io/)

## Licença

Consulte o arquivo [LICENSE](LICENSE) deste repositório.
