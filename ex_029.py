'''
Exercício 29 — Conversão de Quilogramas para Gramas

Crie um algoritmo que receba um peso em quilogramas e apresente o valor correspondente em gramas.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# pede o peso em kg
kg = input("Digite seu peso em quilograma: ")
# atingido caso o valor possa ser convertido em float
if e_float(kg):
    # converte kg para float
    kg = float(kg)
    # cria a formula
    kg_em_grama = kg * 1000
    # imprime o resultado
    print(f'O seu peso convertigo para grama é: {int(kg_em_grama)}g')
# atingido caso o if seja false
else:
    print("Digite apenas números")