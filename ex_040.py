'''
Exercício 40 — Cálculo do IMC

Crie um algoritmo que receba:

peso (kg);

altura (m).
Apresente o Índice de Massa Corporal (IMC).
'''

# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
kg = input("Digite seu peso em kg: ")
altura = input("Digite sua altura em m: ")

if e_float(kg) and e_float(altura):
    kg = float(kg)
    altura = float(altura)
    imc = kg / (altura**2)
    print(f'Seu imc é: {imc:.2f}')
# atingifo caso o if seja falso
else:
    print("Digite apenas numeros")