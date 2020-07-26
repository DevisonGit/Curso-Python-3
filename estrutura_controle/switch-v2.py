# Python nao tem switch nativamente porem podemos simular com o dicionario


def dia_Da_semana(dia):
    dias = {1: "fim de semana",
            2: "util",
            3: "util",
            4: "util",
            5: "util",
            6: "util",
            7: "fim de semana"
            }
    return dias.get(dia, "** dia invalido*")


if __name__ == '__main__':
    for i in range(0, 9):
        print(f'{dia_Da_semana(i)}')
