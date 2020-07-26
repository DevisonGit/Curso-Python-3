#!/usr/bin/python3
permitidos_bloco = ("bloco_id", "bloco_accessKey")
permitidos_lista = ("ul_id")


def filtrar_conteudo(informados, permitido):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items()
                    if k in permitido)


def tag_bloco(texto, *args, classe='success', inline=False, **novos_atributos):
    tag = 'span' if inline else 'div'
    html = texto if not callable(texto) else texto(*args, **novos_atributos)
    conteudo = filtrar_conteudo(novos_atributos, permitidos_bloco)
    return f'<{tag} {conteudo} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atributos):
    lista = "".join(f'<li>{item}</li>' for item in itens)
    conteudo = filtrar_conteudo(novos_atributos, permitidos_lista)
    return f'<ul> {conteudo} {lista} </ul>'


if __name__ == "__main__":
    print(tag_bloco(tag_lista, "Naruto", "Sasuke", "Sakura",
                    classe="info",
                    inline=True,
                    bloco_id="conteudo",
                    bloco_accessKey="m",
                    ul_id="lista"))
