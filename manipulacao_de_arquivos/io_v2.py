#!/usr/bin/python3
# Neste exemplo o arquivo e carregado por stream
arquivo = open("pessoas.csv")
for registro in arquivo:
    print("Nome: {} Idade: {}".format(*registro.split(',')))
arquivo.close()
