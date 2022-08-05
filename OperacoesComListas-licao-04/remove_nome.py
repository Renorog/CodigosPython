''' Faça um programa que inicialize uma lista vazia e a preencha com 5 nomes diferentes
digitados pelo usuário, depois disso solicite um número de 0 até 4  e remova o elemento desta posição. '''

nome_pessoas = []
nome_pessoas.append(input("Digite o primeiro nome."))
nome_pessoas.append(input("Digite o segundo nome."))
nome_pessoas.append(input("Digite o terceiro nome."))
nome_pessoas.append(input("Digite o quarto nome."))
nome_pessoas.append(input("Digite o quinto nome."))

remove_numero = int(input("Escolha uma posição de 0 até 4 para excluir da lista: "))
del nome_pessoas[remove_numero]

print(nome_pessoas)