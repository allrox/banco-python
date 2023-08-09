import datetime
from extratos import Extrato


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.__saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    # Deposita um valor numa CONTA
    def depositar(self, valor):
        self.__saldo += valor
        # Utiliza '.append' para incluir a operação na array TRANSACOES
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])
        return f"Depósito de {valor} realizado."

    # Saca um valor de uma CONTA
    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            # Utiliza '.append' para incluir a operação na array TRANSACOES
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return f"Saque de {valor} realizado."

    # Transfere um valor da conta atual para a CONTA_DESTINO
    def transferir(self, conta_destino, valor):
        if self.__saldo < valor:
            return "Não existe saldo suficiente"
        else:
            conta_destino.depositar(valor)
            self.__saldo -= valor
            # Utiliza '.append' para incluir a operação na array TRANSACOES
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"

    # Exibe o saldo
    def ver_saldo(self):
        print(f"\nConta Número: {self.numero} -----------------------------------------------"
              f"\nSaldo: {self.__saldo}")
