"""
Calcular o nr de vezes que um carro aparece no array guardando num dicionario a marca e o nr de carros
p.e:
    {"bmw":2,
    " tesla":2,
    "peugeot":1}
"""
import numpy as np

carros=np.array(["bmw","mercedes","audi","bmw","bmw","bmw","mercedes","mercedes","mercedes","mercedes"])
marcas= {}
#ciclo para percorrer o array das marcas
for carro in carros:
    """
    #verificarse a marca ja existe no dicionario
    if carro in marcas:
        marcas[carro] = marcas[carro] + 1
    else:
        marcas[carro] = 1
    """
    marcas[carro]= marcas.get(carro,0) + 1
print(marcas)

