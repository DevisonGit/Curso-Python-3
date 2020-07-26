from random import randint

numero_informado = -1
numero_aleatorio = randint(0, 9)

while numero_informado != numero_aleatorio:
    numero_informado = int(input("Informe o numero: "))

print(f'O numero aleatorio {numero_aleatorio} foi encontrado')
