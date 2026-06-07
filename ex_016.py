'''
Exercício 16 — Média Aritmética

Crie um algoritmo que leia três notas de um aluno e apresente a média aritmética.
'''
# pede as notas
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
# Variavel que cria a operação
media = (nota_1 + nota_2 + nota_3) / 3
# imprime o resultado
print(f"A média das notas foi: {media}")