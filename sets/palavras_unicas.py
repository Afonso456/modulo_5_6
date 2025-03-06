texto= input("Introduza uma frase:\n")
#lista das palavras
palavras= (texto.strip().split(" "))
#converter a lista em um set
palavra_unica= set(palavras)
#len para contar
print(len(palavra_unica))