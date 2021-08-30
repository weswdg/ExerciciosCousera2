import math

a = float(input('Digite um valor para A: '))
b = float(input('Digite um valor para B: '))
c = float(input('Digite um valor para C: '))

delta = b ** 2 -4 * a * c

if delta < 0:
	print("esta equação não possui raízes reais")
elif delta == 0:
	print("a raiz desta equação é x")
elif delta > 0:
	raiz1 = (-b + math.sqrt(delta)) / (2 * a)
	raiz2 = (-b - math.sqrt(delta)) / (2 * a)
	print("as raizes da equação são x e y")
	if raiz1 < raiz2:
		print("as raízes da equação são", raiz1, "e", raiz2)
	if raiz2 < raiz1:
		print("as raízes da equação são", raiz2, "e", raiz1)