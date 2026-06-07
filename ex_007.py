'''
Exercício 7 — Troca de Valores 
Crie um algoritmo que leia dois valores inteiros e troque os valores entre as variáveis. 
'''

# pede o primeiro valor
var_A = input("Digite algum valor para variável A: ")
# pede o segundo valor
var_B = input("Digite outro valor para a variável B: ")
# faz a troca
var_A, var_B = var_B, var_A
# imprime o resultado
print(f'as variáveis trocadas ficaram com A: {var_A} e B: {var_B}')