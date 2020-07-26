#  Percorrendo uma string
string = "ola eu sou o Goku"
for letra in string:
    print(f'{letra}', end='*')
print("\n")

# Percorrendo uma lista
lista_aprovados = ["Devison", "Dani", "Luan", "Romito"]
for nome in lista_aprovados:
    print(f'{nome}')
print("\n")

# Percorrendo uma lista com enumerate
lista_aprovados = ["Devison", "Chaves", "Naruto", "Junior"]
for indice, nome in enumerate(lista_aprovados):
    print(f'{indice + 1}) {nome}')
print("\n")

# Percorrendo um tupla
dias_da_semana = ('domingo', 'segunda', 'terca',
                  'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_da_semana:
    print(f'Hoje e {dia}')
print("\n")

# Percorrendo um set
for letra in set("hoje e dia"):
    print(f'{letra}')
