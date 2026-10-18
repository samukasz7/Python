try:
    numero = float(input('Digite um número: '))
    resultado = 10 / numero

    print(f'O resultado é {resultado}')
except ValueError as erro:
    print(f'Erro ocorrido: {erro}')
except ZeroDivisionError as erro:
    print(f'Erro ocorrido: {erro}')