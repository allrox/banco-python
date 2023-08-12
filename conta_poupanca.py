import datetime


class ContaPoupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()

    # def remuneracaoconta(self):
    #     self.saldo += self.saldo * self.taxaremuneracao
