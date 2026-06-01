'''
Exercício 7 — Troca de Valores 
Crie um algoritmo que leia dois valores inteiros e troque os valores entre as variáveis. 
'''

var_A = input("Digite algum valor para variável A: ")
var_B = input("Digite outro valor para a variável B: ")

var_A, var_B = var_B, var_A

print(f'as variáveis trocadas ficaram com A: {var_A} e B: {var_B}')