from contas import Conta
from conta_poupanca import ContaPoupanca


class ContaRemuneradaPoupanca(Conta, ContaPoupanca):
    def __init__(self, clientes, numero, saldo, taxaremuneracao):
        # Herança múltipla a partir de Conta e ContaPoupanca
        Conta.__init__(self, clientes, numero, saldo)
        ContaPoupanca.__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao

    def remuneraconta(self):
        self.saldo += self.saldo * (self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao
