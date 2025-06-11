import csv

def escrever_csv(nome_arquivo, dados):
    cabecalho = ['Nome', 'Idade', 'Cidade']
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(cabecalho)
        escritor.writerows(dados)
    
    print(f"Dados salvos com sucesso em '{nome_arquivo}'!")


dados_pessoas = [
    ['Ana', 34, 'São Paulo'],
    ['Bruno', 25, 'Rio de Janeiro'],
    ['Carla', 45, 'Belo Horizonte']
]
