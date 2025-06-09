import re
import numpy as np

def calcular_estatisticas_log(nome_arquivo):
    tempos = []
    regex = r"Epoch \d+/\d+ - .*? - time: (\d+\.\d+)s"
    
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                match = re.search(regex, linha)
                if match:
                    tempos.append(float(match.group(1)))
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    if tempos:
        media = np.mean(tempos)
        desvio_padrao = np.std(tempos)
        
        print(f"Tempos de execução extraídos: {tempos}")
        print(f"Média do tempo de execução: {media:.4f}s")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.4f}s")
    else:
        print("Nenhum tempo de execução encontrado no formato esperado.")

