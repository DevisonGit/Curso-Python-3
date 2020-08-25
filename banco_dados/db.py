from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmananger

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='@gu@^&*(',
    auth_plugin='mysql_native_password'
)


@contextmananger
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_conmected()):
            conexao.close()
