cores = []
cores.append("vermelho")
print(cores)

#adicionar cor introduzida pelo utilizador
cor = input("indique uma cor:")
cores.append(cor) #adiciona a cor introduzida pelo utilizador no fim da lista
print(cores)

#inserir numa posição
cores.insert(1, "amarelo") #insere acor amarela na posição 1
print(cores)               #os restantes elementos da lista são reorganizados

#listar os elemetos da lista
for cor in cores:
    print(cor)

for pos in range(len(cores)):
    print(f"{pos} -> {cores[pos]}")

#remover um item da lista
cor_apagada = cores.remove("amarelo") #remove o primeiro e da erro se não encontrar
#remover por posições
cor_removida = cores.pop(0) #remove o elemento da posiçaoa indicada
             #da erro se a lista estiver vazia ou não existir a posição
print(f"Cor removida {cor_apagada}")
print(f"Cor removida {cor_removida}")
print(cores)

carros = ["ford","ferrari","bmw","vw"]
del carros[1:3] #remove os elementos nas posições 1 e 2 
print(carros)

#remover todos os eleemntos da lista
carros.clear()

#recriar a lista
carros = []

meus_carros = ["ford","bmw"]
teus_carros = ["mercedes","vw"]

meus_carros.extend(teus_carros)
print(meus_carros,teus_carros)

nossos_carros = meus_carros + teus_carros
print(nossos_carros)