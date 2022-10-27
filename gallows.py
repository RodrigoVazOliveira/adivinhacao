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


def verify_user_wins_or_loser(accepted):
    if accepted:
        print("Voce ganhou")
    else:
        print("Voce perdeu")


def init_words_accepteds(word_secret):
    return ["_" for letter in word_secret]


def get_word_user():
    attemped_letter = input('Por digite uma letra ')
    attemped_letter = attemped_letter.strip().upper()

    return attemped_letter


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
        index = 0
        if attemped_letter in word_secret:
            for letter in word_secret:
                if letter == attemped_letter:
                    letteres_accepted[index] = letter
                index = index + 1
        else:
            errors = errors + 1
            print("Voce errou, numero de erros: {}".format(errors))
        letter_not_accepted = str(letteres_accepted.count("_"))
        print("Voce acertou as seguintes posicoes {} e faltam {}".format(letteres_accepted, letter_not_accepted))
        ingallows = errors == 6
        accepted = "_" not in letteres_accepted

    verify_user_wins_or_loser(accepted)
    print('Fim de jogo')


if __name__ == '__main__':
    game()
