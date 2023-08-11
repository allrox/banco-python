def somar(x, y, z=0):
    """
    Método que soma três parâmetros
    :param x: int
    :param y: int
    :param z: int
    :return: int
    """
    return x + y + z


# Neste exemplo o último parâmetro do método não é informado, contudo ele é executado
print(f"Soma dos parâmetros x e y: ", somar(20, 30))

# Neste exemplo o último parâmetro do método é informado e a operação considera três valores
print(f"Soma dos parâmetros x, y, e z: ", somar(20, 30, 50))
