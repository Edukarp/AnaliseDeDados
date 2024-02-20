#Tuplas
print("Sobre Tuplas")
nomesT = ('Mario', 'Luigi', 'Peach', 'Dayse')
print(nomesT[0])
print(nomesT[:2]) #Primeiro argumento Inclusive, segundo argumento Exclusivo
print(nomesT[1:3])
print(nomesT[-2])
#nomes[0] = 'Yoshi' #Colecao imutavel, sem add, sem delete, sem update.
print("--------------------------------\n")

#Listas
print("Sobre Listas")
nomesL = ['Mario', 'Luigi', 'Peach', 'Dayse']
#Add
nomesL.append('Yoshi') #Adiciona no final da lista
#Update
nomesL[0] = 'Wario'
#Delete
nomesL.pop(1) #deletando por indice
#del nomesL[1] #deletando por indice
nomesL.remove('Dayse') #deletando por valor
#Select
print(nomesL)
print("--------------------------------\n")

#Sets (Conjuntos)
print("Sobre Sets")
nomesS = {'Mario', 'Luigi', 'Peach', 'Dayse'}
nomesS.add('Toad') #Add
nomesS.add('Mario') #Nao permite elementos repetidos
print(nomesS) #Nao possuem Index especifico (elementos desordenados)
nomesS.remove('Peach') #Delete
#Update -> Nao funciona, necessario deletar um elemetno e add outro
print("--------------------------------\n")

#Dictionary
print("Sobre Dictionary")
pessoa = { #Indices customizaveis
    'nome': 'Mario',
    'idade': 30
}
#Add
pessoa['sexo'] = 'M'
#Update
pessoa['nome'] = 'Luigi'
#Delete
del pessoa['idade']
#Select
print(pessoa)
print("--------------------------------\n")

#Colecoes Aninhadas
#Criando um dicionario so pro ex
pessoa2 = {
    'nome': 'Peach',
    'idade': 28
}
pessoas = [pessoa, pessoa2]
print(pessoas[1]['nome'])