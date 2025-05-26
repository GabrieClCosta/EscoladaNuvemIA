temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper() 
destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()

if origem == 'C':
    if destino == 'F':
        fahrenheit = (temp * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
    elif destino == 'K':
        kelvin = temp + 273.15
        print(f"A temperatura em Kelvin é: {kelvin:.2f}K")
    else:
        print("Unidade de destino inválida.")

if origem == 'F':
    if destino == 'C':
        celsius = (temp - 32) * 5/9
        print(f"A temperatura em Celsius é: {celsius:.2f}°C")
    elif destino == 'K':
        kelvin = (temp - 32) * 5/9 + 273.15
        print(f"A temperatura em Kelvin é: {kelvin:.2f}K")
    else:
        print("Unidade de destino inválida.")

if origem == 'K':
    if destino == 'C':
        celsius = temp - 273.15
        print(f"A temperatura em Celsius é: {celsius:.2f}°C")
    elif destino == 'F':
        fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
    else:
        print("Unidade de destino inválida.")



