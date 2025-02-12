
numeros= input("Introduza um numero:")
nr_invertido= ""
for posicao in range(len(numeros) -1,-1,-1):
    nr_invertido = nr_invertido + numeros[posicao]
if nr_invertido == numeros:
    print("Capicua")
else:
    print("O nr não é capicua")