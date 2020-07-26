#!/usr/bin/python3
# Gerar sequencia de Fibonacci 0,1,1,2,3,5,8,13,21...


def fibonacci(quantidade):
    lista = [0, 1]
    for i in range(2, quantidade):
        lista.append(sum(lista[-2:]))
    return lista


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=', ')
