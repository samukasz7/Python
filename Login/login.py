usuario = input('Digite seu usuario: ')
senha_verdadeira = 'aura123'
tentativas = 0
while tentativas < 3:
    senha = input('Digite sua senha: ')
    if senha != senha_verdadeira:
     print('Senha incorreta')
     tentativas += 1

    if senha == senha_verdadeira:
        print('Acesso Liberado')
        break

    elif tentativas == 3:
        print('Acesso bloqueado')