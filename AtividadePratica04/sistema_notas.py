def registrar_notas():
    notas_validas = []
    print("--- Sistema de Registro de Notas da Turma ---")
    print("Digite as notas dos alunos (0 a 10).")
    print("Para finalizar e calcular a média, digite 'fim'.")
    print("-" * 40) 

    while True:
        entrada = input("Digite a nota do aluno ou 'fim' para terminar: ").strip().lower()

        if entrada == 'fim':
            if not notas_validas: 
                print("\nNenhuma nota foi registrada.")
            break 

        try:
            nota = float(entrada)  
            if 0 <= nota <= 10:
                notas_validas.append(nota)
                print(f"Nota {nota:.1f} registrada com sucesso.") 
            else:
                print("Erro: Nota inválida. As notas devem ser entre 0 e 10.")
        except ValueError:
            
            print("Erro: Entrada inválida. Por favor, insira um número ou 'fim'.")
        
        print("-" * 20) 

    if notas_validas:  
        media_turma = sum(notas_validas) / len(notas_validas)
        print("\n--- Resultado Final ---")
        print(f"Total de notas válidas registradas: {len(notas_validas)}")
        print(f"As notas foram: {', '.join(map(str, notas_validas))}") 
        print(f"A média da turma é: {media_turma:.2f}") 
    else:
        print("Não foi possível calcular a média, pois nenhuma nota válida foi inserida.")
    
    print("-" * 40)
    print("Sistema encerrado.")


registrar_notas()