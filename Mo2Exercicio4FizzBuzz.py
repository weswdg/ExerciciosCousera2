#Exercícios 4 - FizzBuzz parcial, parte 3

numero = int(input('Digite um número: '))
resultado = numero % 15
if resultado == 0:
	print("FizzBuzz")
else:
	print(numero)