from .pessoa import Pessoa


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=0):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return super().__str__() + f'\nSalario: {self.salario}'
