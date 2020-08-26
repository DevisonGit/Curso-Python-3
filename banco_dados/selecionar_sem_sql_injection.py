from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'SELECT * FROM contatos WHERE nome like %s'

with nova_conexao() as conexao:
    try:
        nome = input('Contato a localizar: ')
        args = (f'%{nome}%',)
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        for i in cursor:
            print(i)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
