# Importando os módulos para testes
from clientes import Cliente
from contas import Conta

# Criando instâncias de Cliente
cliente1 = Cliente("123", "João", "Rua Xyz")
cliente2 = Cliente("456", "Maria", "Rua Abc")
cliente3 = Cliente("789", "Pedro", "Rua Def")

# Criando instâncias de Conta
conta1 = Conta("João", 1, 1000)
conta2 = Conta("Maria", 2, 0)
conta3 = Conta("Pedro", 3, 0)

# Realizando operações de teste
conta1.depositar(1000)
conta1.sacar(500)
conta1.depositar(2000)
conta1.transferir(conta2, 1900)
conta1.depositar(15000)
conta1.transferir(conta2, 4300)
conta1.sacar(5000)
conta1.transferir(conta3, 5000)
conta2.sacar(3500)
conta3.depositar(18000)
conta3.transferir(conta2, 8000)


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
imprime_extrato(conta2, 2)

Conta.contador_instancias()
