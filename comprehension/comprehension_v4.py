# Comprehension e uma forma de fazer uma lista de forma rapida e concisa
# [ expressao for item in list if condicional]
# usando o generator o consumo de memoria e menor pois ele gera sobre demanda
# ao contrario do comprehension que gera de uma vez
generator = (i * 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
