menu = """
Escolha uma das seguintes opções:

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Insira o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} efetuado com sucesso.")

    elif opcao == 2:
        valor = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro na operação! Você não tem saldo suficiente.\n")
        elif excedeu_limite:
            print("Erro na operação! O valor inserido excede o limite.\n")
        elif excedeu_saques:
            print("Erro na operação! Limite de saque diário atingido.\n")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")

    elif opcao == 3:
        print("------------- Extrato -------------")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-----------------------------------\n")

    elif opcao == 4:
        print("Encerrando o sistema...")
        break

    else:
        print("Operação inválida! Por favor insira novamente a operação desejada.")
