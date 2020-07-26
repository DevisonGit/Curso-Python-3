# Desafio operadores logicos

# Os trabalhos
trabalho_terca = True
trabalho_quinta = False

"""
- Confirmando os 2 trabalhos = TV 50 + sorvete
- Confirmando um trabalho = TV 32 + sorvete
- Nenhum trabalho fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = tv_32 or tv_50
fica_em_casa = not sorvete

print("TV 32 {} TV 50 {} Sorvete {} Fica em casa {}" .format(
    tv_32, tv_50, sorvete, fica_em_casa))
