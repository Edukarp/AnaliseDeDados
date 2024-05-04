import pandas as pd
import numpy as np

#Series (1 Dimensao)
dic = {'A': 10, 'b': 20, 'c': 30}
labels = ['a', 'b','c'] #Indices Customizaveis
dados = [20, 30, 40]
s = pd.Series(data= dados, index= labels)
s1 = pd.Series(dic)
print(s + s1)
print(s.add(s1, fill_value=0)) #Soma elemento a elemento, e valores vazios = 0 #sub(), mul(), div(), pow(), mod()

print(s['a'])
print(s[['b', 'c']])

print("Valores Maiores que 10 em s1:\n", s1[s1 > 10])