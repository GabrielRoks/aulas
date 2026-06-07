'''
Exercício 1 — Conversão de Celsius para Fahrenheit 
Crie um algoritmo que receba uma temperatura em graus Celsius e apresente o valor convertido para Fahrenheit. 
'''

# Pede para inserir a temperatura
tempInserida = float(input("Digite uma temperatura: "))
# Converte a temperatura
conversao = (tempInserida * 1.8) + 32
# Imprime no terminal o resultado
print(f'Sua temperatura convertida é de: {conversao:.2f}°F')