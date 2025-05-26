ano = int(input("Digite um ano: "))

if ano < 0:
    print("Ano inválido. Por favor, insira um ano não negativo.")

elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")

else:
    print(f"{ano} não é um ano bissexto.")

