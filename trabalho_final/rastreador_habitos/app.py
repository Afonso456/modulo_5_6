from main import adicionar_utilizador,remover_utilizador,adicionar_habitos,remover_habitos,registar_progresso,listar_habitos,listar_utilizadores
import utils

def main():
    """Função principal do programa"""
    op = 0
    while op != 8:
        op = utils.menu(['Adicionar utilizador','Remover utilizador','Adicionar habitos','Remover habitos',
                         'Listar habitos','Listar utilizadores','Registar progresso','Sair'],'Menu principal')
        if op == 8:
            break
        elif op == 1:
            adicionar_utilizador()
        elif op == 2:
            remover_utilizador()
        elif op == 3:
            adicionar_habitos()
        elif op == 4:
            remover_habitos()
        elif op == 5:
            listar_habitos()
        elif op == 6:
            listar_utilizadores()
        elif op == 7:
            registar_progresso()
        else:
            print('Opção invalida. Tente novamente')
        
if __name__ == '__main__':
    main()