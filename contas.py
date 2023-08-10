import datetime
from extratos import Extrato


class Conta:

    contador_contas = 0
    lista_contas = []

    def __init__(self, clientes, numero, saldo):
        """
        Inicializa uma nova instância de Conta.
        :param clientes: Lista de clientes associados à conta.
        :type clientes: str
        :param numero: Número da conta.
        :type numero: int
        :param saldo: Saldo inicial da conta.
        :type saldo: float
        """
        self.clientes = clientes
        self.numero = numero
        self.__saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
        Conta.lista_contas.append(self)
        Conta.contador_contas += 1

    def depositar(self, valor):
        """
        Deposita um valor na conta.
        :param valor: A quantia a ser depositada na conta.
        :type valor: float
        :return: Mensagem indicando o sucesso da operação.
        :rtype: str
        """
        self.__saldo += valor
        # Utiliza '.append' para incluir a operação na array TRANSACOES
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])
        return f"Depósito de {valor} realizado."

    def sacar(self, valor):
        """
        Saca um valor da conta.
        :param valor: A quantia a ser sacada da conta.
        :type valor: float
        :return: Mensagem indicando o sucesso da operação ou False se não houver saldo suficiente.
        :rtype: Union[str, bool]
        """
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            # Utiliza '.append' para incluir a operação na array TRANSACOES
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return f"Saque de {valor} realizado."

    def transferir(self, conta_destino, valor):
        """
        Transfere um valor para outra conta.
        :param conta_destino: Conta de destino para a transferência.
        :type conta_destino: Conta
        :param valor: A quantia a ser transferida.
        :type valor: float
        :return: Mensagem indicando o sucesso da operação ou aviso de saldo insuficiente.
        :rtype: str
        """
        if self.__saldo < valor:
            return "Não existe saldo suficiente"
        else:
            conta_destino.depositar(valor)
            self.__saldo -= valor
            # Utiliza '.append' para incluir a operação na array TRANSACOES
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"

    def ver_saldo(self):
        """
        Exibe o saldo relacionado à conta
        """
        print(f"\nConta Número: {self.numero} -----------------------------------------------"
              f"\nSaldo: R$ {self.__saldo:.2f}")
