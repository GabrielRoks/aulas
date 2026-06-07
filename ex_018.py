'''
Exercício 18 — Conversão de Metros para Centímetros

Crie um algoritmo que receba uma medida em metros e apresente o valor correspondente em centímetros.
'''
# PEde o valor em metros
metro = input("Digite uma media em metros: ")
# Cria uma função para validar se um valor digitado pode ser float
def numero_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# Atingido caso possar ser convertido para float
if numero_float(metro):
    # converte para float
    metro_float = float(metro)
    # cria a formula
    conversor = metro_float * 100
    # imprime
    print(f'O valor digitado convertido para centímetros é igual a: {conversor:.2f}Cm')
# Atingido caso o if seja false
else:
    print('Digite apenas números')