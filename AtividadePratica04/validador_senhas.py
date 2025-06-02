def verificar_forca_senha():

    print("--- Verificador de Força de Senha ---")
    print("Uma senha forte deve ter:")
    print("  1. Pelo menos 8 caracteres.")
    print("  2. Pelo menos um número (0-9).")
    print("Digite 'sair' a qualquer momento para encerrar o programa.")
    print("-" * 40)

    while True:
        senha_usuario = input("Digite a senha desejada (ou 'sair'): ").strip()

        if senha_usuario.lower() == 'sair':
            print("Verificação de senha encerrada pelo usuário.")
            break

        
        comprimento_ok = False
        tem_numero = False

        
        if len(senha_usuario) >= 8:
            comprimento_ok = True

        
        for caractere in senha_usuario:
            if caractere.isdigit():
                tem_numero = True
                break 

        
        if comprimento_ok and tem_numero:
            print("✅ Senha forte! Critérios atendidos.")
            break  
        else:
            print("\n❌ Senha fraca. Por favor, tente novamente.")
            if not comprimento_ok:
                print(f"   - A senha deve ter pelo menos 8 caracteres. (Sua senha tem {len(senha_usuario)}).")
            if not tem_numero:
                print("   - A senha deve conter pelo menos um número (0-9).")
            print("-" * 20) 


verificar_forca_senha()