'''
Exercício 30 — Total de Segundos

Crie um algoritmo que receba:

horas;

minutos;

segundos.
Apresente o total de segundos correspondente.
'''
# Pedem os valores de horas, minutos e sehundos
horas = input('Digite as horas: ')
minutos = input("Digite os minutos: ")
segundos = input("Digite os segundos: ")
# aatingido caso os valores podem ser convertidos para int
if horas.isdigit() and minutos.isdigit() and segundos.isdigit():
    # Converte os valores para int
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    # cria a formula
    conversor = (horas * 3600) + (minutos * 60) + segundos
    # imprime o resultado
    print(f'O total de segundos foi: {conversor}')
# atingido caso o if seja falso
else:
    print("Digite apenas números inteiros: ")