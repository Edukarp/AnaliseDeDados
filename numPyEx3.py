import numpy as np

arr = np.loadtxt('arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')

#Ex1
arrAux = np.char.find(arr, 'Success')
arrSucess = arr[arrAux >= 0]
print("Porcentagem de Sucesso: {:.2f}%".format(((arrSucess.shape[0])/(arr.shape[0] - 1))*100))


#Ex2
gastos = arr[1:, 6]
print("Media de Gastos: {:.2f}".format( np.mean(gastos.astype(float))))

#Ex3
pais = np.char.find(arr[: , 2], 'USA')
arrPais = arr[pais >= 0]
print("Missoes Realizadas pelos EUA:", arrPais.shape[0])

#Ex4
maisCara = (np.char.find(arr[:, 1], 'SpaceX') >= 0)
print("Missao mais cara da SpaceX:", arr[:, 6][maisCara].astype(float).max())

#Ex5
nome = np.unique(arr[1:, 1], return_counts=True)
for i in range(nome[0].size):
        print("Compania:", nome[0][i], "Quantidade de Missoes:", nome[1][i])