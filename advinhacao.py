import random


def to_define_level(level):
    if level == 1:
        return 20
    elif level == 2:
        return 10
    else:
        return 5


def get_level_game():
    print("Qual o nivel de dificuldade?")
    print("(1) Facil \n(2) Medio \n(3) Dificil")
    return int(input("Escolha o nivel: "))


def is_inside_interval(numeric_user):
    if numeric_user < 1 or numeric_user > 100:
        print("Voce deve digitar um numero entre 1 a 100!")
        return True
    return False


def get_numeric_attempt_game(round_game, numeric_attempt):
    print("rodada {}, numero de tentativas {}".format(round_game, numeric_attempt))
    return int(input("Digite um o seu numero de 1 a 100: "))


def user_not_accept(numeric_great,
                    numeric_minor,
                    round_game,
                    numeric_attempt,
                    numeric_secret, points):
    if numeric_great:
        print("Maior que o numero do sorteio")
        if round_game == numeric_attempt:
            print("o numero secreto era {}, voce fez {}.".format(numeric_secret, points))
    elif numeric_minor:
        print("O numero e o menor que sorteio")
        if round_game == numeric_attempt:
            print("o numero secreto era {}, voce fez {}.".format(numeric_secret, points))


def adjust_points(numeric_secret, numeric_user):
    points_loser = abs(numeric_secret - numeric_user)
    return points_loser


def run_new_game(round_game,
                 numeric_attempt,
                 numeric_secret,
                 points,
                 numeric_user):
    # is_inside_interval(numeric_user)
    accept = numeric_secret == numeric_user
    numeric_great = numeric_user > numeric_secret
    numeric_minor = numeric_user < numeric_secret

    print("Voce digitou ", numeric_user)
    if accept:
        print("Voce acertou! Sua pontuacao total e de {}".format(points))
        return True
    else:
        user_not_accept(numeric_great, numeric_minor, round_game, numeric_attempt, numeric_secret, points)
        return False


def execute():
    print("=================================")
    print("Bem vindo ao jogo de adivinhacao!")
    print("=================================")
    numeric_secret = round(random.randrange(1, 101))
    round_game = 1
    points = 1000
    level = get_level_game()
    numeric_attempt = to_define_level(level)

    for round_game in range(1, numeric_attempt + 1):
        numeric_user = get_numeric_attempt_game(round_game, numeric_attempt)
        result_game = run_new_game(round_game, numeric_attempt, numeric_secret, points, numeric_user)
        points = points - adjust_points(numeric_secret, numeric_user)
        if result_game:
            break

    print("Fim do jogo!")


if __name__ == "__main__":
    execute()
