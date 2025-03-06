"""
Programa para gerir os livros de uma biblioteca e os imprestimos
Menu: 1.Adicionar livro 2.Listar todos 3.Emprestimo 4.Devolução 5.Terminar
"""

import numpy as np
from datetime import datetime 

MAX_LIVROS= 100


def contagem_livros(livros):
    """
    Devolver o numero de posições preenchidas no array"""
    for p in range(MAX_LIVROS):
        if livros[p] == None:
            return p
    return MAX_LIVROS #array esta cheios

def livro():
    """Lê do utilizadro os dados do livro novo e devolve um dicionario com esses dados"""
    nome= input("Insira o nome do livro:")
    tema= input("Insira o tema do livro:")
    leitor= None
    data_emp= None
    return {"nome":nome,"tema":tema,"leitor":leitor,"data_emp":data_emp}

def adicionar(livros):
    """Função responsavel por adicionar um livro novo ao array"""
    posicao= contagem_livros(livros)
    #verificar se o array esta cheio
    if posicao == MAX_LIVROS:
        print("Não pode adicionar mais dados")
        return
    novo_livro= livro()
    #adicionar o campo id
    novo_livro["id"]= posicao + 1
    #adicionar o novo livro a primeira posicao livre do array
    livros[posicao]= novo_livro
    print("Livro adicionado com sucesso\n")
    

def listar(livros):
    """Função responsavel por listar os livros disponiveis"""
    print(livros)


def emprestimo(livros):
    """Função responsavel por fazer o emprestimo dos livros"""
    id = int(input("Qual o id do livro a emprestar:"))
    #validaro id
    if id < 1 or id > contagem_livros(livros): 
        print("O id introduzido não é valido")
        return
    #verificar se o livro ja esta emrestado
    posicao = id - 1
    if livros[posicao]["leitor"] != None:
        print(f"Este livro esta emprestado ao leitor {livros[posicao]["leitor"]}")
    #ler o nome do leitor
    leitor= input("Nome do leitor:")
    data= datetime.now().strftime("%d-%m-%Y") #data como string
    #registar o emprestimo
    livros[posicao]["leitor"] = leitor
    livros[posicao]["data_emp"] = data
    print("Emprestimo registado com sucesso")


def devolucao(livros):
    """"""
    id = int(input("Qual o id do livroa emprestar:"))
    #validaro id
    if id < 1 or id > contagem_livros(livros): 
        print("O id introduzido não é valido")
        return
    #verificar se o livro ja esta emrestado
    posicao = id - 1
    if livros[posicao]["leitor"] == None:
        print(f"Este livro não esta emprestado")
    #registar o emprestimo
    livros[posicao]["leitor"] = None
    livros[posicao]["data_emp"] = None
    print("Emprestimo registado com sucesso")
    

def menu():
    livros = np.empty(MAX_LIVROS, dtype= object)
    op= 0
    while op != 5:
        print("1.Adicionar livro\n2.Listar todos\n3.Emprestimo\n4.Devolução\n5.Terminar")
        op= input("")
        if op == "1":
            adicionar(livros)
        elif op == "2":
            listar(livros)
        elif op == "3":
            emprestimo(livros)
        elif op == "4":
            devolucao()
        elif op == "5":
            break
        else:
            print("Opção invalida")


if __name__ == "__main__":
    menu()