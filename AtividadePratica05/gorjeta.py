def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
  if valor_conta < 0:
    raise ValueError("O valor da conta não pode ser negativo.")
  if porcentagem_gorjeta < 0:
    raise ValueError("A porcentagem da gorjeta não pode ser negativa.")

  gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return gorjeta


try:
    valor_conta_input = float(input("Digite o valor total da conta: R$"))
    porcentagem_gorjeta_input = float(input("Digite a porcentagem da gorjeta desejada (ex: 15 para 15%): "))

    valor_gorjeta_calculada = calcular_gorjeta(valor_conta_input, porcentagem_gorjeta_input)

    print(f"O valor da gorjeta para uma conta de R${valor_conta_input:.2f} é R${valor_gorjeta_calculada:.2f}.")

except ValueError as e:
    print(f"Erro na entrada de dados: {e}. Por favor, insira valores numéricos válidos.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")