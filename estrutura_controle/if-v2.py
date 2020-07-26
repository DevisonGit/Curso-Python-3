def faixa_etaria(idade):
    if idade in (0, 18):
        return "Menor de idade"
    if idade in (19, 65):
        return "Adulto"
    if idade in (65, 100):
        return "Melhor idade"
    if idade >= 100:
        return "Centenario"


if __name__ == '__main__':
    idades = (17, 25, 65, 150)
    for idade in idades:
        print(f"{idade}: {faixa_etaria(idade)}")
