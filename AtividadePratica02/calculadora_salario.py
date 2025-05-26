numero_funcionario = int(input("Digite o número de funcionários: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

salario_total = horas_trabalhadas * valor_por_hora

print(f"Número de funcionários: {numero_funcionario}")
print(f"Valor por hora: R$ {valor_por_hora:.2f}")
print("Horas trabalhadas:", horas_trabalhadas)

print(f"Salário total: R$ {salario_total:.2f}")