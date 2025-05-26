N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

media = (N1 + N2 + N3 + N4) / 4

if media >= 7:
    print("Aluno aprovado!")
    print(f"Média: {media:.1f}")

elif media <= 5:
    print("Aluno reprovado!")
    print(f"Média: {media:.1f}")

elif 5 < media < 6.9:
    print("Aluno em exame!")
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (media + nota_exame) / 2
    if media_final >= 5:
        print("Aluno aprovado!")
        print(f"Média final: {media_final:.1f}")
    elif media_final <= 4.9:
        print("Aluno reprovado!")
        print(f"Média final: {media_final:.1f}")