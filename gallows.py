def game():
    print('*************************************************************')
    print('***************** Bem vindo ao jogo da forca ****************')
    print('*************************************************************')

    word_secret = "banana"
    ingallows = False
    accepted = False

    while not ingallows and not accepted:
        attemped_letter = input('Por digite uma letra ')
        attemped_letter.strip()
        index = 0
        for letter in word_secret:
            if letter.casefold() == attemped_letter.casefold():
                print("Encontrei a letra {}  na posicao {}".format(letter, index))
            index = index + 1

    print('Fim de jogo')


if __name__ == '__main__':
    game()
