#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m².
l= float(input('Digite a largura da parede: '))
a= float(input('Digite a altura da parede: '))
area = l*a
tinta = (area/2)

print('O tamanho da area é {}m² e será necessário {}L de tinta'.format(area,tinta))