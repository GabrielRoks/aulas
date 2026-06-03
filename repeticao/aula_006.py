'''
Exercício 6 — Divisíveis por 2 e por 3
Crie um algoritmo que receba quatro números inteiros.
Para cada número:
Verifique se ele é divisível por 2 e por 3 simultaneamente.
Apresente o resultado.
'''

while True:
    numero = input('Digite seu primeiro número: ')
    if numero.isdigit():
        numero = int(numero)
        if numero % 2 == 0 and numero % 3 == 0:
            print("O seu número é divisivel por 2 e por 3 simultaneamente")
            break
        else:
            print("O seu número não é divisivel por 2 e por 3 simultaneamente")
            break
    else:
        input('O número precisa ser inteiro\n'
              'Pressione "enter" para uma nova tentativa ')