def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def obter_numero(prompt):
    while True:
        entrada = input(prompt)
        entrada = entrada.replace(',', '.')
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def obter_escolha():
    return input("Digite a sua escolha (1/2/3/4/5): ")

while True:
    menu()
    escolha = obter_escolha()

    if escolha == '5':
        print("Obrigado por usar a nossa calculadora. Até a proxima!")
        break

    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")

    if escolha == '1':
        print(f"{num1} + {num2} = {adicao(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
    elif escolha == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")

    print()  # Linha em branco para melhorar a legibilidade entre operações
