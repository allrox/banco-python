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

    def decoration(metodo):
        """
        Função decoradora, construída para modificar ou estender o comportamentode outras
        funções ou métodos. Neste caso, recebe um método e imprime linhas pontilhadas antes e depois
        do seu retorno.
        :param metodo: Método a ser decorado
        :return: str
        """

        # *args e **kwargs são mecanismos que preparam a função para receber um número
        # variável de argumentos de qualquer tipo da função que está sendo decorada.
        #
        # O asterisco passa uma lista de argumentos posicionais variáveis para uma função,
        # desempacota os argumentos passados e os torna acessíveis como uma tupla dentro da função.
        #
        # O asterisco duplo desempacota os argumentos nomeados passados e os torna acessíveis
        # como um dicionário dentro da função
        def wrapper(*args, **kwargs):
            print(f"---------------------------------------------------------------")
            resultado = metodo(*args, **kwargs)
            print(f"---------------------------------------------------------------")
            return resultado
        return wrapper

    @staticmethod
    def contador_instancias():
        print(f"\n\033[31mO objeto Conta possui {Conta.contador_contas} instâncias.\033[m")

    def depositar(self, valor):
        """
        Deposita um valor na conta.
        :param valor: A quantia a ser depositada na conta.
        :type valor: float
        :return: Mensagem indicando o sucesso da operação.
        :rtype: str
        """
        try:
            self.__saldo += valor
            # Utiliza '.append' para incluir a operação na array TRANSACOES
            self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])
            return f"Depósito de {valor} realizado."
        except TypeError:
            print("Utilize valor numérico e . para separar as casas decimais")

    def sacar(self, valor):
        """
        Saca um valor da conta.
        :param valor: A quantia a ser sacada da conta.
        :type valor: float
        :return: Mensagem indicando o sucesso da operação ou False se não houver saldo suficiente.
        :rtype: Union[str, bool]
        """
        try:
            if self.__saldo < valor:
                return False
            else:
                self.__saldo -= valor
                # Utiliza '.append' para incluir a operação na array TRANSACOES
                self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
                return f"Saque de {valor} realizado."
        except TypeError:
            print("Utilize valor numérico e . para separar as casas decimais")

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
        try:
            if self.__saldo < valor:
                return "Não existe saldo suficiente"
            else:
                conta_destino.depositar(valor)
                self.__saldo -= valor
                # Utiliza '.append' para incluir a operação na array TRANSACOES
                self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
                return "Transferencia Realizada"
        except TypeError:
            print("Utilize valor numérico e . para separar as casas decimais")

    @decoration
    def ver_saldo(self):
        """
        Exibe o saldo relacionado à conta
        """
        print(f"Conta Número: {self.numero}\nSaldo: R$ {self.__saldo:.2f}")
