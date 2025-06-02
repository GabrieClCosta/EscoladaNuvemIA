import random
import string

def gerar_senha_aleatoria(comprimento):
    if not isinstance(comprimento, int) or comprimento <= 0:
        raise ValueError("O comprimento deve ser um número inteiro positivo.")
    
    caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres_disponiveis, k=comprimento))
    return senha


try:
    num_caracteres = int(input("Digite a quantidade de caracteres para a senha: "))
    if num_caracteres > 0:
        senha_criada = gerar_senha_aleatoria(num_caracteres)
        print(f"Senha gerada: {senha_criada}")
    else:
        print("A quantidade de caracteres deve ser um número positivo.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")