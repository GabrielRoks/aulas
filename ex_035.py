'''
Exercício 35 — Consumo Médio

Crie um algoritmo que receba:

distância percorrida (km);

quantidade de combustível consumido (litros).
Apresente o consumo médio em km/l.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# defino as variaveis
distancia = input("Digite a distancia percorrida em Km: ")
litros = input("Digite a quantidade de litros consumido: ")
# execurado caso os dados possam ser convetidos em float
if e_float(distancia) and e_float(litros):
    distancia = float(distancia)
    litros = float(litros)
    litros_por_km = distancia / litros
    print(f'O consumo é: {litros_por_km:.2f}Km/l')
# caso o if seja falso
else:
    print("Digite apenas numeros")