from time import sleep
import os

LIMITE_SAQUES_POR_DIA = 3
LIMITE_SAQUE = 500
saldo = 0
saques = 0
lista_de_saques = []
lista_de_depositos = []
lista_de_operacao_realizada_saque_ou_deposito = [] # 1 = saque, 2 = deposito

# Função para realizar um depósito
def deposito(valor):
    global saldo
    saldo += valor
    lista_de_depositos.append(valor)
    lista_de_operacao_realizada_saque_ou_deposito.append(2)
    print(f"Deposito de R$ {valor.__format__('0.2f')} realizado com sucesso!")
    voltar_menu()

# Função para realizar um saque
def saque(valor):
    global saldo
    global saques

    if saques >= LIMITE_SAQUES_POR_DIA:
        print("Limite de saques por dia atingido!")
        voltar_menu()
        return
    elif valor > LIMITE_SAQUE:
        print(f"Valor de saque superior ao limite de R$ {LIMITE_SAQUE.__format__('0.2f')}")
        voltar_menu()
        return
    elif saldo < valor:
        print("Saldo insuficiente!")
        voltar_menu()
        return

    saldo -= valor
    saques += 1
    lista_de_saques.append(valor)
    lista_de_operacao_realizada_saque_ou_deposito.append(1)
    print(f"Saque de R$ {valor.__format__('0.2f')} realizado com sucesso!")

    voltar_menu()

# Função para exibir o extrato bancário
def extrato():
    lista_de_operacao_realizada_saque_ou_deposito_copia = lista_de_operacao_realizada_saque_ou_deposito.copy()
    lista_de_saques_copia = lista_de_saques.copy()
    lista_de_depositos_copia = lista_de_depositos.copy()
    indice_saques = 0
    indice_depositos = 0

    clear()
    print("Extrato bancário")
    print()
    print("Operações realizadas:")
    print()

    for operacao_realizada in lista_de_operacao_realizada_saque_ou_deposito_copia:
        if operacao_realizada == 1:
            print(f"- R$ {lista_de_saques_copia[indice_saques].__format__('0.2f')}")
            indice_saques += 1
        elif operacao_realizada == 2:
            print(f"+ R$ {lista_de_depositos_copia[indice_depositos].__format__('0.2f')}")
            indice_depositos += 1

    print()
    print(f"Saldo atual: R$ {saldo.__format__('0.2f')}")
    print()
    voltar_menu()

# Função para exibir o menu
def menu():
    print(f"""  Bem vindo ao Sistema Bancário em Python!
    
    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Sair
    
    """)

# Função para limpar a tela
def clear():
    os.system('cls||echo -e \\\\033c')

# Função para voltar ao menu
def voltar_menu():
    print()
    input("Pressione ENTER para voltar ao menu...")

# Loop principal
while True:
    clear()
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        print()
        valor_deposito = float(input("Digite o valor do deposito: R$ "))
        print()
        deposito(valor_deposito)
    elif opcao == '2':
        print()
        valor_saque = float(input("Digite o valor do saque: R$ "))
        print()
        saque(valor_saque)
    elif opcao == '3':
        extrato()
    elif opcao == '4':
        print("Saindo do sistema...")
        sleep(2)
        break
    else:
        print()
        print("Opção inválida!")
        voltar_menu()