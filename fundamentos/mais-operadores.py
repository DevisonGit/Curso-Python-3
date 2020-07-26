# Operador membro

lista = [1, 2, "Ana", "Brasil"]
print(2 in lista)
print("Ana" in lista)  # Esta na lista?
print("Ana" not in lista)  # Nao esta na lista?

print("\n")
# Operador identidade

a = 3
b = a
c = 3

print(a is b)
print(a is b)
print(b is c)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_a is not lista_c)
print(lista_b is lista_c)
