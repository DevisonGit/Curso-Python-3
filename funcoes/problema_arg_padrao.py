def fibonacci(sequencia=[0, 1]):
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    chamada = fibonacci()
    print(chamada, id(chamada))
    for i in range(10):
        fibonacci(chamada)
        print(chamada, id(chamada))

    # O problema ocorre quando tentamos zerar a sequencia
    restart = fibonacci()
    print(restart, id(restart))
