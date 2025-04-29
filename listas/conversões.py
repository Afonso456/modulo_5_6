d1 = {"nome":"joaquim","idade":"15","morada":"Viseu"}

#converter dicionario para lista
lista = list(d1.items())
print(f"Lista {lista}")

#converter duas listas em um dicionario
chaves = ["nomes","idade","morada"]
valores = ["joaquim","16","viseu"]

dicionario = dict(zip(chaves,valores))
print(f"Dicionario {dicionario}")