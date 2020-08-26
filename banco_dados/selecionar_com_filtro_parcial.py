from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos WHERE nome like "%da%"'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        for i in cursor:
            print(i)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
