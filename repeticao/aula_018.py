'''
Exercício 4 — Maior e Menor Valor com WHILE
Crie um algoritmo que permita ao usuário digitar vários números.
A leitura deve continuar enquanto o valor informado for negativo.
Quando o usuário digitar um valor maior ou igual a zero:
Encerrar a entrada de dados;
Apresentar o maior valor digitado;
Apresentar o menor valor digitado.
'''

lista = []

while True:
    numero = float(input('Digite algum numero negativo\n'
                         '(A operação continuará até que digite um numero positivo): '))
    if numero < 0:
        lista.append(numero)
    else:
        lista.sort()
        print(f'O maior valor digitado foi: {lista[-1]}\n'
              f'E o menor valor digitado foi: {lista[0]}')
        break