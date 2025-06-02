def classificar_e_contar_numeros():
    """
    Solicita números inteiros ao usuário, informa se são pares ou ímpares,
    e ao final exibe a contagem de cada tipo.
    """
    numeros_pares = 0
    numeros_impares = 0

    print("--- Classificador de Números Pares e Ímpares ---")
    print("Digite números inteiros um por um.")
    print("Para encerrar e ver o resultado, digite 'fim'.")
    print("-" * 50)

    while True:
        entrada_usuario = input("Digite um número inteiro (ou 'fim' para sair): ").strip().lower()

        if entrada_usuario == 'fim':
            print("\nEncerrando a entrada de números.")
            break  

        try:
            numero = int(entrada_usuario) 

            
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                numeros_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                numeros_impares += 1
            print("-" * 20) 

        except ValueError:
            
            if entrada_usuario: 
                print(f"Erro: '{entrada_usuario}' não é um número inteiro válido. Tente novamente.")
            else:
                print("Erro: Nenhuma entrada detectada. Tente novamente.")
            print("-" * 20) 
           


    print("\n--- Resultado Final ---")
    print(f"Quantidade de números PARES inseridos: {numeros_pares}")
    print(f"Quantidade de números ÍMPARES inseridos: {numeros_impares}")
    print("-" * 50)
    print("Programa finalizado.")

classificar_e_contar_numeros()