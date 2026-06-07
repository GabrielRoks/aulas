'''
Exercício 25 — Conversão de Anos para Meses

Crie um algoritmo que receba uma idade em anos e apresente essa idade em meses.
'''
# pede a idade em anos
idade_anos = input("Digite sua idade em anos: ")
# atingido caso a idade pode ser convertida para int
if idade_anos.isdigit():
    # converte a idaede para int
    idade_anos = int(idade_anos)
    # cria a formula
    idade_meses = idade_anos * (365 / 12)
    # imprime o resultado
    print(f'A idade convertida em meses (de 30 dias) é aproximadamente: {int(idade_meses)} meses')
# atingido caso o if seja false
else:
    print('Digite apenas números inteiros')