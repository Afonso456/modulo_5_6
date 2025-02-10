"""
Programa para criar um dicionario com as defenições de palavras inseridas pelo utilizador
Adicionar defenição
Listar defenição
Pesquisar palavra
Apagar defenição
Terminar
No futuro guardar os dados num ficheiro (M07)
"""
from dicionario import configurar,adicionar,listar,pesquisar,apagar,em_teste

def menu():
    """
    Função que faz o menu do dicionario e chama as outras funções
    """
    dicionario={ }
    op= 0
    if em_teste:
        configurar(dicionario)
    while op != 5:
        print("1.Adicionar palavra e defenição\n2.Listar defenições\n3.Pesquisar palavra\n4.Apagar palavra\n5.Terminar")
        op= input("") 
        if op == "1":
            adicionar(dicionario)
        elif op == "2":
            listar(dicionario)
        elif op == "3":
            palavra = input("Insira a palavra a pesquisar:")
            pesquisar(palavra,dicionario)
        elif op == "4":
            palavra = input("Insira a palavra a apagar:")
            apagar(palavra,dicionario)
        elif op == "5":
            break

if __name__ == "__main__":
    menu()