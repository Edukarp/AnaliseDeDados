import numpy as np

#Random
np.random.seed(10) #definindo uma seed de aleatoriedade
arr = np.random.randint(1, 11, 15) #15 numeros Entre 1 e 10 (primeiro inclusivo, segundo exclusivo)
print(arr)

#Unique -> retirar os elementos repetidos e mostra quantas vezes os elementos se repetem
print(np.unique(arr, return_counts=True))

mtz = arr.reshape(3,5)
print(mtz)
print(mtz.sum(axis=1)[0]) #soma de cada linha (axis=1) e retornando só a primeira
print(mtz.sum(axis=0)[0]) #soma de cada coluna (axis=0) e retornando só a primeira

#Broadcasting
print(mtz*0.5) #operacoes de vetor com escalar

#Condicionais
print(mtz)
pares = mtz%2 == 0
maiorAvg = mtz > mtz.mean()
print(mtz[pares]) #mostra os valores pares
print(mtz[maiorAvg]) #mostra os valores maiores que a media

#Analise Textual
arr = np.array(['Eduardo', 'Beatriz', 'Matheus', 'Barbara'])
result = np.char.find(arr, 'B') #case sensitive
cond = result >= 0
print(result) #mostra a posicao em que se encontra (-1 = nao tem)
print(arr[cond])