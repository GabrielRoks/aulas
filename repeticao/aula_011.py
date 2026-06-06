'''
Exercício 1 — Tabuada com FOR
Crie um algoritmo que receba um número inteiro.
Utilize um laço FOR para apresentar sua tabuada de 1 até 10.
'''

multiplicador = int(input("Digite a tabuda que você que (Ex: 5): "))

for i in range(1, 11):
    calculo = multiplicador * i
    if multiplicador <= 0 or multiplicador > 10:
        print("Infelizmente só posso fazer contas da tabuáda do 1 ao 10")
        break
    else:
        print(f'{multiplicador} x {i} = {calculo}')
    i += 1