import utils
from datetime import datetime,timedelta

utilizadores = {}  #Criar um dicionario vazio


def adicionar_utilizador():
    """Função para adicionar utilizadores"""
    nome = utils.ler_string(3,'Nome do utilizador a adicionar:')
    if nome not in utilizadores:
        # Adicionar o utilizador ao dicionario
        utilizadores[nome] = {
            'habitos': [],
            'dias totais': 0,
            'dias consecutivos': 0
        }
        print(f'Utilizador "{nome}" adicionado com sucesso')
    else:
        print(f'Utilizador "{nome}" já existe.')

def remover_utilizador():
    """Função para remover utilizadores"""
    nome = utils.ler_string(3,'Nome do utilizador a remover:')
    if nome in utilizadores:
        # Remover o utilizador do dicionario
        del utilizadores[nome]
        print(f'Utilizador "{nome}" removido com sucesso')
    else:
        print(f'Utilizador "{nome}" não encontrado.')

def adicionar_habitos():
    """Função para adicionar habitos a um utilizador"""
    nome = utils.ler_string(3,'Insira o nome do utilizador a pesquisar:')
    # verificar se o utilizador existe
    if nome in utilizadores:
        # perguntar o habito a adicionar
        habito = utils.ler_string(3,'Habito a adicionar:')
        # se o habito não existir adiciona-lo
        if habito not in utilizadores[nome]['habitos']:
            utilizadores[nome]['habitos'].append(habito)
            print(f'Habito {habito} adicionado com sucesso')
        else:
            print(f'Habito {habito} já existe')
    else:
        print(f'Utilizador {nome} não encontrado')

def remover_habitos():
    """Função para remover habitos de um utilizador"""
    nome = utils.ler_string(3,'Insira o nome do utilizador a pesquisar:')
    # verificar se o utilizador existe
    if nome in utilizadores:
        # perguntar o habito a remover
        habito = utils.ler_string(3,'Habito a remover:')
        # se o habito existir remove-lo
        if habito in utilizadores[nome]['habitos']:
            utilizadores[nome]['habitos'].remove(habito)
            print(f'Habito {habito} removido com sucesso')
        else:
            print(f'Habito {habito} não encontrado')
    else:
        print(f'Utilizador {nome} não encontrado')

def listar_habitos():
    """Função para listar os habitos, os dias consecutivos e o total de dias"""

    nome = utils.ler_string(3,'Digite o nome do utilizador:')
    if nome in utilizadores:
        print(f'Habitos de {nome}:')
        for habito in utilizadores[nome]['habitos']:
            print(f'- {habito}')
        print(f'Dias totais: {utilizadores[nome]["dias totais"]}')
        print(f'Dias consecutivos: {utilizadores[nome]["dias consecutivos"]}')
    else:
        print(f'Utilizador {nome} não encontrado')

def listar_utilizadores():
    """Função para listar os utilizadores"""
    if utilizadores:
        print('Utilizadores:')
        for nome in utilizadores:
            print(f'- {nome}')
    else:
        print('Não existem utilizadores registados')

def registar_progresso():
    """Função para registar o progresso dos habitos"""
    nome = utils.ler_string(3,'Digite o nome do utilizador:')
    if nome in utilizadores:
        habito = utils.ler_string(3,'Digite o habito a registar:')
        if habito in utilizadores[nome]['habitos']:
            data = datetime.now()
            # verificar se o habito foi registado no dia de hoje
            if 'ultimohabito' not in utilizadores[nome]:
                utilizadores[nome]['ultimohabito'] = {}
            if habito not in utilizadores[nome]['ultimohabito']:
                utilizadores[nome]['ultimohabito'][habito] = data
                print(f'Habito {habito} registado com sucesso')
                # aumentar os dias totais
                utilizadores[nome]['dias totais'] += 1
                # aumentar os dias consecutivos
                if 'ultimo_registo' not in utilizadores[nome]:
                    utilizadores[nome]['ultimo_registo'] = data
                    utilizadores[nome]['dias consecutivos'] += 1
                else:
                    # verificar se o ultimo registo foi no dia anterior
                    if (data - utilizadores[nome]['ultimo_registo']).days == 1:
                        utilizadores[nome]['dias consecutivos'] += 1
                    else:
                        utilizadores[nome]['dias consecutivos'] = 1
                    utilizadores[nome]['ultimo_registo'] = data
            else:
                print(f'Habito {habito} já foi registado hoje')
        else:
            print(f'Habito {habito} não encontrado')
    else:
        print(f'Utilizador {nome} não encontrado')