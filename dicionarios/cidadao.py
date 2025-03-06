"""
Programa que 
nome morada codigo postal pai mãe e casado
"""
dados= { }
dados["nome"] = input("Nome:")
dados["morada"] = input("Morada:")
dados["codigo postal"] =input("Codigo postal:")
dados["pai"] = input("Nome do pai:")
dados["mae"] = input("Nome da mãe:")
op = input("Casado s/n:")
if op == "s":
    dados["casado"] = True
else:
    dados["casado"] = False

dados["nr_filhos"] = int(input("Nr de fillhos:"))
filhos={}
for filho in range(dados["nr_filhos"]):
    chave= f"nome_{filho+1}"
    filhos[chave]= input(f"Intoduza o nome do filho nº {filho +1}:")

print(filhos)
dados["filhos"]= filhos 
print(dados)
