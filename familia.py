"""
Uma familia tem 3 pessoas. Pretende um programa que utiliza um dicionario para registar o nome de cada um e a marca do respetivo telemovel e computador
O programa deve indicar qual a marca mais comum e se algum membro da familia tem so uma marca
"""

familia= {}

for membro in familia:
    marca_t= input("Marca do telemovel:")
    marca_c= input("Marca do computador:")
    familia["telemovel"] = marca_t
    familia["computador"] = marca_c
    if familia["telemovel"] == familia["computador"]:
        print(f"O membro {membro} da familia usa somente uma marca")
