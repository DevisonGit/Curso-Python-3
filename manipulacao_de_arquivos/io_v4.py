#!/usr/bin/python3
# Neste exemplo o arquivo e carregado por stream e usamos o try / finally
# O finally sempre e executado independente de erros
try:
    arquivo = open("pessoas.csv")
    for registro in arquivo:
        print("Nome: {} Idade: {}".format(*registro.strip().split(',')))
finally:
    arquivo.close()
    print("Arquivo fechado")
