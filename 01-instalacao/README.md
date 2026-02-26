# 01 – Instalação de Python e Streamlit

Nesta pasta você encontra **instruções claras** para instalar o Python e o Streamlit no seu computador. Depois disso, você poderá rodar todos os exemplos deste repositório.

## O que você vai precisar

- Um computador (Windows, Mac ou Linux).
- Acesso à internet para baixar o Python e instalar o Streamlit.

## Passo 1: Instalar o Python

O **Python** é a linguagem de programação que o Streamlit usa. Precisamos instalá-lo primeiro.

### No Windows

1. Acesse o site: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clique em **"Download Python"** (versão 3.10 ou mais nova).
3. Abra o arquivo que foi baixado e **marque a opção** "Add Python to PATH" no início da instalação.
4. Clique em **"Install Now"** e espere terminar.
5. Para conferir se deu certo, abra o **Prompt de Comando** (cmd) e digite:
   ```bash
   python --version
   ```
   Deve aparecer algo como: `Python 3.10.x` ou `Python 3.12.x`.

### No Mac

1. Acesse [https://www.python.org/downloads/](https://www.python.org/downloads/) e baixe a versão mais recente para Mac.
2. Abra o instalador e siga os passos.
3. Para conferir, abra o **Terminal** e digite:
   ```bash
   python3 --version
   ```

### No Linux (Ubuntu/Debian)

Abra o Terminal e digite:

```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

## Passo 2: Instalar o Streamlit

O **Streamlit** é uma biblioteca que permite criar aplicativos web em Python de forma simples.

1. Abra o **Terminal** (Mac/Linux) ou **Prompt de Comando** (Windows).
2. Digite o comando abaixo e pressione Enter:

   ```bash
   pip install streamlit
   ```

   No Mac ou Linux, se der erro de permissão, use:

   ```bash
   pip3 install streamlit
   ```

3. Espere a instalação terminar. Quando aparecer "Successfully installed streamlit...", está pronto.

## Passo 3: Testar se funcionou

1. Entre na pasta deste exemplo:
   ```bash
   cd 01-instalacao
   ```
2. Rode o aplicativo de teste:
   ```bash
   streamlit run app.py
   ```
3. O navegador deve abrir sozinho com uma página mostrando **"Olá! Sua instalação funcionou!"**. Se isso acontecer, está tudo certo.

## Estrutura desta pasta

- **README.md** – Este arquivo (instruções de instalação).
- **app.py** – Um aplicativo bem simples só para testar se o Streamlit está funcionando.

## Próximo passo

Depois de instalar e testar, vá para a pasta [02-fundamentos](../02-fundamentos) para criar seu primeiro app de verdade e aprender os conceitos básicos do Streamlit.
