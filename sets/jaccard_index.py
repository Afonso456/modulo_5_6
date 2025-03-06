frase1= input("Introduza uma frase:")
frase2= input("Introuza outra frase:")

palavras= (frase1.strip().lower().split(" "))
palavras_2= (frase2.strip().lower().split(" "))

frase_separada_1= set(palavras)
frase_separada_2= set(palavras_2)

jaccard= (frase_separada_1 & frase_separada_2) / (frase_separada_1 | frase_separada_2)
print(jaccard)