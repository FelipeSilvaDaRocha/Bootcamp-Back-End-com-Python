def depositar(saldo, valor, extrato):
    # Retorno sugerido: saldo e extrato
    saldo += valor
    print(f"\nDepósito de R$ {valor:.2f} efetuado com sucesso.")
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return extrato, saldo


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    # Retorno sugerido: saldo e extrato
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
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
    return extrato, saldo, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    # Retorno sugerido: extrato
    print("------------- Extrato -------------")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("-----------------------------------\n")


def cadastrar_usuario(usuarios):
    nome = input("Insira o nome do novo usuário: ").strip()
    data_nascimento = input(f"Qual a data de nascimento do(a) {nome}: ")
    cpf = input(f"Insira o CPF de {nome}: ").strip().replace(".", "").replace("-", "")
    endereco = input(f"Insira o endereco de {nome}: ")

    existe_usuario = consultar_cpf(cpf, usuarios)
    if existe_usuario:
        print("Já existe usuário cadastrado com este CPF.")

    else:
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário cadastrado com sucesso!\n")


def consultar_cpf(cpf, usuarios):
    usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario[0] if usuario else None


def criar_conta(AGENCIA, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF para criar a conta: ").strip().replace(".", "").replace("-", "")

    usuario = consultar_cpf(cpf, usuarios)
    if usuario:
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
        print("Conta criada com sucesso!")

        return len(contas) + 1

    else:
        print("Não existe usuário cadastrado com esse CPF.")


def listar_contas(contas):
    print("======= Contas registradas ======")
    for conta in contas:
        exibir = f"""
        Agência: {conta["agencia"]}
        Conta corrente: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]} """
        print(exibir)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 1
    usuarios = []
    contas = []

    menu = """
    Escolha uma das seguintes opções:
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Cadastrar usuário
        [5] - Criar conta
        [6] - Listar contas
        [7] - sair
    =>"""

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            valor = float(input("Insira o valor do depósito: "))
            extrato, saldo = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Insira o valor que deseja sacar: "))
            extrato, saldo, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                                  limite=limite, numero_saques=numero_saques,
                                                  LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            cadastrar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print("Encerrando o sistema...")
            break

        else:
            print("Operação inválida! Por favor insira novamente a operação desejada.")


# Inicialização do programa
main()
