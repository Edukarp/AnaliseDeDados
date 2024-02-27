#Ex1
colocacao = ['Argentina','França','Croacia','Marrocos','Paises Baixos']

#letra A
print(colocacao[:3])
#letra B
print(colocacao[3:])
#letra C
colocacao.sort()
print(colocacao)
#letra D
posicao = colocacao.index("Marrocos")
print("Marrocos, apos a ordenacao, esta na posicao", posicao, "\n")

#Ex2
loja1 = {"Motorola", "Sansung", "Apple","Nokia"}
loja2 = {"Sansung", "Apple"}
print("Loja 1:", len(loja1), "modelos", "\nLoja 2:", len(loja2), "modelos")
print("Total de modelos disponiveis:", len(loja1.union(loja2)), ",sendo eles:", loja1.union(loja2))
print("Os modelos disponiveis em ambas as lojas sao:", loja1.intersection(loja2), "\n")

#Ex3
nome = "aluno1"
media = 76
dic = {"nome": nome,
       "media": media}
if dic['media'] < 60:
    dic['Situacao'] = 'RP'
else:
    dic['Situacao'] = 'AP'

print(dic)