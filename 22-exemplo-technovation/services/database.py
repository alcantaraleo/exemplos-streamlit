"""
Serviço de banco de dados para o projeto ODS 12 - Redução de desperdício alimentar.

Este módulo cuida de TODA a comunicação com o banco de dados.
Usamos SQLite: um banco de dados em arquivo, simples e que não precisa de instalação.
Assim, o app funciona em qualquer computador sem configuração extra.

Responsabilidades:
- Criar a tabela de alimentos desperdiçados (se não existir)
- Inserir novos registros de desperdício
- Buscar todos os registros para listagem e gráficos
- Calcular o total desperdiçado
"""

import logging
import sqlite3
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


def _caminho_banco():
    """
    Retorna o caminho do arquivo do banco de dados.
    O banco fica na pasta do projeto, com nome 'desperdicio.db'.
    """
    # Path(__file__) é o caminho deste arquivo (database.py)
    # .parent.parent sobe duas pastas: services -> 22-exemplo-technovation
    pasta_projeto = Path(__file__).parent.parent
    return pasta_projeto / "desperdicio.db"


def _conectar():
    """
    Cria uma conexão com o banco SQLite.
    Retorna o objeto de conexão para usar nas queries.
    """
    caminho = _caminho_banco()
    return sqlite3.connect(str(caminho))


def _converter_linha(linha):
    """
    Converte uma linha do SQLite (tupla) em um dicionário.
    Fica mais fácil de usar no resto do código.
    """
    return {
        "id": linha[0],
        "nome": linha[1],
        "quantidade": linha[2],
        "data": linha[3],
    }


def criar_tabela_se_nao_existir():
    """
    Cria a tabela 'desperdicio' no banco se ela ainda não existir.

    Colunas:
    - id: número único de cada registro (gerado automaticamente)
    - nome: nome do alimento desperdiçado (ex: "banana", "arroz")
    - quantidade: quanto foi desperdiçado (em gramas, unidades, etc.)
    - data: data e hora em que foi registrado
    """
    con = None
    try:
        # Primeiro criamos a conexão aqui dentro: se der erro, não tentamos fechar algo que não foi aberto
        con = _conectar()
        # SQL para criar a tabela. IF NOT EXISTS evita erro se já existir.
        sql = """
        CREATE TABLE IF NOT EXISTS desperdicio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade REAL NOT NULL,
            data TEXT NOT NULL
        )
        """
        con.execute(sql)
        con.commit()
    finally:
        if con is not None:
            con.close()


def inserir_registro(nome, quantidade):
    """
    Insere um novo registro de alimento desperdiçado no banco.

    Parâmetros:
        nome: nome do alimento (ex: "maçã", "pão")
        quantidade: quanto foi desperdiçado (número, ex: 500 para 500 gramas)

    Retorna True se salvou com sucesso, False se deu erro.
    """
    criar_tabela_se_nao_existir()

    try:
        con = _conectar()
        try:
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO desperdicio (nome, quantidade, data) VALUES (?, ?, ?)"
            con.execute(sql, (nome.strip(), float(quantidade), data_atual))
            con.commit()
            return True
        finally:
            con.close()
    except Exception as erro:
        logger.exception("Erro ao inserir registro de desperdício: %s", erro)
        return False


def buscar_todos_registros():
    """
    Busca todos os registros de desperdício salvos no banco.

    Retorna uma lista de dicionários. Cada dicionário tem:
    - id, nome, quantidade, data

    Retorna lista vazia se não houver registros ou se der erro.
    """
    criar_tabela_se_nao_existir()

    try:
        con = _conectar()
        try:
            # ORDER BY data DESC = mais recentes primeiro
            cursor = con.execute(
                "SELECT id, nome, quantidade, data FROM desperdicio ORDER BY data DESC"
            )
            linhas = cursor.fetchall()
            return [_converter_linha(linha) for linha in linhas]
        finally:
            con.close()
    except Exception as erro:
        logger.exception("Erro ao buscar registros: %s", erro)
        return []


def calcular_total_desperdicado():
    """
    Soma a quantidade de todos os registros de desperdício.

    Retorna um número (a soma) ou 0 se não houver registros.
    """
    criar_tabela_se_nao_existir()

    try:
        con = _conectar()
        try:
            cursor = con.execute("SELECT SUM(quantidade) FROM desperdicio")
            resultado = cursor.fetchone()[0]
            return resultado if resultado is not None else 0
        finally:
            con.close()
    except Exception as erro:
        logger.exception("Erro ao calcular total: %s", erro)
        return 0


def buscar_dados_para_grafico():
    """
    Busca os dados agrupados por data para montar o gráfico de evolução.

    Retorna uma lista de dicionários com 'data' e 'total' (soma do dia).
    Útil para st.line_chart ou st.bar_chart mostrar a evolução ao longo do tempo.
    """
    criar_tabela_se_nao_existir()

    try:
        con = _conectar()
        try:
            # Agrupa por data (só a parte da data, sem horário) e soma as quantidades
            sql = """
            SELECT date(data) as dia, SUM(quantidade) as total
            FROM desperdicio
            GROUP BY date(data)
            ORDER BY dia
            """
            cursor = con.execute(sql)
            linhas = cursor.fetchall()
            return [{"data": str(linha[0]), "total": linha[1]} for linha in linhas]
        finally:
            con.close()
    except Exception as erro:
        logger.exception("Erro ao buscar dados para gráfico: %s", erro)
        return []
