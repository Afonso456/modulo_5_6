#definir um dicionario {chave: valor} (valor é o que chave recebe)
dicionario= {"nome":"joaquim"}
print(dicionario["nome"])
#alterar i valor de uma chave
dicionario["nome"]= input("Introduza um nome:")
print(dicionario["nome"])

#adicionar novas chaves:valores
dicionario["idade"] = input("Introduza a idade:")
print(dicionario["idade"])
print(dicionario)

#fazer um ciclo paara percorrer os pares chave:valor
chaves= dicionario.keys()       #devolve uma lista com as chaves
valores= dicionario.values()    #devolve um lista com os valores
elementos= dicionario.items()   #devolve uma lista com os pares chave:valor
for chave in dicionario.keys():
    print(dicionario[chave])

#ciclo que percorre os items do dicionario(chave:valor)
for pares in dicionario.items():
    print(f"{pares[0]} : {pares[1]}")

#remover chaves:valores
valor= dicionario.pop("idade",None)
print(f"Idade(removida):{valor}")  #primeira vez deve devolver 10
valor= dicionario.pop("idade", None)
print(f"Idade(removida {valor})")  #segunda vez devolve None porque a chave já não existe

#remover a chave indicada entre []
del dicionario["nome"]
print(dicionario)