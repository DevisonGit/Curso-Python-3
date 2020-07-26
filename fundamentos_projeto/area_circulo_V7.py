#!/usr/bin/python3
# usando import
import math

if __name__ == '__main__':
    raio = input("Informe o raio: ")
    area = math.pi * float(raio) ** 2
    print('Area do circulo', area)
    print("Modulo:", __name__)
