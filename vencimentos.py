vencimentos = (1000,5000,2500,1350,4750,850) 
nomes       = ("A", "B", "C", "D", "E", "F")

#utilizando uma função calcular e devolver a soma de todos os vencimentos, o maior e o menor 
def vencimento(vencimentos):
    soma  = sum(vencimentos)
    maior = max(vencimentos)
    menor = min(vencimentos)
    estatisticas = soma,maior,menor
    return estatisticas

soma, maior, menor = vencimento(vencimentos)
print(f"A soma dos vencimentos é de {soma}, o maior vencimento é de {maior} e o menor vencimento é de {menor}")

#calcular e mostrar a media dos vencimentos
media = soma / len(vencimentos)
print(media)

#mostrar o nome de quem tem o maior vencimento
pessoa = vencimentos.index(maior)
print(f"A pessoa com o maior vencimento é a {nomes[pessoa]} com um vencimento de {maior}")
