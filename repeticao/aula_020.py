'''
Exercício 6 — Contagem Regressiva
Crie um algoritmo que receba um número inteiro positivo.
Utilize WHILE para realizar uma contagem regressiva até zero.
'''

numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    while True:
        if numero < 0:
            break
        else: 
            print(numero)
            numero -= 1
else:
    print("Digite apenas números inteiros")