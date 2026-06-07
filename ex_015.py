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

# Pedem a quantidade votos dos candidatos, votos em branco e nulo
votos_cA = int(input('Digite a quantidade de votos do candidato A: '))
votos_cB = int(input('Digite a quantidade de votos do candidato B: '))
votos_cC = int(input('Digite a quantidade de votos do candidato C: '))
votos_brancos = int(input('Digite a quantidade de votos em branco: '))
votos_nulos = int(input('Digite a quantidade de votos nulo: '))

# Soma o total de voltos
total_votos = votos_cA + votos_cB + votos_cC + votos_brancos + votos_nulos
# Imprime o total de votos
todos_votos = print(f'O total de votos foi: {total_votos}')
# Imprime a porcentagem de votos de casa candidato
votos_candidatos = print(f'A porcentagem de votos do candidato A foi de: {(votos_cA * 100)/total_votos:.2f}%\n'
                         f'A porcentagem de votos do candiadto B foi de: {(votos_cB * 100)/total_votos:.2f}%\n'
                         f'A porcentagem de votos do candiadto C foi de: {(votos_cC * 100)/total_votos:.2f}%')
# imprime a porcentagem de votos em branco
porc_votos_brancos = print(f'A porcentagem de votos brancos é: {(votos_brancos * 100)/total_votos:.2f}%')
# imprime a porcentagem de voto nulos
porc_votos_nulos = print(f'A porcentagem de votos nulos é: {(votos_nulos * 100)/total_votos:.2f}%')
# imprime a quantidade de votos validos
quant_votos_validos = print(f'A quantidade de votos válidos é de: {total_votos - votos_nulos - votos_brancos} votos.')