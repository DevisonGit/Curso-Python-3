class Humano:
    #  Membro da classe
    especie = "Homo sapiens"

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = "Homo Neandertal"
        return self


if __name__ == "__main__":
    jose = Humano("jose")
    oa = Humano("Oa").das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {jose.especie}')
    print(f'Oa.especie: {oa.especie}')
