#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.
#raiz quadrada ex: 5/(1/2) ***verificar isso

n1 = int(input('Digite um numero: '))
raiz = int(n1**(1/2))

print('O número digitado é {}, o dobro dele é {}, o triplo é {} e a raiz dele é {}'.format(n1, n1*2, n1*3, raiz))

