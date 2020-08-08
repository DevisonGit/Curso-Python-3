class Humano:
    #  Membro da classe
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = "Homo Neandertal"
        return self

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
    oa = Neandertal("Oa")
    print(f'Evolucao classe: {", ".join(Sapiens.especies())}')
    print(f'Evolucao instancia: {", ".join(jose.especies()) }')
    print(f'Jose especie: {jose.especie}')
    print(f'Oa especie: {oa.especie}')
    print(f'Jose e evoluido? {jose.is_evoluido()}')
    print(f'Oa e evoluido? {oa.is_evoluido()}')
