''' Faça um programa que solicite o nome do usuário e depois disso
faça uma saldação do formato: "Olá {nome digitado pelo usuário}" '''

'''      usando format      '''
nome = input("Digite seu nome.\n")
print("Olá {0}".format(nome))

'''    usando interpolação  '''
print(f"Olá {nome}")
