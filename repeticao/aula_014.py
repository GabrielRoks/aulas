'''
Exercício 4 — Maior e Menor Valor com FOR
Crie um algoritmo que solicite ao usuário uma quantidade determinada de valores.

Utilize FOR para:
Ler todos os valores;
Identificar o maior valor digitado;
Identificar o menor valor digitado;
Apresentar os resultados.
'''
lista = []
for i in range(4):
    numero_add = float(input("Digite algum número: "))
    lista.append(numero_add)

for i in range(1):
    print(lista)
    lista.sort()
    print(f'O seu maior valor foi: {lista[-1]}')
    print(f'E o seu menor valor foi: {lista[0]}')
