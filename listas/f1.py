#Coleção F1
'''
PSI - Módulo 6
Coleções - F1
'''
 
GrandePremios = [
    {"Número": 1, "Grande Premio": "Barém", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 2, "Grande Premio": "Arábia Saudita", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 3, "Grande Premio": "Austrália", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número": 4, "Grande Premio": "Japão", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 5, "Grande Premio": "China", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 6, "Grande Premio": "Miami", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 7, "Grande Premio": "Emília-Romanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 8, "Grande Premio": "Mônaco", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 9, "Grande Premio": "Canadá", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 10, "Grande Premio": "Espanha", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 11, "Grande Premio": "Áustria", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 12, "Grande Premio": "Grã-Bretanha", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 13, "Grande Premio": "Hungria", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 14, "Grande Premio": "Bélgica", "Vencedor": "Lewis Hamilton", "Equipa": "Mercedes"},
    {"Número": 15, "Grande Premio": "Países Baixos", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 16, "Grande Premio": "Itália", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 17, "Grande Premio": "Azerbaijão", "Vencedor": "Oscar Piastri", "Equipa": "McLaren-Mercedes"},
    {"Número": 18, "Grande Premio": "Singapura", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"},
    {"Número": 19, "Grande Premio": "Estados Unidos", "Vencedor": "Charles Leclerc", "Equipa": "Ferrari"},
    {"Número": 20, "Grande Premio": "Cidade do México", "Vencedor": "Carlos Sainz Jr.", "Equipa": "Ferrari"},
    {"Número": 21, "Grande Premio": "São Paulo", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 22, "Grande Premio": "Las Vegas", "Vencedor": "George Russell", "Equipa": "Mercedes"},
    {"Número": 23, "Grande Premio": "Catar", "Vencedor": "Max Verstappen", "Equipa": "Red Bull Racing-Honda RBPT"},
    {"Número": 24, "Grande Premio": "Abu Dhabi", "Vencedor": "Lando Norris", "Equipa": "McLaren-Mercedes"}
]


# Quem ganhou o GP de São Paulo
for GP in GrandePremios:
     if GP["Grande Premio"] == "São Paulo":
          print(f"O vencedor de São Paulo foi " ,[GP["Vencedor"]])
 
# Quais os grandes prémios que ganhou a Ferrari
for GP in GrandePremios:
     if GP["Equipa"] == "Ferrari":
          print(f"O grande prémio que ganhou a Ferrari foi " ,[GP["Grande Premio"]])

# Quais os Grande Prémios que um determinado piloto ganhou (escolha do utilizador)
piloto = input("Introduza o piloto a pesquisar:")
for GP in GrandePremios:
     if GP["Vencedor"] == piloto:
        print(f"O Grande Premio que o {piloto} ganhou foi" , [GP["Grande Premio"]])

# Lista de vencedores (só aparece uma vez)
vencedores = []
for GP in GrandePremios:
     if GP["Vencedor"] not in vencedores:
        vencedores.append(GP["Vencedor"])
        print({GP['Vencedor']})

# Lista de construtores que ganharam provas (só aparece uma vez)
construtores = []
for GP in GrandePremios:
     if GP["Equipa"] not in construtores:
          construtores.append(GP["Equipa"])
          print({GP['Equipa']})

# Mostrar quantos grandes prémios ganhou cada um desses pilotos
for piloto in vencedores:
    contagem = 0
    for GP in GrandePremios:
        if GP["Vencedor"] == piloto:
            contagem += 1
    print(f"O piloto {piloto} ganhou {contagem} grandes premios")        