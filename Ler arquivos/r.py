with open('putas.txt', 'r', encoding='utf-8') as arquivo3: 
    nomes = arquivo3.readlines()
    for nome in nomes:
        print(nome)






#O r serve para ler um arquivo.
#read()        lê o arquivo inteiro
#readline()    lê uma linha
#readlines()   lê todas as linhas e coloca em uma lista