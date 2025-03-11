import os

#limpando a tela 
os.system("cls")

# Funções de operações básicas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Função principal da calculadora
def calculadora():
    print("Escolha a operação que deseja realizar:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    # Verificar se a escolha é válida
    if escolha not in ['1', '2', '3', '4']:
        print("Operação inválida.")
        return

    # Solicitar os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizar a operação escolhida
    if escolha == '1':
        print(f"{num1} + {num2} = {somar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Chamar a função principal
calculadora()