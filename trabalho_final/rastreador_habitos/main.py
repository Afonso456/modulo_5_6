import utils
from datetime import datetime,timedelta

utilizadores = {}  #Criar um dicionario vazio

# Função para adicionar os utilizadores
def adicionar_utilizador():
    nome = utils.ler_string(3,'Nome do utilizador a adicionar:')
    if nome not in utilizadores:
        utilizadores[nome] = {
            'habitos': [],
            'dias totais': 0,
            'dias consecutivos': 0
        }
        print(f'Utilizador "{nome}" adicionado.')
    else:
        print(f'Utilizador "{nome}" já existe.')

#Função para remover utilizadores
def remover_utilizador():
    nome = utils.ler_string(3,'Nome do utilizador a remover:')
    if nome in utilizadores:
        del utilizadores[nome]
        print(f'Utilizador {nome} removido com sucesso')
        print(utilizadores)
    else:
        print(f'Utilizador "{nome}" não existe.')

# Função para adicionar habitos
def adicionar_habitos():
    nome = utils.ler_string(3, 'Digite o nome do utilizador:')
    if nome in utilizadores:
        habito = utils.ler_string(3, 'Insira o hábito a ser adicionado:')
        if habito in utilizadores[nome]['habitos']:
            print(f'Habito {habito} já existe para o utilizador {nome}')    
        else:
            #guardar os habitos num dicionario
            novo = {'habitos':habito}
            utilizadores[nome]['habitos'].append(novo)
            print(f'Hábito "{habito}" adicionado para {nome}.')
    else: 
        print(f'Utilizador "{nome}" não encontrado.')
        op = input('Deseja adicionar o utilizador? (s/n):')
        if op.lower() == 's':
            adicionar_utilizador()
            print(f'Utilizador {nome} adicionado')

# Função para remover habitos
def remover_habitos():
    nome = utils.ler_string(3,'Insira o nome do utilizador a pesquisar:')
    # verificar se o utilizador existe
    if nome in utilizadores:
        # perguntar o habito a apagar
        habito = utils.ler_string(3,'Habito a apagar:')
        # se o habito existir apaga-lo
        if habito in utilizadores[nome]['habitos']:
            utilizadores[nome]['habitos'].remove(habito)
            print(f'Habito {habito} removido com sucesso')
        else:
            print(f'Habito {habito} não encontrado')
    else:
        print(f'Utilizador {nome} não encontrado')

# Função para listar os habitos, os dias consecutivos e o total de dias
def listar_habitos():
    nome = utils.ler_string(3,'Nome do utilizador a pesquisar:')
    if nome in utilizadores:
        for habito in utilizadores[nome]['habitos']:
            print(f'Habitos: {utilizadores[nome]['habitos']}')
            print(f'Total de dias: {utilizadores[nome]["dias totais"]}')
            print(f'Dias consecutivos: {utilizadores[nome]["dias consecutivos"]}')
    else:
        print(f'Não existe um utilizador com o nome {nome}')

# Função para listar os utilizadores
def listar_utilizadores():
    for utilizador in utilizadores:
        print(utilizador)

# Função para registar o progresso dos habitos
def registar_progresso():
    nome = utils.ler_string(3,'Digite o nome do utilizador:')
    habito = utils.ler_string(3,'Digite o hábito a ser registrado:')
    #data atual
    data_atual = datetime.now()
    #str da data atual
    str_data_atual = data_atual.strftime('%d-%m-%Y')
    #data do dia anterior
    data_ant = data_atual - timedelta(days = 1)
    #str da data anterior
    str_data_ant = data_ant.strftime('%d-%m-%Y')
    if nome not in utilizadores:
        print(f'Não foi possivel encontrar o utilizador {nome}.')
        if habito not in utilizadores[nome]['habitos']:
            print(f'Habito não existe para o utilizador {nome}')
    else:
        utilizadores[nome]['habitos'].append(str_data_atual)
        print(f'Hábito "{habito}" registado em {str_data_atual} para {nome}.')