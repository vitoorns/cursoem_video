#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
salario = float(input('Digite seu salario: '))
aumento = 0.15
calc = salario * aumento
n_salario = salario + calc
print("O seu salario era R${}0 e com o aumento ficará R${}0".format(salario,n_salario))