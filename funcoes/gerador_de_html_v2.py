#!/usr/bin/python3
def gerador_de_html(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(gerador_de_html(texto="texto de erro", classe="error", inline=True))
    print(gerador_de_html(texto="texto de sucesso", inline=False))
    print(gerador_de_html(classe="error", inline=False,
                          texto="texto por ultimo"))
