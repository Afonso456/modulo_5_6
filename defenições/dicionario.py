def adicionar(dicionario):
    """
    Função para adicionara palavras e as suas Sdefenições
    """
    palavra= input("Insira a palavra:")
    defenicao= input("Insira a defenição da palavra:")
    op= ""
    if palavra in dicionario:
        op= input("Deseja alterar a palavra (s/n)?\n")
    if op == "n":
        return
    elif op == "s":
        palavra= input("Insira a palavra a alterar:")
        defenicao= input("Insia o significado da palavra:")
        dicionario[palavra]= defenicao

def listar(dicionario):
    """
    Função para mostrar as palavras e as suas defenições
    """
    op= input("Deseja listar por ordem alfabetica(s/n)?\n")
    if op != "s":
        for palavra,defenicao in dicionario.items():
            print(f"{palavra} -> {defenicao}")
    else:
        #ordenar as chaves
        chaves = dicionario.keys()
        chave= sorted(chaves)
        #percorrer as chaves ordenadas e mostrar o seu valor
        for palavra in chave:
            print(f"{palavra} -> {dicionario[palavra]}")

def pesquisar(palavra,dicionario):
    """"
    Função para mostrar a palavra e a sua defenição procurada pelo utilizador
    """
    for chave,defenicao in dicionario.items():
        if palavra == chave[:len(palavra)]: #slicing apenas para comparar o inicio da chave
            print(f"{palavra} -> {defenicao}")

def apagar(palavra,dicionario):
    """
    Função para apagar uma palavra e a sua defenição
    """
    op= ""
    op= input("Deseja apagar a palavra (s/n)?\n")
    if op == "s":
        if palavra in dicionario:
            del dicionario[palavra]
            print("Plavra apagada com sucesso")
    else:
        print(f"A palavra {palavra} não existe no dicionário")

def configurar(dicionario):
    """"
    Função para configurar o dicionario
    """
    dicionario["pêra"]= "fruta"
    dicionario["pc"] = "computador pessoal"
    dicionario["bicicleta"]= "meio de transporte"

#se o programa estiver em desenvolvimento a variavel esta em_teste é True
#se o programa estiver acabado a variavel em_teste é False
em_teste= True