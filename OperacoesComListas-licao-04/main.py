lista_de_compras = ["Pão", "Água", "Leite", "Ovos"]

'''lista_de_compras[2] = "Suco de laranja"  # Para adicionar um novo ítem, basta atrubuir o valor ao índice corespondnte.'''

lista_de_compras.append("Café")  # Para adicionar um ítem ao final da lista, usa-se a função: append.

'''print(lista_de_compras)
print(lista_de_compras[-1])
print(lista_de_compras[-2])
print(lista_de_compras[-3])
print(lista_de_compras[-4])'''
'''print(lista_de_compras[-5])'''

''' A palavra reservada in, verifica se o ítem está na lista; Retornando True ou False.'''

if "Café" in lista_de_compras:
    print("Preciso comprar café")


''' A função len conta quantos ítens uma determinada lista possui; O len é uma abreviação para length.
    A função len deve receber a lista por parâmetro e ela retornará um inteiro com a quantidade de elementos'''

'''print(len(lista_de_compras))'''

''' Removendo os ítem da posiçao 3 (os ovos) da nossa lista.'''

del lista_de_compras[3]

print(lista_de_compras)

'''Obs:. Agora é importante notar que, a posição 3 não deixará de existir. O que 
acontece de fato, é que todos os ítens que estavam em uma posição maior que a do ítem excluído
são deslocados uma posição para a esquerda.  '''

print(lista_de_compras[3]) # -> Café , que antes estava na posição 4, agora ocupa a posição 3.




