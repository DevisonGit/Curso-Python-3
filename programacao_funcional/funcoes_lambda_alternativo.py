compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)


def calc_preco_totais(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(map(calc_preco_totais, compras))

print('Precos totais: ', totais)
print('Total geral', sum(totais))
