'''
Exercício 21 — Salário por Hora

Crie um algoritmo que receba:

quantidade de horas trabalhadas;

valor pago por hora.
Apresente o salário total a receber.
'''
# pede os valores de horas trabalhadas e o valor de cada hora
horas_trab = input("Digite a quantida de horas trabalhadas: ")
valor_hora = input("Digite o valor pago por hora: ")
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# atingido quando os dados podem ser convertido para float
if e_float(horas_trab) and e_float(valor_hora):
    # converte os dados para float
    horas_trab = float(horas_trab)
    valor_hora = float(valor_hora)
    # cria a formula
    salario = valor_hora * horas_trab
    # imprime o resultado
    print(f'O salário a receber é: R${salario:.2f}')
# atingido caso o if seja false
else:
    print("Favor digitar apenas números")