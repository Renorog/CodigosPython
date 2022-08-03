''' Faça um programa que solicite o nome completo do usuário e exiba
somente o seu segundo nome/primeiro sobrenome.'''

nome = input("Digite seu nome completo.")
segundo_nome = nome.split()
print(segundo_nome[1])