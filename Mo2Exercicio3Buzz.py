#Exercícios 3 - FizzBuzz parcial, parte 2

numero = int(input('Digite um número: '))
resultado = numero % 5
if resultado == 0:
	print("Buzz")
else:
	print(numero)