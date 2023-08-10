class Cliente:
    def __init__(self, cpf, nome, endereco):
        """
        Inicializa uma nova instância de Cliente
        :param cpf: Documento do Cliente
        :type: str
        :param nome: Nome Completo
        :type: str
        :param endereco: Endereço de residência
        :type: str
        """
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        