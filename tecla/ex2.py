ivaucher= float(input("Introduza o IVaucher:"))
valor_compra= float(input("Valor compra:"))

total = float(ivaucher) - float(valor_compra)
total_iva= total + (valor_compra / 2)
print(total_iva)