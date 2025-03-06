notas = {
    "joaquim" : [10, 12, 14, 8],
    "maria"   : [14, 10, 13, 8],
    "carlos"  : [10, 10, 10, 10]
}

disciplinas = ("pt","ing","mat","psi")

#mostrar a media de notas de cada aluno
mmedia = -1 
nomemm =  ""
for aluno in notas:
    media = sum(notas[aluno]) / len(notas[aluno])
    print(f"A media das notas do(a) {aluno} é de {media} ")
    if mmedia < media:
        mmedia = media
        nomemm = aluno
#mostrar o nome do aluno com a melhor media
print(f"O aluno com a melhor media foi o/a {nomemm} e teve {mmedia}")

#motrar o nº de negativas de cada aluno
for aluno in notas:
    negativas = 0
    for nota in notas[aluno]:
        if nota < 10:
            negativas += 1
    #mostrar o nome dos alunos sem negativas
    if negativas == 0:
        print(f"O aluno {aluno} não tem negativas")
    else:
        print(f"O aluno {aluno} tem {negativas} negativas")


#calcular e mostrar a media das notas de cada disciplina
for i in range(len(disciplinas)):
    soma = 0
    for aluno in notas:
        soma += notas[aluno][i]
    media = soma / len(notas.keys())
    print(f"A disciplina {disciplinas[i]} tem a media de {media}")

#criar um dicionario com o nome do aluno, o nome das disciplinas as respetivas notas de cada aluo
notas_v2 = {}
for aluno in notas:
    notas_v2[aluno]={}
    for i in range(len(disciplinas)):
        pass