#!/usr/bin/python3
def gerador_de_html(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    print(gerador_de_html("texto de teste"))
    print(gerador_de_html("texto de erro", "error"))
