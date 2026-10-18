try:
    frutas = ['maçã', 'banana', 'pera']
    print(frutas[3])

except IndexError as erro:
    print(f'Indice invalido {erro}')