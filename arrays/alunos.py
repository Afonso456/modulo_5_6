import numpy as np

notas=np.array([12,10,11,14])

aluno1={"nome":"joaquim","turma":"10ºT","email":"joaquim@gmail.com","notas":100, "nota":"notas"}

#listar as notas do aluno1
for nota in aluno1["notas"]:
    print(nota)

for posicao in range(len(aluno1["nota"])):
    print(aluno1["notas"][posicao])