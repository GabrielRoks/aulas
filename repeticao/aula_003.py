'''
Exercício 3 — Aprovação com Exame Final

Crie um algoritmo que receba quatro notas de um aluno.
Calcule a média.
Se a média for maior ou igual a 7, apresente "Aluno Aprovado".
Caso contrário, solicite a nota do exame final.
Se a nota do exame for maior ou igual a 5, apresente "Aluno Aprovado em Exame".
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
    elif media < 7:
        print(f'A média foi de: {media:.2f} pontos. Aluno de recuperação, faça o exame final.')
        exfinal = float(input('Digite a nota do exame final: '))
        if exfinal < 5:
            print("Aluno reprovado.")
            break
        else:
            print("Aluno aprovado.")
            break
    else:
        print(f'A média foi de: {media:.2f} pontos. Aluno aprovado.')
        break