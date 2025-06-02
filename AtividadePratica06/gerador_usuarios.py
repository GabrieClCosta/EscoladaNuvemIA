import requests

def obter_perfil_aleatorio():
    url_api = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status()  
        
        dados_usuario = resposta.json()
        
        if dados_usuario and 'results' in dados_usuario and len(dados_usuario['results']) > 0:
            usuario = dados_usuario['results'][0]
            
            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email_usuario = usuario['email']
            pais_usuario = usuario['location']['country']
            
            print("--- Perfil de Usuário Aleatório Gerado ---")
            print(f"Nome: {nome_completo}")
            print(f"Email: {email_usuario}")
            print(f"País: {pais_usuario}")
            
        else:
            print("Não foi possível obter os dados do usuário da API.")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar os dados recebidos da API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    obter_perfil_aleatorio()