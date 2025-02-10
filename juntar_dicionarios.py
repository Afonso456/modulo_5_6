d1= {"a": 1, "b": 2, "c": 3}
d2= {"c": 4, "d": 5}

#juntar dois dicionarios
d1.update(d2) # adicioar as chaves novas e atualizar os valores de chaves existentes
print(d1)
print(d2)

dicionarioA={"a":1, "b":2, "c": 3}
dicionarioB={"c":4, "d":5}
#o operador | so existe a partir da versão 3.9 do python
juntar= dicionarioA|dicionarioB #operador para juntar os dois dicionarios
print(juntar)
print(dicionarioA)
print(dicionarioB)