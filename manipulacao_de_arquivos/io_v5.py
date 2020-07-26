#!/usr/bin/python3
# Neste exemplo o with que sempre fecha o arquivo

with open("pessoas.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {} Idade: {}".format(*registro.strip().split(',')))

if arquivo.closed:
    print("Arquivo fechado")
