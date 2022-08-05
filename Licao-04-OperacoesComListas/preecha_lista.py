''' Faça um programa que inicialize uma lista vazia e solicite ao usuário 3 nomes de cidades,
um por vez, cada vez que o usuário digitar um nome, o programa deve incluir esse nome na lista de
cidades. '''

nome_cidades = []
'''cidade1 = input("Informe a primeira cidade: ")
nome_cidades.append(cidade1)
cidade2 = input("Informe a segunda cidade: ") 
nome_cidades.append(cidade2)
cidade3 = input("Informe a terceira cidade: ")
nome_cidades.append(cidade3)'''

'''   outra maneira de fazer com menos linhas de código.  '''

cidade = input("Informe o nome da primeira cidade: ")
nome_cidades.append(cidade)
nome_cidades.append((input("Informe o nome da segunda cidade: ")))
nome_cidades.append((input("Informe o nome da terceira cidade: ")))

print(nome_cidades)