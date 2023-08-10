# Neste teste é criada uma classe mãe que contém dois métodos, 'somar' e 'multiplicar'.
# A subclasse 'ClasseFilha' traz outros dois métodos e herda estrutura e métodos da superclasse

class ClasseSomaMultiplicacao:  # Classe mãe ou superclasse
    def __init__(self, a, b):  # Inicializando a classe
        self.a = a
        self.b = b

    def somar(self):
        """
        Método para somar os elementos a e b
        :return: str
        """
        return self.a + self.b

    def multiplicar(self):
        """
        Método para multiplicar os elementos a e b
        :return: str
        """
        return self.a * self.b


class ClasseFilha(ClasseSomaMultiplicacao):  # Classe filha ou subclasse

    def subtrair(self):
        """
        Método para subtrair os elementos a e b, herdados da classe mãe ou superclasse
        :return: str
        """
        return f"{self.a - self.b} \033[31m(calculado pela subclasse)\033[m"

    def dividir(self):
        """
        Método para dividir os elementos a e b, herdados da classe mãe ou superclasse
        :return: str
        """
        return f"{self.a / self.b}  \033[31m(calculado pela subclasse)\033[m"


# Atribuindo a classe filha à variável teste para habilitar métodos próprios e da superclasse
teste = ClasseFilha(20, 10)

print(f"O resultado da soma é: {teste.somar()}")
print(f"O resultado da multiplicação é: {teste.multiplicar()}")
print(f"O resultado da subtração é: {teste.subtrair()}")
print(f"O resultado da divisão é: {teste.dividir()}")
