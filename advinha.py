import random

def adivinha_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo!")
            elif palpite > numero_secreto:
                print("Muito alto!")
            else:
                print(f"Parabéns, você acertou! O número era {numero_secreto}.")
                print(f"Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    adivinha_numero()
    
