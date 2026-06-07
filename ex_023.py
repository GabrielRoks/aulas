'''
Exercício 23 — Valor da Prestação

Crie um algoritmo que calcule o valor de uma prestação em atraso utilizando:

valor da prestação;

taxa de juros (%);

tempo de atraso (meses).
Apresente o valor atualizado.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# pedem os dados de prestaçao, taxa mensal e quantidade meses   
prestacao = input("Digite o valor da sua prestação: ")
taxa = input("Digite a taxa de juros mensal: ")
meses = input("Tempo de atraso em meses: ")
# atingido quando os dados de prestação e taxa podem ser float e de meses podem ser int
if e_float(prestacao) and e_float(taxa) and meses.isdigit():
    # convertem os dadosd
    prestacao = float(prestacao)
    taxa = float(taxa)
    meses = int(meses)
    # cria a formula
    juros_comp = prestacao * (1 + (taxa / 100))**meses
    # imprime o resultado
    print(f'O valor a se pagar após os juros por atraso é: {juros_comp:.2f}')
# atingido caso o if seja falso
else:
    print("Digite apenas números")