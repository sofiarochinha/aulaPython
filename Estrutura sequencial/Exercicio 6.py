import math #importa-se uma biblioteca para aceder a formulas matemáticas e constantes

print('Calcular a área de um círculo a partir do raio')

raio = int(input('Insira o raio do círculo: '))

areaCirculo = math.pi * raio * raio

print('A área do círculo é: ' + str(areaCirculo))
