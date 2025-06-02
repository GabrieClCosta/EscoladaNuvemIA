from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    data_hoje = date.today()
    ano_atual = data_hoje.year

    if ano_nascimento > ano_atual or ano_nascimento < 1880:
        raise ValueError("Ano invalido")

    dia_atual = data_hoje.day
    mes_atual = data_hoje.month
    
    dia_nascimento_para_calculo = dia_atual

    if mes_atual == 2 and dia_atual == 29:
        is_nascimento_bissexto = (ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0) or \
                                 (ano_nascimento % 400 == 0)
        if not is_nascimento_bissexto:
            dia_nascimento_para_calculo = 28
    
    data_nascimento_estimada = date(ano_nascimento, mes_atual, dia_nascimento_para_calculo)
    
    diferenca_datas = data_hoje - data_nascimento_estimada
    return diferenca_datas.days


try:
    entrada_ano = int(input("Digite o ano de nascimento: "))
    idade_em_dias_calculada = calcular_idade_em_dias(entrada_ano)
    print(f"Idade aproximada em dias: {idade_em_dias_calculada}")
except ValueError as e:
    print(f"Erro: {e}")
except Exception:
    print("Erro: Entrada invalida.")