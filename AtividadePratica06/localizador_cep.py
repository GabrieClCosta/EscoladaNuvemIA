import requests

def consultar_endereco_por_cep():
    cep_input = input("Digite o CEP (apenas números, ex: 01001000): ").strip()

    if not cep_input.isdigit() or len(cep_input) != 8:
        print("Formato de CEP inválido. Por favor, digite 8 números.")
        return

    url_api = f"https://viacep.com.br/ws/{cep_input}/json/"

    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status() 
        
        dados_endereco = resposta.json()

        if dados_endereco.get("erro"):
            print(f"CEP {cep_input} não encontrado ou inválido.")
        else:
            print("\n--- Endereço Encontrado ---")
            print(f"CEP: {dados_endereco.get('cep', 'N/A')}")
            print(f"Logradouro: {dados_endereco.get('logradouro', 'N/A')}")
            print(f"Bairro: {dados_endereco.get('bairro', 'N/A')}")
            print(f"Cidade: {dados_endereco.get('localidade', 'N/A')}")
            print(f"Estado (UF): {dados_endereco.get('uf', 'N/A')}")
            if dados_endereco.get('complemento'):
                 print(f"Complemento: {dados_endereco.get('complemento')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar conectar com a API ViaCEP: {e}")
    except ValueError:
        print("Erro ao processar a resposta da API (não é um JSON válido).")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

consultar_endereco_por_cep()