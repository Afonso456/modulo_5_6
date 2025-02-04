frutas={ }
for fruta in range(5):
    nome= input("Introduza a fruta:")
    quantidade= int(input("Introduza a quantidade:"))
    frutas[nome]= quantidade
#remover a fruta odiada
fruta_odiada= input("Qual a sua fruta odiada? :")
if fruta_odiada in frutas:
    del frutas[fruta_odiada]
    #listar frutas do dicionrario
    for chave,valor in frutas.items():
        print(f"{chave} -> {valor}")
else:
    print("A fruta não existe na lista")

#mostrar o nome da fruta com maior quantidade
maior_quantidade= 0
for chave,valor in frutas.items():
    if valor > maior_quantidade:
        maior_quantidade = valor
        fruta_maior = chave

print(f"A fruta com maior quantidade é {fruta_maior} com {maior_quantidade} unidades") 