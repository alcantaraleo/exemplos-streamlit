"""
Funções para conectar ao Supabase e fazer operações no banco.

Este módulo contém funções simples (sem classes) para:
- Obter o cliente Supabase (conexão)
- Buscar todos os registros (SELECT)
- Inserir um novo registro (INSERT)
"""

import os
import streamlit as st
from supabase import create_client


@st.cache_resource
def obter_cliente():
    """
    Cria e retorna o cliente Supabase conectado ao projeto.

    O @st.cache_resource faz o Streamlit guardar (cachear) o cliente em memória.
    Assim, o cliente é criado apenas uma vez e reutilizado em todas as interações,
    economizando tempo e recursos de rede. É como guardar um brinquedo em uma caixa
    próxima, em vez de buscar no armário toda vez que precisar usar.

    As credenciais vêm de st.secrets (Streamlit) ou de variáveis de ambiente.
    Retorna None se as credenciais não estiverem configuradas ou houver erro.
    """
    try:
        # Tenta primeiro pegar do Streamlit secrets (padrão para apps Streamlit)
        url = None
        key = None
        try:
            if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
                url = st.secrets["SUPABASE_URL"]
                key = st.secrets["SUPABASE_KEY"]
        except (KeyError, AttributeError, TypeError):
            pass

        # Se não estiver no secrets, tenta variáveis de ambiente (ex.: arquivo .env)
        if not url:
            url = os.environ.get("SUPABASE_URL")
        if not key:
            key = os.environ.get("SUPABASE_KEY")

        # Se ainda não tiver as duas variáveis, não conseguimos conectar
        if not url or not key:
            return None

        # create_client é a função da biblioteca supabase para criar a conexão
        cliente = create_client(url, key)
        return cliente

    except Exception:
        # Em caso de qualquer erro (rede, credencial inválida etc), retorna None
        # Assim evitamos que o app quebre e podemos mostrar mensagem amigável
        return None


def buscar_registros():
    """
    Busca todos os registros da tabela 'registros' no Supabase.

    Faz um SELECT * na tabela.
    Retorna uma lista de dicionários (cada um é uma linha),
    lista vazia [] se a tabela não tiver dados,
    ou None se ocorreu um erro de conexão/banco.

    Distinguir None (erro) de [] (tabela vazia) ajuda a mostrar
    mensagens diferentes para o usuário.
    """
    try:
        # Obtém o cliente conectado
        cliente = obter_cliente()
        if cliente is None:
            return None

        # .table("registros") aponta para a tabela chamada "registros"
        # .select("*") significa "pegue todas as colunas"
        # .execute() envia a query para o banco e espera a resposta
        resposta = cliente.table("registros").select("*").execute()

        # resposta.data contém a lista de linhas retornadas
        # Cada linha é um dicionário com os nomes das colunas como chaves
        dados = resposta.data if resposta.data else []
        return dados

    except Exception:
        # Em caso de erro (tabela não existe, sem permissão, etc), retornamos None
        # Isso permite que o app mostre uma mensagem de erro específica
        return None


def inserir_registro(nome, valor):
    """
    Insere um novo registro na tabela 'registros'.

    Parâmetros:
        nome: texto com o nome a ser salvo
        valor: número a ser salvo (será convertido para float)

    Retorna True se inseriu com sucesso, False se deu erro.
    """
    try:
        # Obtém o cliente conectado
        cliente = obter_cliente()
        if cliente is None:
            return False

        # Preparamos os dados: dicionário com nomes das colunas e valores
        # O id é gerado automaticamente pelo banco (UUID), não precisamos enviar
        dados = {
            "nome": str(nome).strip(),
            "valor": float(valor),
        }

        # .table("registros") aponta para a tabela
        # .insert(dados) adiciona uma nova linha com esses dados
        # .execute() envia o comando para o banco
        cliente.table("registros").insert(dados).execute()

        # Se chegou aqui, não deu exceção, então deu certo
        return True

    except Exception:
        # Em caso de erro, retornamos False
        # O app pode mostrar st.error() com mensagem amigável
        return False
