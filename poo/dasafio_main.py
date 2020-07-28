from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    cliente = Cliente('Devison', 32)
    vendedor = Vendedor('Pedro', 28, 5600)
    compra1 = Compra(cliente, datetime.now(), 600)
    compra2 = Compra(cliente, datetime(2020, 6, 4), 1500)
    cliente.registrar_compras(compra1)
    cliente.registrar_compras(compra2)
    print(f'Total: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')
    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f'Total: {valor_total} em {qtde_compras} compras')
    print(f'Última compra: {cliente.ultima_compra()}')


if __name__ == "__main__":
    main()
