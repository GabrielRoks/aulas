'''
Exercício 28 — Distância Percorrida

Crie um algoritmo que receba:

velocidade média (km/h);

tempo de viagem (horas).
Apresente a distância percorrida
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# pede os valores de velocidade media e temop
veloc_med = input("Digite a velocidade média em Km/h: ")
tempo = input ("Digite o tempo de viagem em Horas: ")
# atingido caso os valores podem ser convertidos para float
if e_float(veloc_med) and e_float(tempo):
    # converte para float
    veloc_med = float(veloc_med)
    tempo = float(tempo)
    # cria a formula
    distancia = veloc_med * tempo
    # imprime o resultado
    print(f'A distância percorrida foi de: {distancia:.2f}Km')
# atingido caso o if seja falso
else:
    print("Digite apenas números")