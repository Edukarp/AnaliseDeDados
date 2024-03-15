import numpy as np

#Ex1
array21 = np.arange(0, 21, 1)
print(array21, "tamanho:", array21.size)

#Ex2
array51 = np.arange(0, 51, 2)
array100 = np.arange(100,50, -2)
print(np.concatenate([array51, np.sort(array100)]))

#Ex3
print(np.flip(np.concatenate([array51, np.sort(array100)])))

#Ex4
matriz1 = np.ones([3, 4])
print(matriz1.reshape(12))

#Ex5
matriz = np.zeros([5, 4])
numL = matriz.shape[0]
numC = matriz.shape[1]
arrayMult = np.zeros([numL*numC])
if arrayMult.size%2 == 0:
    print(arrayMult.size, "elementos, sendo assim, uma quantidade PAR")
else:
    print(arrayMult.size, "elementos, sendo assim, uma quantidade IMPAR")
