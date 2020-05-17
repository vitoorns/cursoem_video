#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua taboada
n = int(input('Digite um numero: '))
contador = 0
while (contador <= 10):
    print('{} x {} = '.format(n,contador) ,n*contador)
    contador = contador + 1
