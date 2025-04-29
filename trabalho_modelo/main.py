"""
Trabalho Modelo - Modulo 6
--------------------------
Um programa para gerir livros e emprestimos de uma biblioteca.
    -Gestão de livros (CRUD)
    -Gestão de leitores (CRUD)
    -Emprestimos e devoluções 
    -Estatisticas (emprestimos em atraso, top livros, top mes, top leitores)
"""
import utils,livros,leitores,emprestimos,estatisticas,os

#Deve estar True quando em testes e False quando concluido
DEBUG = True

def menu_principal():
    if DEBUG:
        livros.configurar()
        leitores.configurar()
    op = 0
    while op != 5:
        os.system("cls")
        op = utils.menu(["Livros","Leitores","Emprestimos/Devoluções","Estatisticas","Sair"],"Menu principal")
        if op == 5:
            break
        if op == 1:
            livros.menu()  
        if op == 2:
            leitores.menu()
        if op == 3:
            emprestimos.menu()
        if op == 4:
            estatisticas.menu()
        

if __name__ == "__main__":
    menu_principal()