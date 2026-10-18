
print('Digite 3 numeros: ')
n1 = float(input())
n2 = float(input())
n3 = float(input())
if n1 > n2 and n1 > n3:
    print('Primeiro numero é o maior entre os 3')
if n2 > n1 and n2 > n3:
    print('Segundo numero é o maior entre os 3')
if n3 > n1 and n3 > n2:
    print('Terceiro numero é o maior entre os 3')
if n1 == n2 and n2 == n3:
    print('Os numeros tem o mesmo valor')