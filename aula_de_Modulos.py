from math import sqrt
from math import ceil

#A importação desta forma está sendo puxada apenas a função "sqrt"
#import math <- Aqui está trazendo a biblioteca toda de matemática

num = int(input('Digite um número que deseja saber a raiz quadrada: '))
raiz = sqrt(num)
#raiz = math.sqrt(num) <= aqui seria utilizado caso tivessse importado toda a biblioteca e não uma unica função.

print('A raiz quadrada de {} é {}'.format(num,ceil(raiz)))
