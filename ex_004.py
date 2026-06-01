# Calculo de combustivel
"""
Crie um algoritmo que calcule quantos litros de combustível foram gastos em uma viagem sabendo: 
tempo gasto;  
velocidade média;  
consumo do veículo de 12 km/l.  
"""

## 
# distancia = float(input("Digite a distância percorrida em Km: "))
velocidade = float(input("Digite a velocidade média do seu percurso em Km/h: "))
tempo_gasto = float(input('Digite o tempo gasto: '))
distancia = velocidade * tempo_gasto
consumo = print(f'O consumo da sua viagem foi de: {distancia / 12}L.')