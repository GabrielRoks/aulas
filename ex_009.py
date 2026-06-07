'''
Exercício 9 — Conversão de Dólar para Real 
Crie um algoritmo que receba um valor em dólar e a cotação atual da moeda, apresentando o valor convertido em reais. 
'''

# var com cotação atual do dolar
cotacao_dolar = 5.04
# var de formula
real_p_dolar = 1 / cotacao_dolar
# pede o valor
valor_converter = float(input("Digite um valor em dólar para converter para real: "))
# converte o valor e imprime 
conversao = print(f'Com a cotação atual de do dolar em R${cotacao_dolar} o valor convertido em reais seria: R${valor_converter / real_p_dolar:.2f}')