nomes=["joaquim","maria","carlos"]
idades=[   30,     25,      33]

#fazer um dicionario com os nomes como chaves e as idades como valores
dicionario= dict(zip(nomes,idades))
print(dicionario)

for chave,valor in zip(nomes,idades):
    print(f"{chave} -> {valor}")