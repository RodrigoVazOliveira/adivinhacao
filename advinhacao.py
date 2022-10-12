import random

def advinha():
    print("=================================")
    print("Bem vindo ao jogo de adivinhacao!")
    print("=================================")

    numeric_secret = round(random.randrange(1, 101))
    numeric_attempt = 3
    round_game = 1
    points = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil \n(2) Medio \n(3) Dificil")
    level = int(input("Escolha o nivel: "))

    if level == 1:
        numeric_attempt = 20
    elif level == 2:
        numeric_attempt = 10
    else:
        numeric_attempt = 5

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
            print("Voce acertou! Sua pontuacao total e de {}".format(points))
            break
        else:
            if numeric_great:
                print("Maior que o numero do sorteio")
                if round_game == numeric_attempt:
                    print("o numero secreto era {}, voce fez {}.".format(numeric_secret, points))
            elif numeric_minor:
                print("O numero e o menor que sorteio")
                if round_game == numeric_attempt:
                    print("o numero secreto era {}, voce fez {}.".format(numeric_secret, points))
            points_loser = abs(numeric_secret - numeric_user)
            points -= points_loser

    print("Fim do jogo!")
