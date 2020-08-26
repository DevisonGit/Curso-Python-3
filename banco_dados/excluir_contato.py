from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'DELETE FROM contatos WHERE id = %s'

with nova_conexao() as conexao:
    try:
        id_excluir = input('Id a ser exluido: ')
        args = (f'{id_excluir}',)
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
