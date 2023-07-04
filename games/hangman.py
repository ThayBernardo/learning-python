import random
import messages

def raffle_word():
    file = open('words.txt', 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word

def show_corrects_letters(secret_word):
    return ['_' for letter in secret_word]

def ask_kick():
    kick = input('Qual letra? ')
    kick = kick.strip().upper()
    return kick

def correct_kicks(secret_word, kick, corrects_letters):
    index = 0
    for letter in secret_word:
        if kick == letter.upper():
            corrects_letters[index] = letter
        index += 1

def play():
    messages.show_message_welcome()
    secret_word = raffle_word()
    corrects_letters = show_corrects_letters(secret_word)
    print('Palavra: {}'.format(corrects_letters))

    hanged = False
    correct = False
    errors = 0

    while not hanged and not correct:
        kick = ask_kick()

        if kick in secret_word:
            correct_kicks(secret_word, kick, corrects_letters)
        else:
            errors += 1
            messages.dreaw_hangman(errors)

        hanged = errors == 7
        correct = '_' not in corrects_letters

        print('Palavra: {}'.format(corrects_letters))
    
    if correct:
        messages.show_message_win()
    else:
        messages.show_message_loser(secret_word)

if __name__ == '__main__':
    play()