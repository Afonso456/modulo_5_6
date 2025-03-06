"""
Sets(conjuntos)
Unicos(os elementos repetidos são descartados), não ordenados(não tem ordem fixa),
mutaveis(adicionar,remover), elementos imutaveis(bool, int, float, str)
"""

#definir o set
nomes1= {"joão","maria"}
nomes2= {"joão","joaquim","carlos"}
nomes3= {"maria","joão"}

#Igualdade
if nomes1 == nomes3: #iguais porque a ordem dos elementos não conta
    print("São iguais")
else:
    print("São diferentes")

#União
nomes= nomes1.union(nomes2) #faz a união e devolve sem alterar
print(f"União {nomes}") 

nomes_v2= nomes1 | nomes2 #faz a união e devolve sem alterar
print(f"União{nomes_v2}")

nomes1.update(nomes2) #faz a união e altera
print(f"União {nomes1}")


#Interseção
nomes_iguais = nomes3.intersection(nomes2) #devolve a interseção sem alterar
print(f"Interseção {nomes_iguais}")
nomes_iguais_v2= nomes2 & nomes3 #devolve a interseção sem alterar
print(nomes_iguais_v2)
nomes1.intersection_update(nomes3) #faz a interseção alterando
print(f"Interseção {nomes1}")

#Diferença
diferenca = nomes3.difference(nomes2)
print(f"{nomes3} - {nomes2}: Diferença {diferenca}")
diferenca = nomes2.difference(nomes3)
print(f"{nomes2} - {nomes3}: Diferença {diferenca}")
diferenca = nomes2 - nomes3 
print(f"{nomes2} - {nomes3}: Diferença {diferenca}")

#Diferença simetrica
diferenca_simetrica= nomes3.symmetric_difference(nomes2) #retira os repetidos nos dois conjuntos
print(f"{nomes3} - {nomes2}: Diferença simetrica {diferenca_simetrica}")

diferenca_simetrica = nomes2 ^ nomes3 
print(f"{nomes3} - {nomes2}: Diferença simetrica {diferenca_simetrica}")

#converter
valores = set([1,2,3,4,5,6,7,7,1,2,3,4,5,8,4,4,5,0,0])
print(valores) #adicionar elementos ao set


for pos, valor in enumerate(valores,start=1): #cria uma sequencia com os valores do set e atribui-lhes uma posição
    print(f"Elementos da posicao {pos}: {valor}")
"""
este codigo não funciona
for i in range(len(lista)):
    print(lista[i]) #não podemos fazer isto com sets
"""

#testar se existe
if 2 in valores:
    print("O valor existe")
else:
    print("O valor não existe")
valores.add(6)
print(valores)

valores.add("maria")
print(valores)

#elemento duplicado
valores.add(1)
print(valores)

#remover elementos do set
valores.remove(1)
print(valores)

#listar os elementos do set
for elemento in valores:
    print(elemento)

print(len(valores))