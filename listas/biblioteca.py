"""
Programa para gerir os livro de uma biblioteca e os seus emprestimos
"""

livros = ["livro1","livro2","livro3","livro4"]

emprestimos = []
titulo = " "

#o porgrama deve terminar quando é inserido um titulo em branco ou quando não ha mais livros para emprestar
while titulo != "" and len(livros) > 0:
#ler o titulo do livro a emprestar
    titulo = input("Titulo do livro:")
    if titulo in livros:
#remover da lista do livrose adicionar a lista dos emprestimos
        livros.remove(titulo)
        emprestimos.append(titulo)
#mostrar os livors e os emprestimos
        print(f"Livros -> {livros} \nEmprestimos -> {emprestimos}")
    else:
#avisar o utilizador quando o livro esta emprestado ou não existe
        print("Livro não encontrado ou emprestados")
