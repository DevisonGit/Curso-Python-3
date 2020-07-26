# print(dir(str))
nome = "Devison Santos"
print(nome[0])

texto = "texto com ' aspas simples escapando"
print(texto)

texto = 'texto com " aspas dupla escapando'
print(texto)

texto = "texto com \" escape de barra"
print(texto)

texto_longo = """texto realmente longooooooooooooo
\tcom quebras de linha e tabulacao
\tlinha 1
\tlinha 2"""
print(texto_longo)

texto_longo = '''texto realmente longooooooooooooo
\tcom quebras de linha e tabulacao
\tlinha 1
\tlinha 2'''
print(texto_longo)

print(nome[7:])
print(nome[::-1])
print("tudo invertido"[::-1])

numeros = '1234567890'
print(numeros[::])
print(numeros[::-1])
print(numeros[::2])
print(numeros[1::2])
