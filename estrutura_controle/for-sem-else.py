PALAVRAS_PROIBIDAS = ["futebol", "politica", "religiao"]

textos = ["o Joao gosta de Futebol",
          "A praia esta bonita"]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Tem uma palavra proibida:", palavra)
            found = True
            break
    if not found:
        print(texto)
