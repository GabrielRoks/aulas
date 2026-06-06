'''
Exercício 10 — Tratamento por Sexo
Crie um algoritmo que receba:
Nome da pessoa;
Sexo (M ou F).
Apresente:
"Ilmo. Sr. [Nome]" para sexo masculino;
"Ilma. Sra. [Nome]" para sexo feminino.
'''


while True:
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo [M] ou [F]: ").upper()
    if len(nome) < 2:
        print("Favor inserir seu nome")
        continue
    elif sexo == False:
        print("Favor inserir seu sexo")
        continue
    elif sexo == 'M':
        print(f'Ilmo. Sr. {nome}')
        break
    elif sexo == 'F':
        print(f'Ilma. Sra. {nome}')
        break
    else:
        print('Digite apenas "M" ou "F" para o sexo')
        continue