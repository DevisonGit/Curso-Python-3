class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == "__main__":
    quadrado = Potencia(2)
    cubo = Potencia(3)
    print(f'Quadrado: {quadrado(3)}')
    print(f'Cubo: {cubo(5)}')
    print(f'4 {Potencia(4)(5)}')
