import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('space.csv',delimiter=';')

#Exercicio 1
#df2 = df[df['Location'].str.contains('USA', case=True) | df['Location'].str.contains('China', case=True)]

#Separando as empresas pela localizacao (se conter USA ou China, e sensitive case ativado)
dfUsa = df[df['Location'].str.contains('USA', case=True)]
dfChina = df[df['Location'].str.contains('China', case=True)]

#Pegando a quantidade de empresas e tirando as empresas repetidas
dfChina_comp = dfChina['Company Name'].value_counts().drop_duplicates()
dfUsa_comp = dfUsa['Company Name'].value_counts().drop_duplicates()

country_counts = { #Fazendo um dicionario, o 'nunique' é igual um len()
    'China': dfChina_comp.nunique(),
    'USA': dfUsa_comp.nunique()
}

# Convertendo o dicionário para um DataFrame
country_counts_df = pd.DataFrame(list(country_counts.items()), columns=['Country', 'Unique Companies'])

# Plotando o gráfico de barras
#plt.bar(dfChina_comp.index.values, dfChina_comp) #Plotando a quantidade de cada empresa da China
plt.bar(country_counts_df['Country'], country_counts_df['Unique Companies'],
        color=['red','blue'])
plt.title('Quantidade de Empresas Únicas por País')
plt.xlabel('País')
plt.ylabel('Quantidade de Empresas')
plt.show()

#Exercicio 2
df = pd.read_csv('paises.csv',delimiter=';')

print(df.columns)
dfNA = df[df['Region'].str.strip() == 'NORTHERN AMERICA']

dfNA_birthrate = dfNA['Birthrate'].astype(float)
dfNA_deathrate = dfNA['Deathrate'].astype(float)
x = dfNA['Country'] #Definindo a variavel x do grafico como o pais

#Mostrando dois graficos juntos
plt.plot(x,dfNA_deathrate, 'r-', label='Deathrate')
plt.plot(x,dfNA_birthrate,'b--', label='Birhrate')
plt.title('Birthrate e Deathrate em NORTHERN AMERICA')
plt.xlabel('Country')
plt.ylabel('Rate')
plt.legend() #Usando as labels
plt.show() #Mostrando o plot