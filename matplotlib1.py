import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([1,2,3,4]) #Criando valores no eixo X
y = x*2 #Criando valores no eixo Y
y2 = x**2

#Criando as Labels das coordenadas X e Y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

#o -> marcador cicular, : -> linhas pontilhadas g -> verde, largura da linha, tamanho dos marcadores
plt.plot(x, y, 'o:g', linewidth=3, markersize=15) #Executando o plot
plt.show() #Mostrando o plot

#Mostrando dois graficos juntos
plt.plot(x,y, 'r-', x, y2,'b--')
plt.show() #Mostrando o plot

#Subplots
plt.subplot(1, 2, 1) #Numero de linhas, numero de colunas, posicao que ocupara
plt.title("Linear")
plt.plot(x, y, '-r')

plt.subplot(1, 2, 2)
plt.title("Exponencial")
plt.plot(x,y2, 'b--')

plt.show() #Mostrando o plot

