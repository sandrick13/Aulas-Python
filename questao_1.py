# Questão 1: Desenvolvimento de Programa - Caixa Eletrônico Simples

# Você foi contratado para desenvolver um programa em Python que simule um caixa eletrônico simples. 
# O programa deve permitir que o usuário escolha entre três opções: verificar saldo, sacar dinheiro e depositar dinheiro. 
# O programa deve solicitar as entradas necessárias do usuário e fornecer as saídas apropriadas. O saldo inicial da conta é R$ 1000,00. 
# Desenvolva o programa de acordo com a especificação acima.


class CaixaEletronico:
    def __init__(self):
        self.saldo = 1000
    
    def verificar_saldo(self,valor):
        return self.saldo
    
    def sacar_dinheiro(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso"
        else:
            return "Saldo insuficiente para realizar saque"
    
    def depositar_dinheiro(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:.2f} realizado com sucesso"
    
caixa = CaixaEletronico()

while True:
    print("1 - Verificar Saldo")
    print("2 - Sacar Dinheiro")
    print("3 - Depositar Dinheiro")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        print(f"Seu saldo atual é: R${caixa.verificar_saldo():.2f}")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor para saque: "))
        print(caixa.sacar_dinheiro(valor_saque))
    elif opcao == 3:
        valor_deposito = float(input("Digite o valor para depósito: "))
        print(caixa.depositar_dinheiro(valor_deposito))
    elif opcao == 4:
        print("Saindo do programa")
        break
    else:
        print("Opção inválida")

        






