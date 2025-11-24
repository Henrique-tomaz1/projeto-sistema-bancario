# Faça um programa que leia o cateto oposto de um 
# triangulo adjacente de um triangulo retangulo, calcule o ocomprimeiro da hipotenusa
# 

from math import pow,sqrt, hypot
cateto_oposto = float(input('Informe o valor do lado A '))
cateto_adjacente= float(input('Informe o valor do lado B '))
hipo = hypot(cateto_adjacente, cateto_oposto)

# soma = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)

# hipo = sqrt(soma)

print(f' a hipo é {hipo:.2f}')

# ceil arredonda para cima
# floor arrendonda para Baixo
# trunc trucnr numero elimina da virgula para frente
# pow  potencia semelhnte a **
# sqrt  calcula raiz quadrada
# factorial - calculo de fatorial
#radians 


import math

angulo_rad = math.radians(hipo)

seno = math.sin(angulo_rad)
cos = math.cos(angulo_rad)
tan = math.tan(angulo_rad)

print(f' Seno {seno:.2f}\n cos {cos:.2f} \n tan {tan:.2f}')



#seno = cateto oposto / hipo
#cos = cateto adjacente / hipo
# tan = cateto  oposto / adjacente 