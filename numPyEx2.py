import numpy as np

#Ex1
np.random.seed(5)
arr10 = np.random.rand(10)
int100 = arr10*100
int100 = int100.astype(int)
print(int100)

#Ex2
np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape(4, 4)
print(mtz)

#Ex3
print(mtz.mean(axis=1)) #media de cada linha (axis=1)
print(mtz.mean(axis=0)) #media de cada coluna (axis=0)
print("Maior valor da linha:",mtz.mean(axis=1).max())
print("Maior valor da coluna:",mtz.mean(axis=0).max())

#Ex4
mtz2 = np.unique(mtz, return_counts=True)
print(mtz2[1])
igual2 = mtz2[1] == 2
print(mtz2[0][igual2])