#!/usr/bin/python3
def gerador_de_html(texto, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = texto if not callable(texto) else texto(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = "".join(f'<li>{item}</li>' for item in itens)
    return f'<ul> {lista} </ul>'


if __name__ == "__main__":
    print(gerador_de_html(tag_lista, "Naruto", "Sasuke", "Sakura",
                          classe="info",
                          inline=True))
