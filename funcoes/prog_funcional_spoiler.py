def executar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print("Bom dia")


def boa_tarde():
    print("Boa tarde")


def boa_noite():
    print("Boa noite")


if __name__ == "__main__":
    executar(bom_dia)
    executar(boa_tarde)
    executar(boa_noite)
