'''
Exercício 2 — Conversão de Fahrenheit para Celsius 
Crie um algoritmo que receba uma temperatura em graus Fahrenheit e apresente o valor convertido para Celsius. 
'''
# Pede para inserir a temperatura
tempConverter = float(input('Digite uma temperatura em °F: '))
# Converte a temperatura
convertida = (tempConverter - 32) / 1.8
# Imprime no terminal o resultado
print(f"A sua temperatura convertida para °C é: {convertida:.2f}°C")