dicionario1={"a":1, "b":2, "c":3}
dicionario2={"c":2, "d":3}
#Esta linha não faz uma copia do dicionario
# as duas variaveis dicionario2 d icionario3 apontam para a mesma memoria (partilham os mesmos dados)
dicionario3= dicionario2
dicionario3["e"] = 4
print(dicionario2)

#criar uma copia de um dicionario
dicionario4= dicionario1.copy()
dicionario4["z"]= 10 
print(dicionario1)

#OU
dicionario4= {}
for chave,valor in dicionario1.items():
    dicionario4[chave] = valor
