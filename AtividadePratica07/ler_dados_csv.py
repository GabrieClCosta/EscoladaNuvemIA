import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)
            cabecalho = next(leitor)
            print(f"{cabecalho[0]:<10} {cabecalho[1]:<5} {cabecalho[2]:<15}")
            print("-" * 30)
            
            for linha in leitor:
                print(f"{linha[0]:<10} {linha[1]:<5} {linha[2]:<15}")
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

