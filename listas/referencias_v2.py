alunos = [
    {"nprocesso":123,"nome":"maria","email":"maria@gamil.com"},
    {"nprocesso":124,"nome":"joaquim","email":"joaquim@gamil.com"},
    {"nprocesso":125,"nome":"antonio","email":"antonio@gamil.com"}
]

notas = [
    {"nprocesso":alunos[0],"notas":[10,11,12,13]},
    {"nprocesso":alunos[1],"notas":[10,15,8,14]}
]

#mostrar o nome e as notas do alunos
#os alunos sem notas n devem aparecer
for nota in notas:
    print(f"{nota["nprocesso"]["nome"]} -> {nota["notas"]}")

#apagar o primeiro aluno
del alunos[0]

for nota in notas:
    print(f"{nota["nprocesso"]["nome"]} -> {nota["notas"]}")

print(alunos)