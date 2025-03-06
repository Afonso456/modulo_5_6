partidoA= {"a","b","c"}
partidoB= {"a","k","y"}
partidoC= {"a","b","z","t"}

#listar os elementos repetidos
partido_a_b= partidoA.intersection(partidoB)
partido_a_c= partidoA.intersection(partidoC)
partido_b_c= partidoB.intersection(partidoC)
repetidos_todos= partido_a_b | partido_b_c | partido_b_c
print(f"O elemento repetido em pelo menos 2 partidos são o: {repetidos_todos}")

#listar os repetidos em todos os partidos
partidos_a_b_c= partidoA & partidoB & partidoC
print(f"O elemento que está em todos os partidos é o {partidos_a_b_c}")

#listar os elementos de cada partido sem ser repetido
print(f"Partido A {partidoA.difference(repetidos_todos)}")
print(f"Partido B {partidoB.difference(repetidos_todos)}")
print(f"Partido C {partidoC.difference(repetidos_todos)}")
