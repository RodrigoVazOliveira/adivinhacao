def game():
    print('*************************************************************')
    print('***************** Bem vindo ao jogo da forca ****************')
    print('*************************************************************')

    word_secret = "banana"
    letteres_accepted = ["_","_","_","_", "_", "_"]
    ingallows = False
    accepted = False

    print(letteres_accepted)
    while not ingallows and not accepted:
        attemped_letter = input('Por digite uma letra ')
        attemped_letter.strip()
        index = 0
        for letter in word_secret:
            if letter.casefold() == attemped_letter.casefold():
                letteres_accepted[index] = letter
            index = index + 1

        print("Voce acertou as seguintes posicoes: {}".format(letteres_accepted))

    print('Fim de jogo')


if __name__ == '__main__':
    game()
