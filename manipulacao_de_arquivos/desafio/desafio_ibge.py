#!/usr/bin/python3
# Desafio IBGE abrir o arquivo com o
# encoding ISO-8859-1
# ignorar a primeira linha
# pegar o quarto e nono campo.
import csv

with open("desafio-ibge.csv", encoding='ISO-8859-1') as arquivo:
    with open("desafio-ibge.txt", mode="w") as saida:
        for linha in arquivo:
            print("{3} / {8}".format(*dado), file=saida)
