#!/usr/bin/python3
# Neste exemplo o arquivo e carregado em sua totalidade para a memoria
arquivo = open("pessoas.csv")
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print("Nome: {} Idade: {}".format(*registro.split(',')))
