"""
Programa para testar a função menu
1.Adicionar
2.Remover
3.Listar
4.Terminar
"""

import utils

while True:
    op = utils.menu(("Adicionar","Remover","Listar","Termnar"))
    if op == 1:
        print("Adicioanr")
    elif op ==2:
        print("Remover")
    elif op == 3:
        print("Listar")
    elif op == 4:
        break