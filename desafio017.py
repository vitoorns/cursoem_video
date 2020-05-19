#27:15
#Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa.
import math

co = float(input ('Digite o valor do cateto oposto: '))
ca = float(input ('Digite o valor do cateto adjacente: '))

x = co
y = ca

print('O valor da hipotenusa é: {:.2f}'.format(math.hypot(x,y)))