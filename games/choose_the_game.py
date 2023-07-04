import games.hangman as hangman
import divination

def choose_game():
    print('*' * 33)
    print('*******Escolha o seu jogo!*******')
    print('*' * 33)

    print('(1) Forca (2) Adivinhação')

    chosen_game_str = input('Qual jogo ?')
    chosen_game_int = int(chosen_game_str)

    if chosen_game_int == 1:
        print('Jogando forca')
        hangman.play()
    else:
        print('Jogando adivinhação')
        divination.play()

if __name__ == '__main__':
    choose_game()