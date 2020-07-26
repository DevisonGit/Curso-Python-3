#!/usr/bin/python3
# usando import
import math
import sys


def calcular(raio):
    return math.pi * float(raio) ** 2


def imprimir(area):
    print('Area do circulo', area)


if __name__ == '__main__':
    imprimir(calcular(sys.argv[1]))
