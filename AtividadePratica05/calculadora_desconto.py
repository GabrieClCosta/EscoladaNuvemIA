def calcular_preco_com_desconto():
  try:
    preco_original = float(input("Digite o preço original do produto (ex: 250.75): R$"))
    percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

    if preco_original < 0 or percentual_desconto < 0:
      print("Erro: O preço original e o percentual de desconto não podem ser negativos.")
      return
    if percentual_desconto > 100:
      print("Aviso: O percentual de desconto é maior que 100%. O preço final será negativo ou zero.")

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto

    print(f"\n--- Resumo do Cálculo ---")
    print(f"Preço Original: R${preco_original:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto}%")
    print(f"Valor do Desconto: R${valor_desconto:.2f}")
    print(f"Preço Final com Desconto: R${preco_final:.2f}")

  except ValueError:
    print("Erro: Entrada inválida. Por favor, insira valores numéricos válidos.")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

calcular_preco_com_desconto()