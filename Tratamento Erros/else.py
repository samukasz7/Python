try:
    numero = float(input('Digite um número: '))
    resultado = 10 / numero

    
except ValueError as erro:
    print(f'Erro ocorrido: {erro}')
except ZeroDivisionError as erro:
    print(f'Erro ocorrido: {erro}')
else:
    print(f'O resultado é {resultado}')
finally('Fim do calculo!')