'''
Exercício 33 — Conversão de Real para Dólar

Crie um algoritmo que receba:

valor em reais;

cotação do dólar.
Apresente o valor convertido para dólares.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# var com cotação atual do dolar
cotacao_dolar = input("Digite a cotação do dolar: ")
real = input("Digite o valor em real que deja converter: ")
# caso o valor seja float
if e_float(cotacao_dolar) and e_float(real):
    cotacao_dolar = float(cotacao_dolar)
    real = float(real)
    # var de formula
    real_p_dolar = real / cotacao_dolar
    print(f'O valor convertido para dolar é: {real_p_dolar:.2f}')
# aatingido quando o if é falsp
else:
    print("Digite apenas numeros")