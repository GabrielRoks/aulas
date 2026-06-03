'''
Exercício 9 — Valor Maior que 3

Crie um algoritmo que receba um número.
Se o valor for maior que 3, apresente-o.
Caso contrário, não apresente nada.

'''

while True:
    numero = float(input("Digite algum número: "))
    if numero > 3:
        print(numero)
        break
    else:
        print(' ')
        break