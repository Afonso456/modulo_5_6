"""
Programa que mostra a capital de um estado recebido do utilizador
""" 
capitais= {"Portugal" : "Lisboa",
           "Espanha" : "Madrid",
           "França" : "Paris",
           " Brasil" : "Brasilia",
           "Inglaterra" : "Londres",
           "Italia" : "Roma"}

#perguntar ao utilizador o pais
pais= input("Introduza o pais pretendido:")
"""
if pais not in capitais:
    print("Sou burro e não conheço a capital desse pais")
else:
#mostrar a capital correspondente
    print(capitais[pais])
"""
#utilizar a função get 
print(capitais.get(pais,"Não tennho informações sobreesse pais"))