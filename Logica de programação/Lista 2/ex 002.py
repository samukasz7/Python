valor_carro = int(input('Digite o valor de fabrica do carro: '))
imposto = valor_carro * 45 / 100
lucro_distribuidor = valor_carro * 12 / 100
total_pagar = valor_carro + imposto + lucro_distribuidor
print(f'O total a pagar é {total_pagar}')