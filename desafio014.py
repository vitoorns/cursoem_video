#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# (3 °C × 9/5) + 32

c = float(input('Digite a temperatura para conversão: '))
conves = (c * (9/5))+32

print('Diante da temperatura de {}graus C a temperatura em fahrenheit é {}'.format(c, conves))




