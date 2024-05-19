### 3 saques diarios, limite max 500rs p saque; Return>Não será possível sacar o dinheiro por falta de saldo.
###valores : R$ xxxxx,xx
### extrato deve listar todos depositos e saques realiziadso e o saldo atual
extrato = []
saldo = 0.00
limite_diario = 500.00
limite_saques_diario = 3
numero_saques = 0

while True:


    acao = input('''Envie
                    d para deposito
                    s para saque
                    e para extrato
                    q para sair
                ''')

    if (acao == "s"):
        valor = int(input('Qual valor para saque? '))
        if (saldo >= valor and numero_saques < 3):
            if (valor <= 500):
                saldo -= valor
                numero_saques += 1
                extrato.append(f'Saque no valor de R${valor} realizado com sucesso')
                print(f'Saque no valor de R${valor} realizado com sucesso')
            else:
                print(f'O valor máximo para saque é de R$500,00')

        elif (numero_saques >= 3):
            print('Você já realizou 3 saque diários.')

        elif (saldo < valor):
            print (f'Não é possível realizar o saque. Você esta tentando sacar {valor}, porém o saldo na conta é de R${saldo}')


    elif (acao == "d"):
        valor = int(input('Qual valor para deposito? '))
        saldo += valor
        extrato.append(f'R${valor} foi depositado com sucesso.')

        print(f'R${valor} foi depositado com sucesso.')


    elif (acao == "e"):
        extrato.append(f'Saldo atual: R${saldo}')
        extrato = str(extrato).replace(",", "\n").replace("[","").replace("]","")
        print(extrato)

    elif (acao == 'q'):
        break
