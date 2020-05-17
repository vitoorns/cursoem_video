#faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Digite o valor do produto: '))
d = 0.05
cal= p * d
pdesc = p - cal
print ('O valor do produto é {} o desconto é 5% e o valor do produto como desconto é {}'.format(p,pdesc))