class Extrato:
    def __init__(self):
        self.transacoes = []

    def gerar_extrato(self, numeroconta):
        # Linha de cabeçalho
        print(f"\nExtrato da Conta Nº {numeroconta} "
              f"\n---------------------------------------------------------------")

        # Laço que imprime os dados armazenadas na array TRANSAÇÕES
        for p in self.transacoes:
            # p[x] representa o índice na lista // 15: indica que o valor deve ser formatado como uma STRING
            # com pelo menos 15 caracteres // 15.2f indica que o valor deve ser formatado como ponto flutuante
            # utilizando 2 casas decimais // stsftime (string format time) especifica a saída de data e hora.
            print(f"{p[0]:15s} {p[1]:15.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y   %H:%M:%S')}")
