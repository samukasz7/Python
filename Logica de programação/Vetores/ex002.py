vetor = []
vetor2 = []

for i in range(20):
    valores = int(input('Digite um valor: '))
    vetor.append(valores)

for i in vetor:
    if i > 0:
        i = i * 2
        vetor2.append(i)

    if i < 0:
        i = i * -1
        vetor2.append(i)

print(vetor)
print(vetor2)