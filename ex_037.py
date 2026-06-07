'''
Exercício 37 — Potência de um Número

Crie um algoritmo que receba:

uma base;

um expoente.
Apresente o resultado da potência.
'''
# crio as var
base = input("Digite um numero: ")
expoente = input("Digite outro numero: ")
# caso possa ser convertido para int
if base.isdigit() and expoente.isdigit():
    base = int(base)
    expoente = int(expoente)
    formula = base**expoente
    print(f'O resultado é: {formula}')
# caso o if seja false
else:
    print("Digite apenas numeros inteiros")