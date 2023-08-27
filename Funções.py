nome = "Python"
def soma_multiplicar (valor1, valor2, operacao):
    print(nome)
    if operacao == "somar":
        resultado = valor1 + valor2
    if operacao == "multiplicar":
        resultado = valor1 * valor2
    return resultado

valor_1 = float(input("Informe o valor 1: "))
valor_2 = float(input("Informe o valor 2: "))
opcao = input("Qual a operação: ")

resutado = soma_multiplicar(valor_1, valor_2, opcao)

print(resutado)


