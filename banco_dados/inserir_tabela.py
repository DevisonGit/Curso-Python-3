from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos(nome, telefone) VALUES(%s, %s)'
dados = ('Devison', 957970234)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, dados)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
