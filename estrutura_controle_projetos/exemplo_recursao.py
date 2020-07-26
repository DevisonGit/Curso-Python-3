def recursao(maximo, atual):
    if atual <= maximo:
        print(atual)
        recursao(maximo, atual + 1)
    return


recursao(10, 1)
