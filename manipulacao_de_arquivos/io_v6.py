#!/usr/bin/python3
# Neste exemplo gravamos os dados em um arquivo
with open("pessoas.csv") as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            dados = registro.strip().split(',')
            print("Nome: {} Idade: {}".format(*dados), file=saida)

if arquivo.closed:
    print("Arquivo fechado")
