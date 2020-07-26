class Data():
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'

    def str_ret(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 23
d1.mes = 7
d1.ano = 2020
print(d1)

d2 = Data()
d2.dia = 23
d2.mes = 7
d2.ano = 2020
print(d2.str_ret())
