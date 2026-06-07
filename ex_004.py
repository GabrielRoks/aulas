# Calculo de combustivel
"""
Crie um algoritmo que calcule quantos litros de combustível foram gastos em uma viagem sabendo: 
tempo gasto;  
velocidade média;  
consumo do veículo de 12 km/l.  
"""

## 
# Pede a velocidade média
velocidade = float(input("Digite a velocidade média do seu percurso em Km/h: "))
# pede o tempo de viagem
tempo_gasto = float(input('Digite o tempo gasto: '))
# calcula a distancia
distancia = velocidade * tempo_gasto
# imprime o resultado
consumo = print(f'O consumo da sua viagem foi de: {distancia / 12}L.')