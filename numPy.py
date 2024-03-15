import numpy as np

'''
#diferente das Listas os Arrays guardam apenas um mesmo tipo
array = np.array([1, 2, 3])
print(array)
print(type(array))

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

matriz5 = np.ones([5, 5])
print(matriz5)

arr = np.zeros(10)
print(arr)

            #incio/fim/passo    linhas/colunas (com um valor volta ser unidimensional)
arr2 = np.arange(20, 30, 1).reshape(5, 2)
print(arr2)
'''

#Opercaoces entre Arrays

jan = np.arange(20,30,1)
fev = np.arange(40,50,1)
print(jan)
print(fev)
print(jan+fev) #somando elemento por elemento
print(np.concatenate([jan, fev]).reshape(5, 4))

print(jan.size) #tamanho
print(jan.ndim) #numero de dimensoes
print(jan.shape) #shape

