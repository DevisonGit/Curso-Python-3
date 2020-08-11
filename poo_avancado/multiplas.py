class Animal():
    @property
    def capacidades(self):
        return('comer', 'beber', 'dormir')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades \
            + ('bater em bandidos', 'atirar teias em predio')


if __name__ == "__main__":
    john = Homem()
    print(f'Homem {john.capacidades}')
    aranha = Aranha()
    print(f'Aranha {aranha.capacidades}')
    peter = HomemAranha()
    print(f'Homem Aranha {peter.capacidades}')
