''' Faça um programa que solicite a idade do usuário, verifique se o texto
informado só contém números. Caso tenha somente números exiba a mensagem: "Você
tem {idade digitada} anos.", caso contrário exiba a mensagem: "Você digitou uma
idade inválida". '''

idade = input("Digite sua idade.\n")
idade_valida = idade.isdigit()

if(idade_valida):
    print(f"Você tem {idade} anos")
else:
    print("Você digitou uma idade inválida.")
