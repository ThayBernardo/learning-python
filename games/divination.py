import random
import messages

def choose_the_level(level_int):
    if level_int == 1:
        return 20
    elif level_int == 2:
        return 10
    else:
        return 5

def play():
    messages.show_message_welcome_divination()

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    level_str = input('Defina o nível: ')
    level_int = int(level_str)

    total_attempts = choose_the_level(level_int)

    for round in range(1, total_attempts + 1):
        print("Tentativa {} de {}".format(round, total_attempts))

        kick_str = input('Digite o seu número: ')
        print('Seu número: ', kick_str)
        kick_int = int(kick_str)

        if kick_int < 1 or kick_int > 100:
            print('Você deve digitar um número entre 1 e 100')
            continue

        correct_number = kick_int == secret_number
        bigger         = kick_int > secret_number

        if correct_number:
            print('Você acertou! E fez {} pontos'.format(points))
            break
        else:
            if bigger:
                print('Você errou! Seu chute foi maior que o número secreto.')
            else:
                print('Você errou! Seu chute foi menor que o número secreto.')
            lost_points = abs(secret_number - kick_int)
            points -= lost_points

    print('Fim do jogo!')
    print('O número era {}'.format(secret_number))

if __name__ == '__main__':
    play()