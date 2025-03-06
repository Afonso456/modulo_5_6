"""
Program,a para ler do utilizador as marcas de carros de um stand.
O programa deve mostrar qual a marca com mais veiculos
- Ler do utilizador as marcas e guardar em uma lista 
- Parar de ler quandddo o utilizador inserir uma marca vazia 
- Calcular para cada marca quantos carros existem
- Mostrar a marca com mais carros
(utilizar listas para guardar as marcas)
"""

carros = []
marca = " "
while marca != "":
    marca = input("Introduza uma marca de carro:")
    if marca == "":
        break
    carros.append(marca)
print(carros)

#quantidade de marcas
marcas = set (carros)
mmaior = ""
maior = 0
for marca in marcas:
    contar = carros.count(marca)
    print(f"Da marca {marca} existem {contar} marcas de carro")
    #quantidade de carro por marca
    if contar > maior:
        mmaior = marca
        maior = contar
print(f"A marca {mmaior} é a que tem mais veiculos com {maior} carros")

op = ""
while op != "s" and op != "n":
    op = input("Deseja reover uma marca (s/n):")
    if op == "s":
        marca = input("Marca a remover:")
        while marca in carros:
            carros.remove(marca)
    elif op == "n":
        print(carros)