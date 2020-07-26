from datetime import datetime


class Projetos:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())})'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' ----> Concluida ' if self.feito else '')


def main():
    casa = Projetos('Tarefas de Casa')
    casa.add('limpar o guarda roupa')
    casa.add('lavar os pratos')
    print(casa)
    for tarefa in casa.tarefas:
        print(tarefa)
    print('\nLavei os pratos\n')
    casa.procurar('lavar os pratos').concluir()
    print(casa)
    for tarefa in casa.tarefas:
        print(tarefa)


if __name__ == "__main__":
    main()
