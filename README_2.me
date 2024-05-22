# Sistema Bancário Simples

Este é um sistema bancário simples implementado em Python. Ele permite a criação de usuários e contas, além de realizar operações bancárias básicas, como depósitos, saques e exibição de extratos.

## Funcionalidades

- **Criar Usuário:** Permite criar um novo usuário no sistema.
- **Criar Conta:** Permite criar uma nova conta para um usuário existente.
- **Acessar Conta:** Permite acessar uma conta existente para realizar operações bancárias.
- **Depósito:** Permite realizar depósitos em uma conta.
- **Saque:** Permite realizar saques de uma conta, respeitando limites diários.
- **Extrato:** Exibe o extrato de uma conta, incluindo todas as transações e o saldo atual.

## Estrutura do Código

O código está organizado em funções para realizar diferentes operações:

- **criar_usuario:** Solicita os dados do usuário e cria um novo usuário no sistema.
- **criar_conta:** Solicita o número da conta e cria uma nova conta associada a um usuário.
- **acessar_conta:** Permite acessar uma conta existente para realizar operações bancárias.
- **realizar_deposito:** Realiza um depósito em uma conta.
- **realizar_saque:** Realiza um saque de uma conta, respeitando limites diários.
- **mostrar_extrato:** Exibe o extrato de uma conta.
- **menu:** Apresenta o menu de operações bancárias (depósito, saque, extrato).
- **menu_entrada:** Apresenta o menu inicial (criar usuário, criar conta, acessar conta).
- **main:** Função principal que inicia o sistema bancário.

## Como Usar

1. **Executar o Sistema:**
   Execute o script Python para iniciar o sistema bancário.

2. **Menu Inicial:**
   No menu inicial, você tem as seguintes opções:
   - Digite `'criar'` para criar um novo usuário.
   - Digite `'conta'` para criar uma nova conta para um usuário existente.
   - Digite `'acessar'` para acessar uma conta existente.
   - Digite `'q'` para sair do sistema.

3. **Criar Usuário:**
   Se você escolher `'criar'`, será solicitado a fornecer os dados do usuário (CPF, nome, data de nascimento, endereço). Se o usuário for criado com sucesso, você pode então criar uma conta para este usuário.

4. **Criar Conta:**
   Se você escolher `'conta'`, será solicitado a fornecer o CPF do usuário e o número da conta. A conta será criada e associada ao usuário.

5. **Acessar Conta:**
   Se você escolher `'acessar'`, será solicitado a fornecer o CPF do usuário e o número da conta. Se a conta for encontrada, você entrará no menu de operações bancárias.

6. **Operações Bancárias:**
   No menu de operações bancárias, você pode:
   - Digitar `'d'` para realizar um depósito.
   - Digitar `'s'` para realizar um saque.
   - Digitar `'e'` para exibir o extrato.
   - Digitar `'q'` para sair do menu de operações bancárias.

## Código

```python
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
```
