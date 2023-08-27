# Escreva um programa que solicite um número inteiro ao usuário e mostre a tabuada desse número de 1 a 10.

num = int(input("Digite um número inteiro: "))

for i in range(1,11):
    resultado = num * i
    print(num , "X" , i  , "=", resultado)