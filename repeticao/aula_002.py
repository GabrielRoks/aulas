'''
Exercício 2 — Média para Aprovação
Crie um algoritmo que receba quatro notas de um aluno.
Calcule a média aritmética.
Se a média for maior ou igual a 7, apresente "Aluno Aprovado".
Caso contrário, apresente "Aluno Reprovado".
'''
while True:
    primeira_nota = float(input('Digite a primeira nota: '))
    segunda_nota = float(input('Digite a segunda nota: '))
    terceira_nota = float(input('Digite a terceira nota: '))
    quarta_nota = float(input('Digite a quarta nota: '))

    media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
    if media > 10:
        print('Desculpe, uma média maior que 10 não é permitida')
        input('Digite "enter" para uma nova tentativa ')

    elif media >= 7:
        print(f'A média foi de: {media:.2f} pontos, Aluno aprovado.')
        break
    else:
        print(f'A média foi de: {media:.2f} pontos, Aluno reprovado.')
        break