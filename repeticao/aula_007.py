'''
Exercício 7 — Divisíveis por 2 ou por 3

Crie um algoritmo que receba quatro números inteiros.

Para cada número:
Verifique se ele é divisível por 2 ou por 3.
Apresente o resultado.
'''
i = 0

while i < 4:
    numero = input('Digite seu primeiro número: ')
    i += 1
    if numero.isdigit():
        numero = int(numero)
        if numero % 2 == 0 and numero % 3 == 0:
            print("O seu número é divisivel por 2 e por 3 simultaneamente")
        elif numero % 2 == 0:
            print("O seu número é divisível por 2")
        elif numero % 3 == 0:
            print("O seu número é divisivel por 3")
        else:
            print("O seu número não é divisivel por 2 e por 3")
    else:
        input('O número precisa ser inteiro\n'
              'Pressione "enter" para uma nova tentativa ')