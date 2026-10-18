with open('streamers.txt', 'r+', encoding='utf-8') as arquivo4:
    stream = arquivo4.readlines()

    for nome in stream:
        print(nome)

    arquivo4.write('Laiobas')

    #r+ permite ler e escrever no mesmo arquivo.