import random

saldo = 100

while saldo > 0:
    print(f"Saldo: R${saldo}")

    aposta = int(input("Quanto deseja apostar? "))

    numero = random.randint(1, 2)

    if numero == 1:
        print("Você ganhou!")
        saldo += aposta
    else:
        print("Você perdeu!")
        saldo -= aposta