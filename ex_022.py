'''
Exercício 22 — Conversão de Minutos para Horas

Crie um algoritmo que receba uma quantidade de minutos e apresente o equivalente em horas e minutos.

Exemplo:

Entrada: 150 minutos

Saída: 2 horas e 30 minutos
'''
# pede o valor em minutos
minutos = input("Digite um valor em minutos: ")
# atingido caso o valor seja um int positivo
if minutos.isdigit():
    # converte para int
    minutos = int(minutos)
    # cria as formulas
    hora = minutos // 60
    min_rest = minutos % 60
    # imprime os resultados
    print(f'{hora} horas e {min_rest} minutos')
# atingido caso o if seja falso
else:
    print("Digite apenas números inteiros")