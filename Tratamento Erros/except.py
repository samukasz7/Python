try: 
    n1 = int(input('Digite  um número: '))
    n2 = int(input('Digite outro número: '))
    resultado = n1 + n2

    print(f'A soma de {n1} e {n2} é {resultado}')
except:
    print('Digite um número válido!')