def n_inteiro(mensagem= "Introduza um valor inteiro:")->int:
    """
    Função que lê do utilizador um numero interiro. A função garante que o valor inserido é valido
    """
    while True:
        dados= input(mensagem)
        if len(dados) == 0:
            continue
        #verificar se existe um - no inicio do nº(valor negativo)
        if dados[0] == "-":
            testar= dados.replace('-', '')
        else:
            testar= dados
        if testar.isdigit():
            return int(dados)
        print("Erro: o valor inserido não é valido")

def minimo_maximo_inteiro(min, max= None, mensagem = "Introduza um nº inteiro:"):
    """
    Função que recebe o valor minimo e maximo dados pelo utilizador. A função devolve o valor quando é um inteiro valido
    """
    while True:
        n= n_inteiro(mensagem)
        if n >= min and (max is None or n <= max):
            return n
        print("Erro: o valor não é valido")

def n_decimal(mensagem= "Introduza um nº decimal:")-> float:
    """
    Função que lê um nº decimal. A função garente que o valor é valido e aceita como separador das casas decimais . ou ,
    """
    while True:
        dados= input(mensagem)
        if len(dados)==0:
            continue
        #substituir , por .
        dados= dados.replace(',', '.')
        #verificar se existe um - no inicio do nº(valor negativo)
        if dados[0] == "-":
            testar= dados.replace('-', '')
        else:
            testar= dados
        #contar os pontos decimais
        pontos= testar.count('.')
        #remover os pontos decimais
        testar= dados.replace('.', '')
        if testar.isdigit() and pontos <= 1:
            return float(dados)
        print("Erro: o valor inserido não é valido")

def minimo_maximo_decimal(min, max= None ,mensagem= "Introduza um valor:")-> float:
    """
    Função para ler um valor decimal entre limites. Função garante a validade do valor 
    """
    while True:
        valor= n_decimal(mensagem)
        if valor >= min and (max is None or valor <= max):
            return valor
        print("Erro: valor não é valido")


def menu(opcoes,titulo=""):
    """
    Função recebe as opções a mostrarde um menu
    Lê a opção do utilizador e indica se é valida ou não
    """
    #mostrar o titulo do menu
    if titulo != "":
        print(titulo)

    #mostrar as opções com um nr ao lado
    for i in range(len(opcoes)):
        print(f"{i+1}.{opcoes[i]}")

    #ler a opção do utilizador e se não for valida apresentar um erro
    op= minimo_maximo_inteiro(1, len(opcoes)), ("Opção")
    #se for valida devolvemos a opção escolhida
    return op 

def media(valores):
    """
    Função que recebe um tupulos de valores e devolve a media desses mesmos 
    """
    return sum(valores) / len(valores)