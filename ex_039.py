'''
Exercício 39 — Valor Total da Compra

Crie um algoritmo que receba:

quantidade de produtos comprados;

valor unitário.
Apresente o valor total da compra.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

qnt_produtos = input("Digite a quantidade de produtos comprados: ")
vl_und = input("Digite o valor da unidade desses produtos: ")

if e_float(qnt_produtos) and e_float(vl_und):
    qnt_produtos = float(qnt_produtos)
    vl_und = float(vl_und)
    preco_total = vl_und * qnt_produtos
    print(f"O valor da compra é: R${preco_total:.2f}")
# atingifo caso o if seja falso
else:
    print("Digite apenas numeros")