"""
Listas por compreensão - criar uma lista com base num codigo
que gera a lista a partir de outra lista ou uma função geradora
"""
import random

carros = ["ford","bmw","ferrari","mercedes","renault"]

#criar uma lista dos carros cuja marca começa com f
carros_f= []

for marca in carros:
    if marca[0] == "f":
        carros_f.append(marca)

#lista aplicando um filtro á lista das marcas
carros_f = [marca for marca in carros if marca[0] == "f"]

print(carros_f)

#lista numeros sorteados
lista = [random.randint(1,100) for _ in range(10)]
print(lista)