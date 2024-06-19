class Conta:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.limite_saque_diario = 3
        self.valor_max_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Parábens seu depósito de R$ {valor:.2f} foi realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saque_diario:
            print("Limite diário de saques atingido.")
        elif valor > self.valor_max_saque:
            print(f"O valor máximo para saque é de R$ {self.valor_max_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        print("\n--- Extrato ---")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"R$ {deposito:.2f}")
        print("Saques:")
        for saque in self.saques:
            print(f"R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

    def resetar_saques_diarios(self):
        self.saques_diarios = 0

# Criando a conta bancária
minha_conta = Conta()

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        minha_conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        minha_conta.sacar(valor)
    elif opcao == "3":
        minha_conta.extrato()
    elif opcao == "0":
        print("Obrigado por usar o nosso sistema bancário!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")








