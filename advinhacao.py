import random

print("=================================")
print("Bem vindo ao jogo de adivinhacao!")
print("=================================")

numeric_secret = round(random.random() * 100)

numeric_attempt = 3
round_game = 1

# while round_game <= numeric_attempt:
for round_game in range(1, numeric_attempt + 1):
    print("rodada {}, numero de tentativas {}".format(round_game, numeric_attempt))
    numeric_user = int(input("Digite um o seu numero de 1 a 100: "))
    accept = numeric_secret == numeric_user
    numeric_great = numeric_user > numeric_secret
    numeric_minor = numeric_user < numeric_secret

    if numeric_user < 1 or numeric_user > 100:
        print("Voce deve digitar um numero entre 1 a 100!")
        continue

    print("Voce digitou ", numeric_user)
    if accept:
        print("Voce acertou!")
        break
    else:
        if numeric_great:
            print("Maior que o numero do sorteio")
        elif numeric_minor:
            print("O numero e o menor que sorteio")

print("Fim do jogo!")
