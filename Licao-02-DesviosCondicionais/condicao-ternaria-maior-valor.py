''' Faça um programa que solicite ao usuário 2 valores, utlize uma condição
ternária para escrever o maior valor: o primeiro ou o segundo (caso os valores
sejam iguais, considere o segundo). '''
primeiro_valor = int(input("Digite um valor: \n"))
segundo_valor = int(input("Digite um valor: \n"))

print("Primeiro valor é maior." if primeiro_valor > segundo_valor else "Segundo valor é maior." )