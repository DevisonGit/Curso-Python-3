from random import randint


def sortear_dados():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    elif i == sortear_dados():
        print("ACERTOU", i)
        break
else:
    print("Nao acertou")
