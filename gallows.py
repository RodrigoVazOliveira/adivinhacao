import random


def get_word_secrets():
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            words.append(line.strip())

    number_word = random.randrange(0, len(words))

    return words[number_word]


def print_welcome():
    print('*************************************************************')
    print('***************** Bem vindo ao jogo da forca ****************')
    print('*************************************************************')


def user_win_show():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def user_loser_show():
    print("Puxa, você foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def verify_user_wins_or_loser(accepted):
    if accepted:
        user_win_show()
    else:
        user_loser_show()


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def init_words_accepteds(word_secret):
    return ["_" for letter in word_secret]


def get_word_user():
    attemped_letter = input('Por digite uma letra ')
    attemped_letter = attemped_letter.strip().upper()

    return attemped_letter


def mark_word_accepted(word_secret, attemped_letter, letteres_accepted):
    index = 0
    for letter in word_secret:
        if letter == attemped_letter:
            letteres_accepted[index] = letter
        index = index + 1


def game():
    print_welcome()
    word_secret = get_word_secrets().upper()
    letteres_accepted = init_words_accepteds(word_secret)
    ingallows = False
    accepted = False
    errors = 0

    print(letteres_accepted)
    while not ingallows and not accepted:
        attemped_letter = get_word_user()
        if attemped_letter in word_secret:
            mark_word_accepted(word_secret, attemped_letter, letteres_accepted)
        else:
            errors = errors + 1
            print("Voce errou, numero de erros: {}".format(errors))
            draw_gallows(errors)
        letter_not_accepted = str(letteres_accepted.count("_"))
        print("Voce acertou as seguintes posicoes {} e faltam {}".format(letteres_accepted, letter_not_accepted))
        ingallows = errors == 6
        accepted = "_" not in letteres_accepted

    verify_user_wins_or_loser(accepted)
    print('Fim de jogo')


if __name__ == '__main__':
    game()
