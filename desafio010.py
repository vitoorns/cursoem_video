#crie um programa que leia quanto dinheiro uma pessoa tem na carteira mostre quantos dollares ela pode comprar
#considerar o dollar 3,37
dinheiro = float(input('Digite o valor de dinheiro na carteira: '))
dollar = float (input('Digite o valor do dolar: '))
calculo = dinheiro/dollar

print ('com esse valor {} você pode comprar: US${:.2f}0'.format(dinheiro, calculo))