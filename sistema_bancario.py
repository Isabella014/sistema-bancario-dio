usuarios = {}

def filtrar_usuario(cpf):
    return usuarios.get(cpf)

def criar_usuario():
    cpf = input('Digite seu CPF: ')
    if filtrar_usuario(cpf):
        print('Já existe um usuário cadastrado com esse CPF')
        return None
    nome = input('Insira seu nome: ')
    data_nascimento = input('Insira sua data de nascimento: ')
    endereco = input('Insira seu endereço: ')
    usuarios[cpf] = {
        'nome': nome,
        'data de nascimento': data_nascimento,
        'endereço': endereco,
        'contas': {}
    }
    print('Usuário criado com sucesso')
    return cpf

def criar_conta(cpf):
    if not filtrar_usuario(cpf):
        print('Usuário não encontrado')
        return
    numero_conta = input('Digite o número da conta: ')
    if numero_conta in usuarios[cpf]['contas']:
        print('Essa conta já existe')
        return
    usuarios[cpf]['contas'][numero_conta] = {
        'extrato': [],
        'saldo': 0.00,
        'limite_diario': 500.00,
        'limite_saques_diario': 3,
        'numero_saques': 0
    }
    print('Conta criada com sucesso')

def acessar_conta(cpf, numero_conta):
    usuario = filtrar_usuario(cpf)
    if not usuario:
        print('Usuário não encontrado')
        return None
    conta = usuario['contas'].get(numero_conta)
    if not conta:
        print('Conta não encontrada')
        return None
    return conta

def realizar_deposito(conta, valor):
    conta['saldo'] += valor
    conta['extrato'].append(f'R${valor:.2f} foi depositado com sucesso.')
    return f'R${valor:.2f} foi depositado com sucesso.'

def realizar_saque(conta, valor):
    if conta['saldo'] >= valor and conta['numero_saques'] < conta['limite_saques_diario']:
        if valor <= conta['limite_diario']:
            conta['saldo'] -= valor
            conta['numero_saques'] += 1
            conta['extrato'].append(f'Saque no valor de R${valor:.2f} realizado com sucesso.')
            return f'Saque no valor de R${valor:.2f} realizado com sucesso.'
        else:
            return f'O valor máximo para saque é de R$500,00.'
    elif conta['numero_saques'] >= conta['limite_saques_diario']:
        return 'Você já realizou 3 saques diários.'
    elif conta['saldo'] < valor:
        return f'Não é possível realizar o saque. Você está tentando sacar R${valor:.2f}, porém o saldo na conta é de R${conta["saldo"]:.2f}.'

def mostrar_extrato(conta):
    extrato_str = "\n".join(conta['extrato'])
    extrato_str += f'\nSaldo atual: R${conta["saldo"]:.2f}'
    return extrato_str

def menu(conta):
    while True:
        acao = input('''\nEnvie
                    'd' para depósito
                    's' para saque
                    'e' para extrato
                    'q' para sair
                ''').strip().lower()

        if acao == "d":
            valor = float(input('Qual valor para depósito? '))
            print(realizar_deposito(conta, valor))
        elif acao == "s":
            valor = float(input('Qual valor para saque? '))
            print(realizar_saque(conta, valor))
        elif acao == "e":
            print(mostrar_extrato(conta))
        elif acao == 'q':
            break
        else:
            print("Ação inválida. Por favor, envie 'd', 's', 'e' ou 'q'.")

def menu_entrada():
    while True:
        opcao = input('''\nEnvie
                    'criar' para criar um usuário
                    'conta' para criar uma conta
                    'acessar' para acessar sua conta
                    'q' para sair
                ''').strip().lower()

        if opcao == 'criar':
            cpf = criar_usuario()
            if cpf:
                criar_conta(cpf)
        elif opcao == 'conta':
            cpf = input('Digite seu CPF: ')
            criar_conta(cpf)
        elif opcao == 'acessar':
            cpf = input('Digite seu CPF: ')
            numero_conta = input('Digite o número da conta: ')
            conta = acessar_conta(cpf, numero_conta)
            if conta:
                menu(conta)
        elif opcao == 'q':
            break
        else:
            print("Ação inválida. Por favor, envie 'criar', 'conta', 'acessar' ou 'q'.")

def main():
    menu_entrada()

main()
