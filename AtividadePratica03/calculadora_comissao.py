nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas do vendedor: "))

comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao

print(f"Vendedor: {nome_vendedor}")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")
