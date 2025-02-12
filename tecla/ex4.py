valor_base={
1:1500,
    2:3000,
    3:4500,
    4:6000,
    5:7500,
    6:9000,
    7:10500,
    8:12000,
    9:13500,
    10:15000
}
 
licitacoes={}
op = ""
while op!="fim":
    try:
        linha=input("")
        if linha!="fim":
            dados = linha.split(" ")
            nome = dados[0]
            numero = int(dados[1])
            valor = int(dados[2])
            if valor_base[numero]<=valor:
                if numero not in licitacoes:
                    licitacoes[numero]={'nome':nome,'valor':valor}
                else:
                    if valor>licitacoes[numero]['valor']:
                        licitacoes[numero]={'nome':nome,'valor':valor}
        else:
            break
    except:
        continue
 
if len(licitacoes.keys())==0:
    print("Nenhuma viatura licitada")
else:
    for i in range(10):
        if (i+1) in licitacoes:
            print(f"{i+1} {licitacoes[i+1]['valor']} {licitacoes[i+1]['nome']}")