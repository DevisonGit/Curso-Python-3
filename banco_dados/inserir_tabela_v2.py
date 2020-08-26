from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'INSERT INTO contatos(nome, telefone) VALUES(%s, %s)'
dados = (
    ('Devison', 957970234),
    ('Ana', 957970234),
    ('Julia', 957970234),
    ('Dani', 957970234),
    ('Ricardo', 957970234),
    ('Dilma', 957970234),

)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, dados)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
