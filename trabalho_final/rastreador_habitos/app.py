from main import adicionar_utilizador,remover_utilizador,adicionar_habitos,remover_habitos,registar_progresso,listar_habitos,listar_utilizadores
import utils


def main():
    op = 0
    while op != 8:
        print("---Rastreador de Habitos---")
        op = utils.menu(['Adicionar utilizadores','Remover utilizador','Adicionar habito','Remover habito','Listar habitos','Listar Utilizadores','Registar progresso','Sair'])
        if op == 8:
            break
        if op == 1:
            adicionar_utilizador()
        if op == 2:
            remover_utilizador()
        if op == 3:
            adicionar_habitos()
        if op == 4:
            remover_habitos()
        if op == 5:
            listar_habitos()
        if op == 6:
            listar_utilizadores()
        if op == 7:
            registar_progresso()

if __name__ == "__main__":
    main()