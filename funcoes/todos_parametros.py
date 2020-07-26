def todos_parametros(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == "__main__":
    todos_parametros("teste", " som", valido=True, Nome="Serafina")
    todos_parametros(valido=True, Nome="Serafina")
    todos_parametros([1, 2, 3], True)
