nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"produto: {nome_produto}")
print(f"preço original: R$ {preco_original:.2f}")  
print(f"porcentagem de desconto: {porcentagem_desconto}%")
print(f"valor do desconto: R$ {valor_desconto:.2f}")
print(f"preço final: R$ {preco_final:.2f}")