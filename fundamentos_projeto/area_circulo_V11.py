#!/usr/bin/python3
# usando import
import math
import sys


def calcular(raio):
    return math.pi * float(raio) ** 2


def imprimir(area):
    print('Area do circulo', area)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Esta faltando o valor do raio")
        print(f"Sintaxe: {sys.argv[0]} 12")
    else:
        imprimir(calcular(sys.argv[1]))
