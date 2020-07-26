# Comprehension e uma forma de fazer uma lista de forma rapida e concisa
# [ expressao for item in list if condicional]
dobros = [i * 2 for i in range(10)]
print("com Comprehension: ", dobros)

# versao "normal"
dobros = []
for i in range(10):
    dobros.append(i * 2)
print("sem Comprehension: ", dobros)
