import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dfPaises = pd.read_csv('arquivos/paises.csv',delimiter=';')

print(dfPaises.columns)
dfPaises2 = dfPaises.nlargest(6, 'Area (sq. mi.)') #Extraindo os dados dos 6 maiores paises
#Plotando qual destes paises possui a maior renda per capita
plt.scatter(x=dfPaises2['Country'],
            y=dfPaises2['GDP ($ per capita)'],
            s=dfPaises2['Area (sq. mi.)']/10000) #Size, divide pra ficar proporcional e visivel
plt.show() #O tamamnho de cada ponto ilustra o tamanho desse pais, isso é dado pelo parametro s=...