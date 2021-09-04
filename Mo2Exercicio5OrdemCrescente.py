#Exercício 5 - Verificando ordenação

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))
num_3 = int(input('Digite um número: '))
if num_1 > num_2:
	print("não está em ordem crescente")
elif num_1 < num_2 and num_2 > num_3:
	print("não está em ordem crescente")
else:
	print("crescente")