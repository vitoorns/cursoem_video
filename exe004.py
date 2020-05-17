#faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele;

n1 = input("digite algo")

print ('o tipo primitivo deste valor é ', type(n1))
print ('Só tem espaços? ', n1.isspace())
print('É um numero? ',n1.isnumeric())
print('É alfabéico? ',n1.isalpha())
print ('É alfanumerico? ', n1.isalnum())
print('está em maiusculo? ', n1.islower())
print ('está em minusculo? ', n1.isupper())
print (.fotmat(n1))