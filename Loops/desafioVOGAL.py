palavra = input('Digite uma palavra: ')

vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0

for i in palavra:
    if i in vogais:
        contador += 1

print(f'A palavra tem {contador} vogais')