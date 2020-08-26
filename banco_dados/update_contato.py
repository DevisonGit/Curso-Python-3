from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'

with nova_conexao() as conexao:
    try:
        id_atz = input('Id a ser atualizado: ')
        nome_atz = input('Novo nome: ')
        args = (f'{nome_atz}', f'{id_atz}',)
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros atualizados')
