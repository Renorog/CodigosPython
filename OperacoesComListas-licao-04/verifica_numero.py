''' Faça um programa que inicialize uma lista com vários números diferentes, depios disso,
   solicite ao usuário um número, virifique se o número está ou não na lista e exiba uma
   mensagem notificando o usuário do resultado. '''

numeros = [12, 32, 45, 65, 78, 98, 14, 25, 36, 47, 58, 69, 13, 27, 39, 29, 40, 63]

numero_usuario = int(input("Digite um número."))
if (numero_usuario in numeros):
    print(f"O número {numero_usuario} está na lista.")
else:
    print(f"O número {numero_usuario} não está na lista.")