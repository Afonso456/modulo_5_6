alunos = [
    {"nprocesso":123,"nome":"maria","email":"maria@gamil.com"},
    {"nprocesso":124,"nome":"joaquim","email":"joaquim@gamil.com"},
    {"nprocesso":125,"nome":"antonio","email":"antonio@gamil.com"}
]

notas = [
    {"nprocesso":123,"notas":[10,11,12,13]},
    {"nprocesso":124,"notas":[10,15,8,14]}
]

#mostrar o nome e a nota dos alunos
#os alunos sem notas não devem aparecer
for aluno in alunos:
    for nota in notas:
        if nota["nprocesso"] == aluno["nprocesso"]:
            print(f"{aluno["nome"]} -> {nota["notas"]}")


"""
Considerações:
    - o que deve acontecer quando tentar apagar o aluno 124? Apagar tambem as notas
    ou não deixar apagar o aluno
    - podemos adicionar as notas do aluno 129? Sim, mas como ele não existe não seria possivel
    - não podemos alterar o nº processo
"""