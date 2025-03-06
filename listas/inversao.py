alunos = ["joaquim","antonio","maria","carlos","joaquim"]

#inverter a ordem dos nomes
converter_alunos= alunos[::-1]
print(converter_alunos)

#existem nome repetidos
if len(alunos) != len(set(alunos)):
    print("Existem nomes repetidos")
else:
    print("Não existem nomes repetidos")
