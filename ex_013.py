'''
Exercício 13 — Reajuste Salarial 
Crie um algoritmo que calcule o novo salário de um funcionário com base em um percentual de reajuste informado pelo usuário. 
'''

# Pede o valor do salário atual
salario = float(input('Digite seu salário atual (ex: 1621.00): '))
# Pede a porcentagem de aumento
porcentagem = float(input('Digite o percentual de reajuste do seu salário (ex: 7): '))
# realiza o reajuste
reajuste = (salario * porcentagem) / 100
# imprime o reajuste e o salario com reajuste
salario_reajustado = print(f'O seu reajuste foi de R${reajuste}\n'
                           f'E o seu salario reajustado ficou em R${reajuste + salario:.2f}')