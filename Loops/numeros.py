numeros = [2, 3 , 23, 67, 6, 10, 12, 92]
for verificar in numeros:
    if verificar % 2 == 0:
        print(f'Essas porras é par: {verificar}')

numeros2 = [2, 3 , 23, 67, 6, 10, 12, 92]
for verifica in numeros2:
    if verifica % 2 == 0:
        continue
    print(f'Essas porras é impar: {verifica}')