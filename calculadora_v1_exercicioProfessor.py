# Calculadora em Python

# Calculadora com resolução do PROFESSOR com base nos ensinamentos do capitulo 1 e 2 do curso Python Fundamentos Para Análise de Dados 3.0 (DSA)

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\nDigite sua opção (1/2/3/4): ")

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

if escolha == '1':
	print("\n")
	print(num1, "+", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/", num2, "=", add(num1, num2))
	print("\n")

else:
	print("\nOpção Inválida!")