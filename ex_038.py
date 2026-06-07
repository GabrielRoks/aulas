'''
Exercício 38 — Conversão de Dias para Semanas

Crie um algoritmo que receba uma quantidade de dias e apresente o equivalente em semanas e dias restantes.
'''

# pede o valor em dias
dias = input("Digite um valor em dias: ")
# atingido caso o valor seja um int positivo
if dias.isdigit():
    # converte para int
    dias = int(dias)
    # cria as formulas
    semana = dias // 7
    dias_rest = dias % 7
    # imprime os resultados
    print(f'{semana} semana e {dias_rest} dias')
# atingido caso o if seja falso
else:
    print("Digite apenas números inteiros")