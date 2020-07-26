class Data():
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    def str_ret(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
print(d1)

d2 = Data(25, 1, 1988)
print(d2.str_ret())
