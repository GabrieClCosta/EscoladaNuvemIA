def verificar_palindromo(frase: str) -> str:
  texto_normalizado = frase.lower()
  texto_limpo_final = "" 
  texto_normalizado = frase.lower()
  for caractere in texto_normalizado:
      if caractere.isalnum():
          texto_limpo_final += caractere
 
  if not texto_limpo_final: 
      return "Não"

  if texto_limpo_final == texto_limpo_final[::-1]:
    return "Sim"
  else:
    return "Não"



entrada_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")


resultado = verificar_palindromo(entrada_usuario)

if resultado == "Sim":
    print(f"A palavra '{entrada_usuario}' é um palíndromo.")
else:
    print(f"A palabra '{entrada_usuario}' não é um palíndromo?")