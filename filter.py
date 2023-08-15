from functools import reduce

# Exercício 1
print("\n----------- Exercício 1 ------------\n")
# Listas para estudo
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Utiliza filter e função lambda para avaliar
# os itens MOD iguais a 0 na lista (iterável)
pares = filter(lambda item: item % 2 == 0, lista1)

# Utiliza filter e função lambda para avaliar
# os itens MOD diferentes de 0 na lista (iterável)
impares = filter(lambda item: item % 2 != 0, lista2)

print(f"Lista completa >> {lista1}\nLista com filter % 2 == 0 >> {list(pares)}\n")
print(f"Lista completa >> {lista2}\nLista com filter % 2 != 0 >> {list(impares)}")


# Exercício 2
print("\n----------- Exercício 2 ------------")
lista3 = ["Alexandre", "João", "Paulo", "Pedro", "Ana", "Priscilla"]
lista_em_maiusculas = lambda x: str.upper(x)
lista_convertida = sorted(list(map(lista_em_maiusculas, lista3)), reverse=True)

print(f"\nLista com textos convertidos para maiúsculas: {lista_convertida}")


# Exercício 3
# Arredondar os valores apresentados na lista_4 conforme a precisão indicada na lista_5
print("\n----------- Exercício 3 ------------\n")
lista4 = [9.56783, 7.57568, 3.00914, 6.2321]
lista5 = [2, 2, 3, 3]

# A função lambda "personaliza" round() de modo que y representa a precisão do arredondamento.
# Neste caso, o efeito é como 'round(9.56783, 2)' que retorna 9.57
arredondamento = lambda x, y: round(x,y)
lista_arredondada = list(map(arredondamento, lista4, lista5))

print(f"Lista de valores > {lista4}\nLista de precisão > {lista5}")
print(lista_arredondada)


# Exercício 4
# Somar todos os elementos da lista1 utilizando programação funcional
print("\n----------- Exercício 4 ------------\n")
soma = lambda x, y: y + x
resultado_da_soma = reduce(soma, lista1)
print(f"Lista para soma dos elementos > {lista1}")
print(f"Resultado da soma dos elementos > {resultado_da_soma}")