'''
Exercício 2 — Contador Acumulador com FOR
Crie um algoritmo que utilize um laço FOR para somar os números de 1 até 100.
Ao final apresente o valor acumulado.
'''
acumulador = 0
for i in range(1, 101):
    acumulador += i

print(acumulador)