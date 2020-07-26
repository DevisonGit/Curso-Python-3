from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' Concluida ' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('limpar o guarda roupa'))
    casa.append(Tarefa('Lavar os pratos'))
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lava pratos']
    for tarefa in casa:
        print(f'{tarefa}')


if __name__ == "__main__":
    main()
