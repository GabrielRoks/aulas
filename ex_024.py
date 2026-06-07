'''
Exercício 24 — Área de um Triângulo

Crie um algoritmo que receba a base e a altura de um triângulo e apresente sua área.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# pede os dados
base = input("Digite a base do triângulo em Cm: ")
altura = input("Digite a altura do triângulo em Cm: ")
# atingido caso os valores podem ser convertidos para float
if e_float(base) and e_float(altura):
    # converte  os valors
    base = float(base)
    altura = float(altura)
    # cria a formula
    area = (base * altura) / 2
    # imprime o resultado
    print(f'A area do triângulo é: {area:.2f}Cm')
# atingido caso o if seja false
else:
    print("Digite apenas números")