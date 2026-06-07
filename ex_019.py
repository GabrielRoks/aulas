'''
Exercício 19 — Idade em Dias

Crie um algoritmo que receba a idade de uma pessoa em anos e apresente aproximadamente quantos dias ela viveu.

Considere:

1 ano = 365 dias.
'''
# pede a idade em anos
idade_anos = input("Digite sua idade em anos: ")
# atingido caso a idade possa ser convertida para um int positivo
if idade_anos.isdigit():
    # converte para int
    idade_anos = int(idade_anos)
    # cria a formula
    idade_dias = idade_anos * 365
    # imprime o resultado
    print(f'Sua idade convertida em dias vividos é aproximadamente: {idade_dias} dias')
# atingido caso o if seja false
else:
    print("Por favor digite apenas número inteiros")