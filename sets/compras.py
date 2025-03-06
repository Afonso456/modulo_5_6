"""
Pretendemos criar um sistema de recomendação de produtos que o joão ainda não comprou 
mas que pertencem a uma categoria de produtos que já atenha
"""

#compras
joao       = {"tv", "sapatos" , "tablet"}

#categorias de recomendação
roupa      ={"calções","casaco", "t_shirt"}
calcado    = {"sapatos","botas","sapatilhas"}
eletronica ={"tv", "tablet", "pc", "xbox"}

#recomendar produtos cuja categoria pertence a um produto que o joão ja comprou mas cujo produto ainda não comprou
joao_roupa= joao.intersection(roupa)
if len(joao_roupa) > 0:
    roupa_para_joao= roupa.difference(joao)
    print(f"Recomendamos para o João {roupa_para_joao}")

joao_calcado= joao.intersection(calcado)
if len(joao_calcado) > 0:
    calcado_para_joao= calcado.difference(joao)
    print(f"Recomendamos para o João {calcado_para_joao}")


joao_eletronica= joao.intersection(eletronica)
if len(joao_eletronica) > 0:
    eletronica_para_joao= eletronica.difference(joao)
    print(f"Recomendamos para o João {eletronica_para_joao}")