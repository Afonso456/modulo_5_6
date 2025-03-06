"""
Listas Estruturas de dados dinamicos(nº de elementospode aumentar ou diminuir), não homegenea(pode ter elementos de diferentes tipos de dados,
incluindo, mutaveis - listas, dicionarios, arrays, etc...)
"""

#definir uma lista
minha_lista = [] #lista vazia
minha_lista2 = [1,2,3,"quatro"]
minha_lista3 = list({1,2,3,4})
lista_de_cinco = list(range(5))

print(minha_lista,minha_lista2,minha_lista3,lista_de_cinco)

#listas são referencias 
x = 10
y = x
y= 11
print(x,y)
lista_x = [1,2,3]
lista_y = lista_x # as duas variaveis "apontam" para o mesmo conjunto de dados
lista_x[1] = 10
print(lista_x,lista_y)
#criar uma copia da lista
lista_z = lista_x[:] #cria uma lista nova e copia todos os valores
lista_x[1] = 5
print(lista_x,lista_z)

#listar valores da lista
print(lista_x[0],lista_y[0],lista_z[0]) #mostrar o 1º elemento da lista
lista_k = [1,2,[10,20]] #lista com uma lista incorporada
print(lista_k[2][0]) #mostra o 1º valor da lista incorporada

#dicionario incorporado
notas = [{"joaquim":10},{"maria":15},{"antonio":12}]
#mostrar a noto do antonio
print(notas[2]["antonio"])
notas[0]["faltas"] = 10
print(notas[0])