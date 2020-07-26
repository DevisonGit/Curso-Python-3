def log(function):
    def decorator(*args, **kwargs):
        print(f'inicio da funcao:{function.__name__}')
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def subtracao(x, y):
    return x - y


if __name__ == "__main__":
    soma(10, 10)
    subtracao(10, y=5)
