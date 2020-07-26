def calcula_imposto(preco_bruto, calcula_imposto, *params):
    return preco_bruto + preco_bruto * calcula_imposto(*params)


def imposto_importado(importado):
    return 0.10 if importado else 0.05


def imposto_explsivo(explosivo, fator_multiplicacao=1):
    return 0.10 * fator_multiplicacao if explosivo \
        else 0.05 * fator_multiplicacao


if __name__ == "__main__":
    print("Imposto de produto normal: ",
          calcula_imposto(1000, imposto_importado, False))
    print("Imposto de produto Importado: ",
          calcula_imposto(1000, imposto_importado, True))
    print("Imposto de produto nao explosivo: ",
          calcula_imposto(1000, imposto_explsivo, False, 1.5))
    print("Imposto de produto explosivo: ",
          calcula_imposto(1000, imposto_explsivo, True, 1.5))
