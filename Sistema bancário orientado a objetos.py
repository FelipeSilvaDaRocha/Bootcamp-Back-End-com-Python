import textwrap
from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adcionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf


class Conta:
    def __init__(self, numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(cliente, numero)

    def sacar(self, valor: float):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Erro na operação! Você não tem saldo suficiente.\n")
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
            return True

        else:
            print("A operação falhou! Digite o valor corretamente.")
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de R$ {valor:.2f} efetuado com sucesso.")
            return True

        else:
            print("A operação falhou! Digite o valor corretamente.")

        return False


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor: float):
        limite = self.limite
        limite_saques = self.limite_saques

        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"]])

        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

        if excedeu_limite:
            print("Erro na operação! O valor inserido excede o limite.\n")

        elif excedeu_saques:
            print("Erro na operação! Limite de saque diário atingido.\n")

        else:
            return super().sacar(valor)

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao, ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_trasacao = conta.depositar(self.valor)

        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao, ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def filtrar_clientes(cpf, clientes):
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None


def recuperar_conta(cliente):
    if not cliente.conta:
        print("O cliente não possui conta!")
        return

    return cliente.conta[0]


def depositar(clientes):
    cpf = input("Digite o CPF do cliente que deseja depositar: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = input("Insira o valor que deseja depositar: ")
    transacao = Deposito(valor)

    conta = recuperar_conta(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def menu():
    menu_option = """
        ============== MENU =============
        Escolha uma das seguintes opções:
            [1] - Depositar
            [2] - Sacar
            [3] - Extrato
            [4] - Cadastrar usuário
            [5] - Criar conta
            [6] - Listar contas
            [7] - sair
        =>"""

    return input(textwrap.dedent(menu_option))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)
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
