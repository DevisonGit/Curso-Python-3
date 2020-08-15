#!/usr/local/bin/python3
def sequencia():
    num = 0
    while True:
        num += 1
        yield num


if __name__ == "__main__":
    generator = sequencia()
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
