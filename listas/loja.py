"""
Programa para gerir um stock.
Cada vez que um produto é vendido o stock deve baixar e de cada vez que o produto é comprado o stock aumenta
"""

produtos = ["batatas","bananas","arroz",     "bacalhau",  "maçãs"]
stock    = [10,        50,       10,          5,           5     ]
unidades = ["kg",     "kg",    "embalagem",  "unidade",   "kg"   ]


def compra():
    produto_comprar = input("Produto a comprar:")
    quantidade_comprar = input("Quantidade:")
    if produto_comprar in produtos:
        index = produtos.index(produto_comprar)
        stock[index] += int(quantidade_comprar)
        print(f"O stock de {produto_comprar} aumentou para {stock[index]}")
    if produto_comprar not in produtos:
        produtos.append(produto_comprar)
        stock.append(int(quantidade_comprar))
        print(f"O produto {produto_comprar} foi adicionado ao seu stock")

def venda():
    produto_vender  = input("Produto a vender:")
    quantidade_vender = int(input("Quanridade:"))
    if produto_vender in produtos:
        if quantidade_vender > stock[produtos.index(produto_vender)]:
            print("Stock indisponivel")
        else:
            index = produtos.index(produto_vender)
            stock[index] -= int(quantidade_vender)
            print(f"O stock de {produto_vender} baixou para {stock[index]}")
        print("Produto inexistente")

def consulta():
    produto_consultar =input("Produto que deseja consultar:")
    if produto_consultar in produtos:
        index = produtos.index(produto_consultar)
        print(f"O stock de {produto_consultar} é {stock[index]}")
    else:
        print("Produto inexistente")

def main():
    while True:
        op = input("Comprar\nVender\nListar produto\nTerminar\n")
        if op == "comprar":
            compra()
        elif op == "vender":
            venda()
        elif op == "listar":
            consulta()
        elif op == "terminar":
            break
        else:
            print("Comando invalido\n")

if __name__ == "__main__":
    main()