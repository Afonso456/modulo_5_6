"""
Referencias entre dicionarios e dicionarios com arrays
"""
marca1={"nome":"nike","tipo":"calçado","pais":"Estados Unidos"}
marca2={"nome":"adidas","tipo":"roupa e calçado","pais":"alemão"}
marca3={"nome":"mimosa","tipo":"alimento","pais":"portugal"}

produto1={"nome":"sapatilhas","preco":85.45,"marca":marca2}
#mostrar o país da marca
print(produto1["marca"]["pais"])
marca2["pais"]= "Japão"
print(produto1)

produto2= {"nome":"casaco","preco":100,"marca":marca2}
print(produto2)

marca2= {}
print(produto1)
print(produto2)