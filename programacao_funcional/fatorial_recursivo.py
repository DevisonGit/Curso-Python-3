def fatorial(x):
    return x * (fatorial(x - 1) if (x - 1) > 1 else 1)


if __name__ == "__main__":
    print(f'O fatorial de 10 e {fatorial(10)}')
