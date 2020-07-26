#!/usr/bin/python3
def gerador_de_html(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


def tag_lista(*itens):
    lista = "".join(f'<li>{item}</li>' for item in itens)
    return f'<ul> {lista} </ul>'


if __name__ == "__main__":
    print(gerador_de_html(tag_lista("item 1", "item 2", "item 3"),
                          classe="info",
                          inline=True))
