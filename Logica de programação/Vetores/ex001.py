vetor = []
for i in range (20):
    valores = int(input('Digite 20 valores: '))
    vetor.append(valores)
for posicao in range(1, 20, 2):
    print(f'Valor: {vetor[posicao]}')