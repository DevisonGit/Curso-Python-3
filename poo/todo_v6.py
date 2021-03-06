from datetime import datetime, timedelta


class Projetos:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def __add_nova_tarefa(self, descricao, vencimento=None, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self.__add_tarefa if isinstance(tarefa, Tarefa)\
            else self.__add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __iter__(self):
        return self.tarefas.__iter__()

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())})'


class Tarefa:
    def __init__(self, descricao, vencimento):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('Concluida')
        elif self.vencimento:
            if self.vencimento < datetime.now():
                status.append('Vencida')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'Vence em {dias} dias')
        return f'{self.descricao} ' + ' '.join(status)


class TarefasRecorrentes(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefasRecorrentes(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projetos('Tarefas de Casa')
    casa.add('limpar o guarda roupa', datetime.now())
    casa.add('lavar os pratos', datetime.now() + timedelta(days=5))
    casa.add(TarefasRecorrentes('Lavar roupas', datetime.now(), 7))
    casa.add(casa.procurar('Lavar roupas').concluir())
    print(casa)
    for tarefa in casa:
        print(tarefa)
    print('\nLavei os pratos\n')
    casa.procurar('lavar os pratos').concluir()
    print(casa)
    for tarefa in casa:
        print(tarefa)


if __name__ == "__main__":
    main()
