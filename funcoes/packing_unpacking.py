def soma_n(*numeros):
    soma = 0
    for i in numeros:
        soma += i
    return soma


if __name__ == "__main__":
    # packing empacota para um tipo especifico
    print(soma_n(1, 2, 3, 4))

    # unpacking desempacota um tipo
    tupla_numeros = (1, 2, 3, 4)
    print(soma_n(*tupla_numeros))
