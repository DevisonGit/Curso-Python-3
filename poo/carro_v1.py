class Carro():
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        if self.velocidade_atual + delta < self.velocidade_maxima:
            self.velocidade_atual += delta
            return self.velocidade_atual
        else:
            return f"O carro chegou na velocidade maxima \
{self.velocidade_maxima}"

    def freiar(self, delta=5):
        if self.velocidade_atual - delta > 0:
            self.velocidade_atual -= delta
            return self.velocidade_atual
        else:
            self.velocidade_atual = 0
            return f"O carro chegou na velocidade minima \
{self.velocidade_atual}"


if __name__ == "__main__":
    carro = Carro(180)

    for _ in range(25):
        print(carro.acelerar(8))

    for _ in range(10):
        print(carro.freiar(20))
