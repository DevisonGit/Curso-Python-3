#!/usr/bin/python3
# Neste exemplo usamos o modulo csv
import csv

with open("pessoas.csv") as arquivo:
    with open("pessoas_v2.txt", "w") as saida:
        for registro in csv.reader(arquivo):
            print("Nome: {} Idade: {}".format(*registro), file=saida)

if arquivo.closed:
    print("Arquivo fechado")
