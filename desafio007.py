#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = float((n1+n2)/2)

print ('A média do alunoe é {}'.format(m))

if m < 7:
    print('recuperação!!')
else:
    print ('Parabens, passou!! ')