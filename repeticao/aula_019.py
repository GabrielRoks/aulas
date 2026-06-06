'''
Exercício 5 — Soma de Valores com WHILE
Crie um algoritmo que leia números inteiros enquanto o usuário desejar.
Ao final apresente:
Quantidade de números digitados;
Soma dos valores;
Média dos valores.
'''

lista = []
soma = 0
while True:
    numero = input('Digite algum número: ')
    if numero.isdigit():
        numero = int(numero)
        soma = numero + soma
        lista.append(numero)
        media = soma / len(lista)
        continuar = input("Deseja continuar inserindo número? S/N: ").upper()
        if continuar == 'S':
            continue
        else:
            print(f'A quantidade de números digitados foi: {len(lista)}')
            print(f'A soma entre os números foi: {soma}')
            print(f'E a média foi: {media}')
            break
    else: 
        print('Digite apenas numeros inteiros')
        continue