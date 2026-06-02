'''
Exercício 15 — Sistema de Votação 
Crie um algoritmo que receba: 
quantidade de votos do candidato A;  
quantidade de votos do candidato B;  
quantidade de votos do candidato C;  
quantidade de votos brancos;  
quantidade de votos nulos.  
O algoritmo deve apresentar: 
total de votos;  
porcentagem de votos de cada candidato;  
porcentagem de votos brancos;  
porcentagem de votos nulos;  
quantidade de votos válidos.
'''

votos_cA = int(input('Digite a quantidade de votos do candidato A: '))
votos_cB = int(input('Digite a quantidade de votos do candidato B: '))
votos_cC = int(input('Digite a quantidade de votos do candidato C: '))
votos_brancos = int(input('Digite a quantidade de votos em branco: '))
votos_nulos = int(input('Digite a quantidade de votos nulo: '))

total_votos = votos_cA + votos_cB + votos_cC + votos_brancos + votos_nulos
todos_votos = print(f'O total de votos foi: {total_votos}')

votos_candidatos = print(f'A porcentagem de votos do candidato A foi de: {(votos_cA * 100)/total_votos:.2f}%\n'
                         f'A porcentagem de votos do candiadto B foi de: {(votos_cB * 100)/total_votos:.2f}%\n'
                         f'A porcentagem de votos do candiadto C foi de: {(votos_cC * 100)/total_votos:.2f}%')

porc_votos_brancos = print(f'A porcentagem de votos brancos é: {(votos_brancos * 100)/total_votos:.2f}%')

porc_votos_nulos = print(f'A porcentagem de votos nulos é: {(votos_nulos * 100)/total_votos:.2f}%')

porc_votos_validos = print(f'A quantidade de votos válidos é de: {total_votos - votos_nulos - votos_brancos} votos.')