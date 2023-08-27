idade = int(input("Digite a sua idade :"))
peso = int(input("Digite o seu peso : "))
tempo_de_sono = int(input("Quantas horas você dormiu na noite anterior? "))

if (idade > 16) and (idade < 69) and (peso > 50) and (tempo_de_sono >= 6):
    print("Você está apto a doar sangue ")
else:
    print("Você não pode doar sangue ")