"""
Programa para fazer um bilhete da lotaria do euromilhões
"""
import random
numeros  = set()
estrelas = set()

def sortear(numeros,quantos,maximo):
    while len(numeros) != quantos:
        sorteado = random.randint(1,maximo)
        numeros.add(sorteado)

sortear(numeros,5,50)
sortear(estrelas,2,12)

print(f"Numeros -> {numeros}")
print(f"Estrelas -> {estrelas}")