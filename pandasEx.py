import pandas as pd
import numpy as np

dfPaises = pd.read_csv('arquivos/paises.csv', delimiter=';')

#print(dfPaises)
print(dfPaises.columns)

#Exercicio 1
#letra A
paisesOceania = dfPaises[dfPaises['Region'].str.strip() == 'OCEANIA'] #str.strip() para tirar os espaços em branco
#paisesOceania = dfPaises[dfPaises['Region'].str.contains('OCEANIA')] #Outra forma usando o contains()
print("PAISES NA OCEANIA:\n",paisesOceania)
#letra B
print("Quantidade de países na Oceania:",len(paisesOceania))

#Exercicio 2
print("Taxa de alfabetizacao:{:.2f}%".format(dfPaises['Literacy (%)'].mean())) #aparentemente nao precisa passar um .astype(float) antes

#Exercicio 3
maiorPais = np.argmax(dfPaises['Population'])
print("Pais:", dfPaises['Country'][maiorPais],
      "Regiao:", dfPaises['Region'][maiorPais])

#Exercicio 4
noCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]['Country'].to_csv('arquivos/noCoast.csv',
                                                                                    sep=';', header=False)