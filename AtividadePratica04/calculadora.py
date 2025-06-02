def calculadora():

    while True:
        
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)  
        except ValueError:
            print("Erro: Entrada inválida para o primeiro número. Por favor, insira um valor numérico.")
            continue  

        
        try:
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)
        except ValueError:
            print("Erro: Entrada inválida para o segundo número. Por favor, insira um valor numérico.")
            continue  

       
        operacao = input("Digite a operação desejada (+, -, *, /): ").strip() # .strip() remove espaços extras

        
        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                
                raise ValueError("Operação inválida.")

            
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break 

        except ZeroDivisionError as zde:
            print(f"Erro: {zde} Por favor, tente novamente.")
            
        except ValueError as ve: 
            print(f"Erro: {ve} As operações válidas são +, -, *, /. Tente novamente.")
            
        except Exception as e: 
            print(f"Ocorreu um erro inesperado durante a operação: {e}. Tente novamente.")
            



print("=======Bem-vindo à Calculadora Python!=======")
calculadora()
print("Calculadora encerrada.")