''' Faça um algoritmo que solicite o ano que o usuário nasceu,
depois disso, faça o programa descrever se o usuário fará ou já fez
18 anos neste ano. '''

ano_atual = 2022
ano_nascimento = int(input("Digite o ano que você nasceu: "))
resultado = ano_atual - ano_nascimento

if(resultado == 18):
    print("Você fez 18 anos, neste ano!\n")
    print("Parabéns!")
elif(resultado < 18):
    print("Você ainda não fez 18 anos!\n")
    print("Você tem: ", resultado, " anos!")
else:
    print("Você já é maior de 18 anos!\n")
    print("Você tem : ", resultado, " anos!")

