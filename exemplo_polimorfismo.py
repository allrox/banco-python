# Exemplo 1
class Argentina:
    def capital(self):
        print("A capital da Argentina é Buenos Aires.")

    def lingua_oficial(self):
        print("A língua oficial é o espanhol.")


class Brasil:
    def capital(self):
        print("A capital do Brasil é Brasília.")

    def lingua_oficial(self):
        print("A língua oficial é o português.")


obj_argentina = Argentina()
obj_brasil = Brasil()

for pais in (obj_brasil, obj_argentina):
    pais.capital()
    pais.lingua_oficial()


# Exemplo 2
class Veiculo:
    def combustivel(self):
        print("Tipo de combustível utilizado:")


class VeiculoEletrico(Veiculo):
    def combustivel(self):
        super().combustivel()
        print("Este veículo não utiliza combustível fóssil.")


class VeiculoAlcool(Veiculo):
    def combustivel(self):
        super().combustivel()
        print("Este veículo consome álcool.")


# Instanciando veículos a partir das subclasses
carro_eletrico = VeiculoEletrico()
carro_alcool = VeiculoAlcool()

# Utilizando métodos que chamam a superclasse
carro_eletrico.combustivel()
carro_alcool.combustivel()
