d = {123:{"nome":"Carlos","cidade":"Viseu","visitas":22},
     124:{"nome":"Paula","cidade":"Viseu","visitas":44},
     125:{"nome":"Filipa","cidade":"Porto","visitas":67},
     126:{"nome":"Rui","cidade":"Lisboa","visitas":35},
     127:{"nome":"Fernando","cidade":"Porto","visitas":165}}


for cliente in d:
    print(cliente)
    for visitas in d[cliente]:
        print(f"Visitas {visitas} - {d[cliente][visitas]}")


cidade_maior= ""
maior = 0
for chave in d:
    t_cidade = d[chave]["cidade"]
    nr_visitas = d[chave]["visitas"]
    for codigo in d[chave]:
        if t_cidade == d[codigo]["cidade"]:
            nr_visitas += d[codigo]["visitas"]
    if nr_visitas > maior:
        cidade_maior = t_cidade
        maior = nr_visitas
print(cidade_maior)