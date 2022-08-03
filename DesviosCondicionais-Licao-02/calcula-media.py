''' Faça um algoritmo que solicite 3 notas para o usuário,calcule
a média e indique se o aluno foi aprovado ou reprovado ( nota
precisa ser maior ou igual a sete para o aluno ser aprovado).'''

nota1 = int(input("Digite a preimeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3 ) / 3

if(media >= 7):
    print("Aprovado!")
else:
    print("Reprovado!")