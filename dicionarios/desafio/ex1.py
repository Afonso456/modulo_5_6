notas = {"aluno1":{"pt":0,"ing":0,"ai":0,"tic":0},
          "aluno2":{"pt":0,"ing":0,"ai":0,"tic":0}}

for chave in notas:
    soma = 0
    for d in notas[chave]:
        nota = int(input(f"Nota de {d} do {chave}:"))
        notas[chave][d] = nota
        #meida de cada aluno
        soma += nota
    media= soma / 4
    notas[chave]["media"] = media
    print(f"A media do aluno {chave} é {media}")
    #media das medias dos dois alunos
    media_alunos = (notas["aluno1"]["media"] + notas["aluno2"]["media"]) / 2
    print(f"A media dos alunos é de {media_alunos}")

    for aluno in notas:
        print(aluno)
        for disciplina in notas[aluno]:
            print(f"O aluno {aluno} tem nota {notas[aluno][disciplina]}")