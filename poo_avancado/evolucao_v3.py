class Humano:
    #  Membro da classe
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def das_cavernas(self):
        self.especie = "Homo Neandertal"
        return self

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade deve ser um valor positivo")
        self._idade = idade

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandertal', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neandertal(Humano):
    especie = Humano.especies()[-2]


class Sapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = Sapiens("Jose")
    jose.set_idade(40)
    print(f'Nome {jose.nome} Idade {jose.get_idade()}')
