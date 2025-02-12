altura_obj = float(input("Altura do objeto:"))
c_sombra= float(input("Comprimento da sombra do objeto:"))
c_sombra_edificio = float(input("Altura das ombra do  predio em metros:"))

total= (altura_obj * c_sombra) / c_sombra_edificio
print(total)