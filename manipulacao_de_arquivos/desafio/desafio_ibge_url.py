#!/usr/bin/python3
# Desafio IBGE abrir o arquivo com o
# encoding ISO-8859-1
# ignorar a primeira linha
# pegar o quarto e nono campo.
# passando URL
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        arquivo = entrada.read().decode('latin1')
        with open("desafio-ibge_url.txt", mode="w") as saida:
            for linha in csv.reader(arquivo.splitlines()):
                print(f"{linha[3]} / {linha[8]}", file=saida)


if __name__ == "__main__":
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
