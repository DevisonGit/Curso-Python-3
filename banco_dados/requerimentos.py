try:
    from mysql import connector
except ModuleNotFoundError:
    print('Mysql connector nao instalado')
else:
    print('Mysql connector instalado e pronto')
