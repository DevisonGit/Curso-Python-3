from db import nova_conexao
from mysql.connector import ProgrammingError


tabela_contato = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),
        telefone VARCHAR(20)
    )
"""

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contato)
        cursor.execute(tabela_emails)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
