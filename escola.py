"""
Programa que cria um dicionario com os professores responsaveis pelas salas do torneio TECLA e o nº 
d alunos que cada sala vai ter. As salas são a C5,C6,C7,C8 e o dicionario deve guardar o nome do professor
e o nº de alunos de cada uma
"""

dados = {"c5":{"professor":"p1","n_alunos":10},
         "c6":{"professor":"p2","n_alunos":14},
         "c7":{"professor":"p3","n_alunos":12},
         "c8":{"professor":"p4","n_alunos":8}
}

for sala in dados:
    professor= input(f"Nome do professor responsavel pela sala {sala}:")
    nr_alunos= int(input(f"Nº de alunos para a sala {sala}:"))
    #atualizar o nome do professor
    dados[sala]["professor"] = professor
    #atualizar o nº de alunos
    dados[sala]["nr_alunos"] = nr_alunos

#listar dados
for sala in dados:
    print(f"Sala:{sala} -> Professor responsavel:{dados[sala]["professor"]} -> Nº de alunos:{dados[sala]["nr_alunos"]}")


op= input("Dsseja adicionar uma sala(s/n):")
if op == "s":
#adicionar uma sala, um professor e o nº de alunos introduzidos pelo utilizador
    sala= input("Insira o nº da sala:")
    responsavel= input("Nome do professor responsavel:")
    alunos= input("Nº da alunos:")
    dados[sala]= {"professor":responsavel,"n_alunos":alunos}
    print(f"Sala:{sala} -> Professor responsavel:{dados[sala]["professor"]} -> Nº de alunos:{dados[sala]["n _alunos"]}")

#remover a sala c5
del dados["c5"]
print(dados)
