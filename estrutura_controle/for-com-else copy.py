PALAVRAS_PROIBIDAS = ("futebol", "politica", "religiao")

textos = ["o Joao gosta de Futebol",
          "A praia esta bonita"]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Tem uma palavra proibida:", palavra)
            break
    else:
        print(texto)
