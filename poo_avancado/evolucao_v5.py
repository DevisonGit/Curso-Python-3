class Humano:
    #  Membro da classe
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def das_cavernas(self):
        self.especie = "Homo Neandertal"
        return self

    @property
    def inteligencia(self):
        raise NotImplementedError("Propriedade nao implementada")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
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

    @property
    def inteligencia(self):
        return False


class Sapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligencia(self):
        return True


if __name__ == "__main__":
    anonimo = Humano("John")

    try:
        print(anonimo.inteligencia)
    except NotImplementedError:
        print("proprieda abstrata")
    jose = Sapiens("Jose")
    print('{} classe {} inteligente {}'
          .format(jose.nome, jose.__class__.__name__, jose.inteligencia))
    oa = Neandertal("Oa")
    print('{} classe {} inteligente {}'
          .format(oa.nome, oa.__class__.__name__, oa.inteligencia))
