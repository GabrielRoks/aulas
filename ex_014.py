'''
Exercício 14 — Área da Circunferência 
Crie um algoritmo que receba o raio de uma circunferência e apresente sua área. 
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# Pede o valor do raio
raio = input("Digite o raio da circunferência: ")
# Operação de condição, é atingida se o valor digitado pode se tornar float
if e_float(raio):
    # define raio como float
    raio = float(raio)
    # define a operação
    area = 3.14 * (raio**2)
    # imprime o resultado
    print(f"A area do circulo foi: {area}")
# É atingido caso o valor inserido não pode ser covertido para float
else:
    print("Digite apenas números")