peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"

elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"

elif 25 <= imc < 29.9:
    classificao = "Sobrepeso"

elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"  

elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"

elif imc >= 40:
    classificaco = "Obesidade grau 3 ou mórbida"



print(f"\nSeu peso: {peso:.2f} kg")
print(f"Sua altura: {altura:.2f} m\n")


print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")