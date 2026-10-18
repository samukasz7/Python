def calcular_desconto(preco):
    return preco * 0.9

valor_final = calcular_desconto(100)

print(f'Você vai pagar R$ {valor_final}')



def verificar_par(numero):
    if numero % 2 == 0:
        print('É par')
    else:
        print('É impar')
        
verificar_par(5)