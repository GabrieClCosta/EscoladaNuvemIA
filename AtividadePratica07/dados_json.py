import json

def manipular_json(nome_arquivo):

    pessoa = {
        "nome": "Daniel",
        "idade": 29,
        "cidade": "Salvador",
        "habilidades": ["Python", "SQL", "Data Analysis"]
    }

    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(pessoa, f, indent=4, ensure_ascii=False)
        
    print(f"Dados escritos em '{nome_arquivo}'")

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados_lidos = json.load(f)
        
    print("\nDados lidos do arquivo:")
    print(dados_lidos)

