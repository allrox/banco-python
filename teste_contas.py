# Importando os módulos para testes
from clientes import Cliente
from contas import Conta
from conta_remunerada import ContaRemuneradaPoupanca
from conta_especial import ContaEspecial


# Criando instâncias de Cliente
cliente1 = Cliente("123", "João", "Rua Xyz")
cliente2 = Cliente("456", "Maria", "Rua Abc")
cliente3 = Cliente("789", "Pedro", "Rua Def")
cliente4 = Cliente("012", "Alexandre", "Rua Ghi")
cliente5 = Cliente("013", "Ana", "Rua Jkl")
cliente6 = Cliente("654", "Cristina", 1500)

# Criando instâncias de Conta
conta1 = Conta("João", 1, 1000)
conta2 = Conta("Maria", 2, 0)
conta3 = Conta("Pedro", 3, 0)
conta5 = Conta("Ana", 5, 0)

# Criando instância da ContaEspecial estruturada com limite de cheque especial
conta4 = ContaEspecial("Alexandre", 4, 0, 5000)

# Criando instância da ContaRemuneradaPoupanca que remunera o correntista com juros sobre o saldo
conta6 = ContaRemuneradaPoupanca("Cristina", 6, 1500, .06)

# Realizando operações de teste
conta1.depositar(150000)
conta1.sacar(eval("30,5"))  # Indução ao tratamento de exceções
conta1.depositar(2000)
conta1.transferir(conta2, 75000)
conta1.depositar(15000)
conta1.transferir(conta2, 4300)
conta1.sacar("5000")  # Indução ao tratamento de exceções
conta1.transferir(conta3, 5000)
conta2.sacar(3500)
conta3.depositar(18000)
conta3.transferir(conta2, 8000)
conta4.depositar(45000)
conta4.sacar(50000)
conta5.sacar(600)  # Indução ao aviso de saldo insuficiente
conta5.depositar(3200)
conta5.transferir(conta6, 3000)


# Função para exibir a geração do extrato com o saldo
def imprime_extrato(x, y):
    """
    Imprime o extrato para a conta e número informados no input
    :param x: Conta desejada
    :type x: extrato
    :param y: Número da conta desejada
    :type y: int
    :return: str
    """
    x.extrato.gerar_extrato(y)
    x.ver_saldo()


# Gerando o extrato das transações
imprime_extrato(conta1, 1)

imprime_extrato(conta2, 2)

imprime_extrato(conta4, 4)

imprime_extrato(conta5, 5)

Conta.contador_instancias()

print("\n\nImprimindo extrato da conta 6 antes da remuneração")
imprime_extrato(conta6, 6)

print("\nImprimindo extrato da conta 6 após a remuneração da poupança")

imprime_extrato(conta6, 6)
