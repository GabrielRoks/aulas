'''
Exercício 26 — Divisão Inteira e Resto

Crie um algoritmo que receba dois números inteiros e apresente:

resultado da divisão inteira;

resto da divisão.
'''
# pedem dois numeros
numero = input("Digite um número inteiro: ")
divisor = input("Digite outro número inteiro: ")
# atingido caso os numeros podem ser covertidos para int positivo
if numero.isdigit() and divisor.isdigit():
    # converte para int
    numero = int(numero)
    divisor = int(divisor)
    # faz a divisão inteira
    divisao_inteira = numero // divisor
    # retira apenas o resto da divisão
    resto_div = (numero / divisor) - divisao_inteira
    # imprime o resukltado
    print(f'A sua divisão inteira do primeiro número pelo segundo foi: {divisao_inteira}\n'
          f'E o resto da divisão foi: {resto_div:.2f}')
# atingido caso o if seja false
else:
    print("Digite apenas números inteiros")