import numpy as np

arr = np.loadtxt('arquivos/paises.csv', delimiter=';', dtype=str, encoding='utf-8')

#Ex1
slicing = arr[1:, :4]
#print(slicing)

#Ex2
regioes = np.unique(arr[1:, 1])
print("Regioes:", regioes, "\nQuantidade de regioes:", regioes.size)

#Ex3
alfab = arr[1:, 9]
print("Media de Alfabetizacao: {:.2f}".format(np.mean(alfab.astype(float))))

#Ex4
amrNorte = (np.char.find(arr[:, 1], 'NORTHERN AMERICA') >= 0)
print("Quantidade de Paises na America do Norte:", arr[amrNorte, :1].size)

#Ex5
maiorGDP = (np.char.find(arr[:, 1], 'LATIN AMER. & CARIB') >= 0)
aux = np.argmax(arr[:, 8][maiorGDP].astype(float)) #argmax retorna o indice
print("Pais com maior Renda PerCapta:", arr[:, 0][aux], "com renda PerCapta de:", arr[:, 8][aux])