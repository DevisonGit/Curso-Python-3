lista = []
print(type(lista))
lista.append(1)
lista.append(2)
print(lista)

nova_lista = [1, 2, "teste", [1, 2.3]]
print(nova_lista)
nova_lista.remove(2)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)
print(len(nova_lista))

outra_lista = [1, 2, "teste", "123", 3.1415]
print(outra_lista)
print(outra_lista[2])

lista_nome = ["Devison", "Dani", "Ricardo", "Ana"]
print(lista_nome[::-1])
del lista_nome[0]
lista_nome[::-1]
print(lista_nome)

nova_lista = [1, 2, "teste", [1, 2.3]]
print(nova_lista[3][1])
