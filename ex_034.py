'''
Exercício 34 — Troco de uma Compra

Crie um algoritmo que receba:

valor da compra;

valor pago pelo cliente.
Apresente o valor do troco.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# defino as variaveis
valor_compra = input('Digite o valor da compra: ')
valor_pago = input("Digite o valor pago: ")
# atingido caso possam ser float
if e_float(valor_compra) and e_float(valor_pago):
    valor_compra = float(valor_compra)
    valor_pago = float(valor_pago)
    troco = valor_pago - valor_compra
    print(f"O seu troco é: R${troco:.2f}")
# atingido caso o if seja falso
else:
    print("Digite apenas numeros")