def maior_numero(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = [4, 8, 9, 2, 5]
maior_numero_da_lista = maior_numero(lista)
print(f'O maior numero da lista é {maior_numero_da_lista}')