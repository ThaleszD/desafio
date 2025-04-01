# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função principal
def main():
    # Receber as notas do aluno
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    # Calcular a média
    media = calcular_media(notas)

    # Exibir a média
    print(f"A média do aluno é: {media:.2f}")

    # Verificar se o aluno foi aprovado
    if media >= 7.0:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")

# Executar o programa
if __name__ == "__main__":
    main()
