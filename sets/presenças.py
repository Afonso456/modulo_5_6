"""
Um programa que calcula:
- os alunos que estiveram presentes todos os dias
- os alunos que faltaram pelo menos um dia
- os alunos que estiveram presentes apenas na segunda e na sexta
"""

segunda= {"Ana","Carlos","Pedro","Maria"}
terca=   {"Ana","João","Pedro","Clara"}
quarta=  {"Maria","Pedro","Ana","Paulo"}
quinta=  {"João","Clara","Paulo","Ana"}
sexta=   {"Ana","Maria","Carlos","Paulo"}

#presentes todos os dias
presentes= segunda & terca & quarta & quinta & sexta
print(presentes)

#faltaram pelo menos 1 dia
uniao = segunda | terca | quarta | quinta | sexta
faltaram = uniao.difference(presentes)
print(faltaram)

#presentes apenas na segunda e sexta
s_s= segunda & sexta
t_q_q= terca | quarta | quinta
presentes_s_s= s_s - t_q_q
print(presentes_s_s)