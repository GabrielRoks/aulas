'''
Exercício 31 — Comissão de Vendas

Crie um algoritmo que receba:

salário fixo de um vendedor;

valor total das vendas;

percentual de comissão.
Apresente o salário final.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
# Pede o salario fixo, venda total e percentual
salario_fixo = input("Digite o salário fixo: ")
valor_venda_total = input("Digite o valor total de venda: ")
percentual = input("Digite o percentual de comissão: ")
# é atingido caso possam ser convertidos para floar
if e_float(salario_fixo) and e_float(valor_venda_total) and e_float(percentual):
    salario_fixo = float(salario_fixo)
    valor_venda_total = float(valor_venda_total)
    percentual = float(percentual)
    salario_comissao = salario_fixo + ((percentual * valor_venda_total) / 100)
    print(f'O salario junto da comissão é de: R${salario_comissao:.2f}')
# é atingifo caso o if seja false
else:
    print("Digite apenas números")