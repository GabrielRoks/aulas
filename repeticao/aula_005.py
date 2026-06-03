'''
Exercício 5 — Ordem Crescente
Crie um algoritmo que receba três números inteiros e apresente-os em ordem crescente.
'''

while True:
    prim = input('Digite o primeiro número: ')
    seg = input('Digite o segundo número: ')
    terc = input('Digite o terceiro número: ')

    lista_num = []
    
    try:
        prim, seg, terc = int(prim), int(seg), int(terc)
        lista_num.append(prim)
        lista_num.append(seg)
        lista_num.append(terc)
        lista_num.sort()
        print(lista_num)
        break
    except:
        input('Erro, digite "enter" para continuar')