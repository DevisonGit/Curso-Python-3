def tag(tag, *args, **kwargs):
    if 'css' in kwargs:
        kwargs['class'] = kwargs.pop('css')
    atributos = ''.join(f'{k} = "{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag}> {atributos} {inner} </{tag}>'


if __name__ == "__main__":
    resultado = tag('p',
                    tag('span', 'Curso de Python 3, por '),
                    tag('strong', 'Juracy Filho', id='jf'),
                    tag('span', ' e '),
                    tag('strong', 'Leonardo Leitão', id='ll'),
                    tag('span', '.'),
                    css='alert')
    print(resultado)
