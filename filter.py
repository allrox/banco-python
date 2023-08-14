# Listas para estudo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Utiliza filter e função lambda para avaliar
# os itens MOD iguais a 0 na lista (iterável)
nova_lista = filter(lambda item: item % 2 == 0, lista)

# Utiliza filter e função lambda para avaliar
# os itens MOD diferentes de 0 na lista (iterável)
nova_lista_2 = filter(lambda item: item % 2 != 0, lista_2)

print(f"Lista completa >> {lista}\nLista com filter % 2 == 0 >> {list(nova_lista)}\n")
print(f"Lista completa >> {lista_2}\nLista com filter % 2 != 0 >> {list(nova_lista_2)}")
