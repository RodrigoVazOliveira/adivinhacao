print("=================================")
print("Bem vindo ao jogo de adivinhacao!")
print("=================================")

numeric_secret = 42

numeric_attempt = 3
round_game = 1

while round_game <= numeric_attempt:
    print("rodada", round_game, ", numero de tentativas: ", numeric_attempt)
    numeric_user = int(input("Digite um o seu numero: "))
    accept = numeric_secret == numeric_user
    numeric_great = numeric_user > numeric_secret
    numeric_minor = numeric_user < numeric_secret

    print("Voce digitou ", numeric_user)
    if accept:
        print("Voce acertou!")
    else:
        if numeric_great:
            print("Maior que o numero do sorteio")
        elif numeric_minor:
            print("O numero e o menor que sorteio")
    round_game += 1

print("Fim do jogo!")