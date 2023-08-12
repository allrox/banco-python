# Programação funcional
# A função multiplicar_por é uma função de ordem superior, que traz função multi aninhada
# Neste caso é necessário chamar a função pai duas vezes para que, na segunda passagem,
# o parâmetro seja passado à função filha.
def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi


def main():
    # Criando uma instância
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

    # Criando uma instância
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))


if __name__ == "__main__":
    main()
