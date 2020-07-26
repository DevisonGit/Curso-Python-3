#!/usr/bin/python3
# usando import
import math


def calcular(raio):
    area = math.pi * float(raio) ** 2
    print('Area do circulo', area)


if __name__ == '__main__':
    raio = input("Informe o raio: ")
    calcular(raio)
