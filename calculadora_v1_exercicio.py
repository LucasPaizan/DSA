# Calculadora em Python

# Calculadora desenvolvida com base nos ensinamentos do capitulo 1 e 2 do curso Python Fundamentos Para Análise de Dados 3.0 (DSA)

print("\n******************* Python Calculadora *******************\n")
print("Selecione o número da operação desejada:\n\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

def resultado(num1, num2):
    '''FAZENDO CALCULO DE ACORDO COM NUMERO SELECIONADO'''
    oper = int(input("Escolha a operação 1/2/3/4: "))
    
    if oper == 1:
        input1 = num1
        input2 = num2
        soma = num1 + num2
        print("SOMA: "+str(input1)+" + "+str(input2)+" = "+str(soma))
    elif oper == 2:
        input1 = num1
        input2 = num2
        subtracao = num1 - num2
        print("SUBTRAÇÃO: "+str(input1)+" - "+str(input2)+" = "+str(subtracao))           
    elif oper == 3:
        input1 = num1
        input2 = num2
        multiplicacao = num1 * num2
        print("MULTIPLICAÇÃO: "+str(input1)+" * "+str(input2)+" = "+str(multiplicacao))              
    elif oper == 4:
        input1 = num1
        input2 = num2
        divisao = num1 / num2
        print("DIVISÃO: "+str(input1)+" / "+str(input2)+" = "+str(divisao)) 
    else:
        print("Opção inválida, por favor escolha novamente!")
        resultado(num1, num2)
        
resultado(num1, num2)