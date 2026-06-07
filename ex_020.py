'''
Exercício 20 — Cálculo do Perímetro de um Retângulo

Crie um algoritmo que receba a largura e o comprimento de um retângulo e apresente seu perímetro.
'''
# pede os dados largura e comprimento
largura = input("Digite a largura do retângulo em Cm: ")
comprimento = input("Digite o comprimento do retângulo em Cm: ")
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# atingido caso os dados possam ser convertidos para float
if e_float(largura) and e_float(comprimento):
    # converte os dados
    largura = float(largura)
    comprimento = float(comprimento)
    # cria a formula
    perimetro = 2 * (largura + comprimento)
    # imprime o resultado
    print(f'O perímetro do retângulo é: {perimetro}Cm')
# atingido caso o if seja false
else:
    print("Favor digitar apenas números")