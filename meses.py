"""
Crie um tuple com os meses do ano 
Mostrar o terceiro mes do ano
Obter os meses de verao(junho,julho,agosto,setembro)
Verificar se "Junho esta presente nos meses de verão
Extra:
listar os meses por ordem alfabetica
mostrar os meses cujo nome começa com j
mostrar o mes(es) com o maior nome
"""
meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
print(meses[2])

meses_verao = meses[5:9]
print(meses_verao)

if "junho" in meses_verao:
    print("Junho faz parte do verão")
else:
    print("Junho não faz parte do verão")

meses_ordenados = sorted(meses)
print(meses_ordenados)

for mes in meses:
    if mes[0] == "j":
        print(mes)

