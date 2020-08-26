from db import nova_conexao
from mysql.connector import ProgrammingError

listar_tabelas = """
    SHOW TABLES
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(listar_tabelas)
        for i, tables in enumerate(cursor, start=1):
            print(f'Table: {tables[0]}')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
