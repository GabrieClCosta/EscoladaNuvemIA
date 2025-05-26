valor_em_reais = 100.00
taxa_dolar = 5.65
taxa_euro = 6.45

valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

print(f"Valor em reais: R$ {valor_em_reais:.2f}")
print(f"Valor em dólares: $", round(valor_em_dolares, 2))
print(f"Valor em euros: €", round(valor_em_euros, 2))