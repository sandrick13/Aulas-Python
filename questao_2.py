# Escreva um programa que solicite um número inteiro positivo ao usuário e calcule a soma de todos os números pares de 1 até esse número.

numero = int(input("Digite um número inteiro positivo: "))

somatodos = 0

for i in range(2, numero, 2):
    somatodos += i

print(f"A soma dos números pares até o {numero:.2f} é {somatodos:.2f}")
