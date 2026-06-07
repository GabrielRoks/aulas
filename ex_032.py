'''
Exercício 32 — Área e Perímetro do Quadrado

Crie um algoritmo que receba o lado de um quadrado e apresente:

área;

perímetro.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# Pede o dado
lado = input("Digite o tamanho do lado do quadrado: ")
#atingido caso possa ser convertido para float
if e_float(lado):
    lado = float(lado)
    perimetro = 4 * lado
    area = lado**2
    print(f'O perímetro do quadrado é: {perimetro}\n'
          f'E a sua area é: {area}')
# atingifo caso o if seja falso
else:
    print("Digite apenas numeros")