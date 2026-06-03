'''
Exercício 8 — Verificação de Intervalo

Crie um algoritmo que receba um valor inteiro.
Verifique se ele está entre 1 e 9.
Apresente uma mensagem informando o resultado.
'''

while True:
    numero = input("Digite um número: ")
    if numero.isdigit():
        numero = int(numero)
        if numero >= 1 and numero <= 9:
            print(f"O seu número {numero} está entre 1 e 9")
            break
        else:
            print(f"O seu número {numero} não está entre 1 e 9")
            break
    else:
        input('O número precisa ser inteiro\n'
              'Pressione "enter" para uma nova tentativa ')