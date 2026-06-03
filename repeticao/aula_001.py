'''
Exercício 1 — Número Positivo para Negativo

Crie um algoritmo que receba um número inteiro.
Se o número for maior que zero, transforme-o em negativo.
Caso contrário, apresente o próprio valor.
'''
while True:
    numero = input('Digite um número: ')

    if numero.isdigit():
        numero = int(numero)
        if numero > 0:
            print(f'O seu número convertido para negativo é: {numero * (-1)}')
            break
        else:
            print(numero)
            break
    else:
        print('O nuúmero precisa ser um inteiro, tente novamente')
        input('pressione "enter" para uma nova tentativa ') 