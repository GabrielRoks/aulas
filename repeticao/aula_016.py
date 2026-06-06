'''
Exercício 2 — Contador Acumulador com WHILE
Crie um algoritmo que utilize um laço WHILE para somar os números de 1 até 100.
Ao final apresente o valor acumulado.
'''

acumulador = 0
i = 1

while i <= 100:
    acumulador += i
    i += 1

print(acumulador)