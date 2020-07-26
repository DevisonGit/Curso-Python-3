#!/usr/bin/python3
# usando import
import math
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


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
        print(TerminalColor.ERRO + "Valor do raio deve ser numerico" +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    imprimir(calcular(sys.argv[1]))
