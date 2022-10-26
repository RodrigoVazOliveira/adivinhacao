def game():
    print('*************************************************************')
    print('***************** Bem vindo ao jogo da forca ****************')
    print('*************************************************************')

    word_secret = "BANANA"
    letteres_accepted = ["_", "_", "_", "_", "_", "_"]
    ingallows = False
    accepted = False
    errors = 0

    print(letteres_accepted)
    while not ingallows and not accepted:
        attemped_letter = input('Por digite uma letra ')
        attemped_letter = attemped_letter.strip().upper()
        index = 0
        if attemped_letter in word_secret:
            for letter in word_secret:
                if letter == attemped_letter:
                    letteres_accepted[index] = letter
                index = index + 1
        else:
            errors = errors + 1
        letter_not_accepted = str(letteres_accepted.count("_"))
        print("Voce acertou as seguintes posicoes {} e faltam {}".format(letteres_accepted, letter_not_accepted))
        ingallows = errors == 6
        accepted = "_" not in letteres_accepted

    if accepted:
        print("Voce ganhou")
    else:
        print("Voce perdeu")
    print('Fim de jogo')


if __name__ == '__main__':
    game()
