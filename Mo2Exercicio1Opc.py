#Exercício 1 - Distância entre dois pontos

import math

x1 = int(input("Digite um número "))
x2 = int(input("Digite um número "))
y1 = int(input("Digite um número "))
y2 = int(input("Digite um número "))

distancia = math.sqrt(((x1 - x2)**2) + ((y1  - y2)**2))
if distancia >= 10:
	print("longe")
else:
	print("perto")