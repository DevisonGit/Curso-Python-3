
lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'Nome': 'Devison', 'Idade': 32},
    {'Nome': 'Daniele', 'Idade': 18},
    {'Nome': 'Dilma', 'Idade': 50},
    {'Nome': 'Ricardo', 'Idade': 50}
]

so_nome = map(lambda p: p['Nome'], lista_2)
print(list(so_nome))

so_idade = map(lambda p: p['Idade'], lista_2)
print(list(so_idade))

frase = map(lambda p: f'{p["Nome"]} tem {p["Idade"]}', lista_2)
print(list(frase))
