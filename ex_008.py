'''
Exercício 8 — Volume de Caixa Retangular 
Crie um algoritmo que calcule o volume de uma caixa retangular utilizando: 
altura;  
largura;  
comprimento.  
'''

# pede a largura
largura = float(input("Digite a largura do seu paralelepípedo em Cm: "))
# pede o comprimento
comprimento = float(input("Digite o comprimento do seu paralelepípedo em Cm: "))
# pede a altura
altura = float(input("Digite a altura do seu paralelepípedo em Cm: "))
# realiza o calculo e imprime
calculo = print(f'O volume do seu paralelepípedo é: {largura * comprimento * altura:.2f}Cm.')