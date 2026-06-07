'''
Exercício 17 — Antecessor e Sucessor

Crie um algoritmo que receba um número inteiro e apresente seu antecessor e seu sucessor.
'''
# Pede um numero inteiro
numero = input("Digite um número inteiro: ")
# Operação de condiçao, atingida caso o valor digitado pode ser convertido para um inteiro positivo
if numero.isdigit():
    # converte para int
    numero = int(numero)
    # define variaveis de anterior e sucessor
    ant = numero - 1
    suc = numero + 1
    # imprime o resultado
    print(f'O antecessor do seu número é: {ant}\n'
          f'E o sucessor do seu número é: {suc}')
    
# é atingido caso o primeiro if seja false
else:
    print("Favor digitar apenas número inteiros")