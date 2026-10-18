try:
    idade = int(input('Digite sua idade: '))
    if idade < 0:
        raise Exception('Digite uma idade válida!')
except Exception as erro:
    print(f'Erro: {erro}')
else:
    print(f'Sua idade é: {idade}')