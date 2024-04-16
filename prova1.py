import numpy as np

arr = np.loadtxt('arquivos/brands.csv', delimiter=';',dtype= str, encoding='utf-8')

#Exercicio 1
google = np.char.find(arr[:, 0], 'Google') >= 0
print("Valorizacao do Google($M):", (arr[google][:, 9]).astype(float) - (arr[google][:, 10]).astype(float))

#Exercicio 2
quantGroup = (arr[np.char.find(arr[:, 0], 'Group') >= 0, 1]).size
#quantGroup = np.char.find(arr[:, 0], 'Group') >= 0     #print(arr[quantGroup, 1].size)     #Outra forma
print("Quantidade de Marcas que Possuem 'Group' em seu nome:", quantGroup)

#Exercicio 3
valor23 = (arr[1:6, 9]).astype(float)*1.1
print("Valor das estimativas de aumento de 10% para o Ano de 2023 nas primeiras 5 emarcas:", valor23)

#Exercico 4
slicing = arr[1:, :3]
#print("Empresas fundadas apos os anos 2000:\n", slicing[np.char.find(slicing[:, 2], "200") >= 0]) #Errado
print("Empresas fundadas apos os anos 2000:\n", slicing[slicing[:, 2].astype(int) > 2000]) #Certo

#Exercicio 5
anos = np.unique(arr[1:, 2], return_counts=True)
print("Ano que mais empresas foram fundadas:",anos[0][np.argmax(anos[1])])
