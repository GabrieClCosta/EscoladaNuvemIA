idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida. Por favor, insira uma idade não negativa.")

elif idade <= 12:
    print("Você é criança.")

elif idade <= 17:
    print("Você é adolescente.")

elif idade <= 59:
    print("Você é adulto.")   

else:
    print("Você é idoso.")