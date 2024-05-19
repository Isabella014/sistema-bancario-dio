# Sistema Bancário Simples

Este projeto consiste em um sistema bancário simples em Python que permite ao usuário realizar depósitos, saques e visualizar um extrato bancário. O sistema possui limites diários para saques e um valor máximo por saque.

## Funcionalidades

- **Depósito**: Permite ao usuário depositar um valor na conta.
- **Saque**: Permite ao usuário sacar um valor da conta, com as seguintes restrições:
  - Limite máximo de 3 saques diários.
  - Limite máximo de R$500,00 por saque.
  - Verificação de saldo disponível antes de permitir o saque.
- **Extrato**: Exibe todos os depósitos e saques realizados, além do saldo atual.

## Requisitos

- Python 3.x

## Como usar

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/Isabella014/sistema-bancario-dio/
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd sistema-bancario
    ```

3. Execute o script:
    ```sh
    sistema-bancario.py
    ```

## Exemplo de uso

Ao executar o script, você verá o seguinte menu:

```
Envie
d para deposito
s para saque
e para extrato
q para sair`
```

- Para realizar um depósito, envie `d` e insira o valor do depósito.
- Para realizar um saque, envie `s`, insira o valor do saque e siga as instruções.
- Para visualizar o extrato, envie `e`.
- Para sair do programa, envie `q`.

### Exemplo de sessão
```
Envie
d para deposito
s para saque
e para extrato
q para sair
d
Qual valor para deposito? 1000
R$1000 foi depositado com sucesso.
Envie
d para deposito
s para saque
e para extrato
q para sair
s
Qual valor para saque? 300
Saque no valor de R$300 realizado com sucesso
Envie
d para deposito
s para saque
e para extrato
q para sair
e
'R$1000 foi depositado com sucesso.
Saque no valor de R$300 realizado com sucesso
Saldo atual: R$700'
Envie
d para deposito
s para saque
e para extrato
q para sair
q
```

