import math
'''
Exercício 4 — Fórmula de Bhaskara
Crie um algoritmo que receba os coeficientes A, B e C de uma equação do segundo grau.
Calcule:
O valor de Δ (delta).
As raízes da equação, quando existirem.
'''


while True:
    coeficiente_a = float(input('Digite o coeficiênte A: '))
    coeficiente_b = float(input('Digite o coeficiênte B: '))
    coeficiente_c = float(input('Digite o coeficiênte C: '))

    delta = (coeficiente_b**2) - (4 * coeficiente_a * coeficiente_c)

    if delta < 0:
        print("Não é possível realizar a equação com valor negativo")
        input('Digite "enter" para uma nova tentativa ')
    else:
        raiz = math.sqrt(delta)

        print(f'O valor de delta é: {delta:.2f} e o valor da sua raíz é: {raiz:.2f}')
        continuar = input("Deseja realizar outro calculo? S/N ")

        if continuar == 's' or continuar == 'S':
            continue
        else:
            break