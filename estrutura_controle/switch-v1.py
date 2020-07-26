# Python nao tem switch nativamente porem podemos simular com o dicionario


def dia_Da_semana(dia):
    dias = {1: "Domingo",
            2: "Segunda",
            3: "Terca",
            4: "Quarta",
            5: "Quinta",
            6: "Sexta",
            7: "Sabado"
            }
    return dias.get(dia, "** dia invalido*")


if __name__ == '__main__':
    for i in range(0, 9):
        print(f'{dia_Da_semana(i)}')
