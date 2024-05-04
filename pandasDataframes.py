import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(data=np.random.randint(1, 50, [5, 4]),  # interios aleatorios entre 1 e 50 no shape 5x4
                  index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'])
print(df, '\n')
print(df['X'], '\n')

#Slicing
#Passando uma lista de linhas e uma lista de todas as colunas
print(df.loc[['B','C'], ['W','X','Y','Z']])
print(df.iloc[1:3, :]) #iloc usa os indices numericos igual o numpy

#Importando dataseets
dfPaises = pd.read_csv('arquivos/paises.csv', delimiter=';')
print(dfPaises.columns) #Filtra somente as colunas
#print(dfPaises['Country']) #Filtra somente o nome dos paises
print(dfPaises.head(3)) #3 primeiros paises
print(dfPaises.tail(3)) #3 ultimos paises
dfPaises['Country'].to_csv('arquivos/nomePaises.csv',
                           sep=';', header=False) #Exportando arquivo somente com o nome dos paises