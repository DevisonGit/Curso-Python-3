class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} \nIdade: {self.idade}'

    def is_adulto(self):
        return True if self.idade >= 18 else False


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario=0):
        super().__init__(nome, idade)
        self.salario = salario

    def __str__(self):
        return super().__str__() + f'\nSalario: {self.salario}'


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compras(self, compra):
        self.compras.append(compra)

    def ultima_compra(self):
        return self.compras[-1]

    def total_compras(self):
        return self.compras[-1]


class Compra():
    def __init__(self, Vendedor, data, valor):
        self.vendedor = Vendedor
        self.data = data
        self.valor = valor


if __name__ == "__main__":
    print('\nFuncionario')
    vendedor = Vendedor("Tiago", 35, 2500.56)
    print(vendedor)
    compra1 = Compra(vendedor, '01-02-2020', 2500)
    compra2 = Compra(vendedor, '01-03-2020', 1500)
    cliente = Cliente('Devison', 32)
    cliente.registrar_compras(compra1)
    cliente.registrar_compras(compra2)
    print('\nCliente:')
    print(cliente)
    print('\nCompras:')
    print(cliente.total_compras())
