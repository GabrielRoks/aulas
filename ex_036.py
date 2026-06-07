'''
Exercício 36 — Soma e Produto

Crie um algoritmo que leia dois números inteiros e apresente:

a soma entre eles;

o produto entre eles.
'''
# crio as var
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
# caso possa ser convertido para int
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2
    produto = num1 * num2
    print(f'A soma é: {soma}\n'
          f'O produto é: {produto}')
# caso o if seja false
else:
    print("Digite apenas numeros inteiros")