#faça um programa que leio um ângulo qualquer e mostre na tela o valor do seno, coseno e o tangente desse angulo
import math
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
conseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o Seno de {:.2f} '.format(angulo,seno))

print('O angulo de {} tem o conseno de {:.2f}'.format(angulo,conseno))

print('O angulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))
