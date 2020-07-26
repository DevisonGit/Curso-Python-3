#!/usr/bin/python3
# usando import
import math
import sys
import errno


def calcular(raio):
    return math.pi * float(raio) ** 2


def imprimir(area):
    print('Area do circulo', area)


def help():
    print("Esta faltando o valor do raio")
    print(f"Sintaxe: {sys.argv[0]} <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print("Valor do raio deve ser numerico")
        sys.exit(errno.EINVAL)

    imprimir(calcular(sys.argv[1]))
