"""
Funções para conectar ao Supabase e fazer operações no banco.

Este módulo contém funções simples (sem classes) para:
- Verificar se as credenciais estão configuradas
- Obter o cliente Supabase (conexão)
- Buscar todos os itens (SELECT)
- Inserir um novo item (INSERT)
- Deletar um item pelo id (DELETE)
"""

import os
import streamlit as st
from supabase import create_client


def _obter_credenciais():
    """
    Função interna que busca URL e chave do Supabase.
    Retorna (url, key) ou (None, None) se não estiverem configuradas.
    """
    url = None
    key = None
    try:
        if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
            url = st.secrets["SUPABASE_URL"]
            key = st.secrets["SUPABASE_KEY"]
    except (KeyError, AttributeError, TypeError):
        pass
    if not url:
        url = os.environ.get("SUPABASE_URL")
    if not key:
        key = os.environ.get("SUPABASE_KEY")
    return (url, key)


def credenciais_configuradas():
    """
    Verifica se SUPABASE_URL e SUPABASE_KEY estão configurados.
    Busca em st.secrets ou variáveis de ambiente.
    Retorna True se estiverem ok, False caso contrário.
    """
    url, key = _obter_credenciais()
    return bool(url and key)


def obter_cliente():
    """
    Cria e retorna o cliente Supabase conectado ao projeto.

    As credenciais vêm de st.secrets (Streamlit) ou de variáveis de ambiente.
    Retorna None se as credenciais não estiverem configuradas ou houver erro.
    """
    try:
        url, key = _obter_credenciais()
        if not url or not key:
            return None

        # create_client é a função da biblioteca supabase para criar a conexão
        cliente = create_client(url, key)
        return cliente

    except Exception as erro:
        # Em caso de qualquer erro (rede, credencial inválida etc), retorna None
        # Log opcional para debug: print(erro) ou import logging; logging.exception(erro)
        return None


def buscar_itens():
    """
    Busca todos os itens da tabela 'itens' no Supabase.

    Faz um SELECT * na tabela.
    Retorna uma lista de dicionários (cada um é uma linha) ou lista vazia se der erro.
    """
    try:
        cliente = obter_cliente()
        if cliente is None:
            return []

        # .table("itens") aponta para a tabela chamada "itens"
        # .select("*") significa "pegue todas as colunas"
        resposta = cliente.table("itens").select("*").execute()

        dados = resposta.data if resposta.data else []
        return dados

    except Exception as erro:
        # Log opcional para debug: print(erro)
        return []


def inserir_item(nome):
    """
    Insere um novo item na tabela 'itens'.

    Parâmetros:
        nome: texto com o nome do item a ser salvo

    Retorna True se inseriu com sucesso, False se deu erro.
    """
    try:
        cliente = obter_cliente()
        if cliente is None:
            return False

        dados = {
            "nome": str(nome).strip(),
        }

        cliente.table("itens").insert(dados).execute()
        return True

    except Exception as erro:
        # Log opcional para debug: print(erro)
        return False


def deletar_item(id_item):
    """
    Remove um item da tabela 'itens' pelo id.

    Parâmetros:
        id_item: o id (UUID) do item a ser removido

    Retorna True se deletou com sucesso, False se deu erro.
    """
    try:
        cliente = obter_cliente()
        if cliente is None:
            return False

        # .eq("id", id_item) significa "onde a coluna id é igual a id_item"
        # .execute() envia o comando DELETE para o banco
        cliente.table("itens").delete().eq("id", id_item).execute()
        return True

    except Exception as erro:
        # Log opcional para debug: print(erro)
        return False
