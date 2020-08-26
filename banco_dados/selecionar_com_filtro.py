from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos WHERE nome = "Dilma"'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchone()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(contatos)
