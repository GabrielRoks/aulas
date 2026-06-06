'''
Exercícios com Estrutura WHILE 
Exercício 1 — Tabuada com WHILE
Crie um algoritmo que receba um número inteiro.
Utilize um laço WHILE para apresentar sua tabuada de 1 até 10.
'''

i = 1
multiplicador = int(input("Digite a tabuda que você que (Ex: 5): "))

while i <= 10:
    calculo = multiplicador * i
    if multiplicador <= 0 or multiplicador > 10:
        print("Infelizmente só posso fazer contas da tabuáda do 1 ao 10")
        break
    else:
        print(f'{multiplicador} x {i} = {calculo}')
    i += 1