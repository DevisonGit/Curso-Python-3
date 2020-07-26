# Percorrendo um dicionario
produto = {"nome": "caneta", "marca": "bic", "preco": 1.50, "estoque": 1500}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')
