PALAVRAS_PROIBIDAS = {"futebol", "politica", "religiao"}

textos = ["o Joao gosta de Futebol",
          "A praia esta bonita"]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Palavras proibidas", intersecao)
    else:
        print(texto)
