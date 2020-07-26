# Continue passa pra o proximo ponto do laco
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# Break interrompe o laco
for i in range(1, 10):
    if i == 5:
        break
    print(i)
else:
    print("teste")
