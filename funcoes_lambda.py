def imc(altura, peso):
    """
    Método que calcula o IMC utilizando uma função anônima ou 'Função Lambda',
    o que pode ser útil quando é necessária uma pequena função anônima aplicada
    em um contexto limitado. É apenas um exemplo de como uma operação pode ser realizada
    sem a necessidade da criação de uma função nomeada
    :param altura: int
    :param peso: int
    :return: float
    """
    imc = lambda x, y: y / (x ** 2)
    return print(f"O IMC do indivíduo com {altura} de altura e {peso} quilos é {round(imc(altura, peso), 2)}")


def media(n1, n2, n3, n4):
    resultado_media = lambda x, y, z, w: (x + y + z + w) / 4
    return print(f"A média dos números {n1}, {n2}, {n3}, {n4} é {round(resultado_media(n1, n2, n3, n4), 2)}")


imc(1.7, 67)
print("---------------------------------------------------------------")
media(8, 0, 10, 9)
