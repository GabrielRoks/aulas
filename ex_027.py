'''
Exercício 27 — Custo de um Produto

Crie um algoritmo que receba:

valor de fábrica de um produto;

percentual de lucro.
Apresente o preço final de venda.
'''
# Cria uma função para validar se um valor digitado pode ser float
def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
# pedem o preço de fabrica e o lucro que se que pelo produto
preco_fab = input("Digite o valor de fábrica do produto: ")
lucro = input("Digite o percentual de lucro que deseja receber: ")
# Atingido caso os dois valores inseridos podem ser convertidos para float
if e_float(preco_fab) and e_float(lucro):
    # converte para float
    preco_fab = float(preco_fab)
    lucro = float(lucro)
    # Cria a formula
    preco_corrigido = ((lucro * preco_fab) / 100) + preco_fab
    # imprime o rwsultado
    print(f"O preço final de venda do pruto fica em: R${preco_corrigido:.2f}")
# Atingido quando o if é faslo
else:
    print("Digite apenas números")