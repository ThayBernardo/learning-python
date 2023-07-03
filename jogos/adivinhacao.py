print('*' * 33)
print('Bem vindo ao jogo de adivinhação!')
print('*' * 33)

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input('Digite o seu número: ')
    print('Seu número: ', chute_str)
    chute_int = int(chute_str)

    if chute_int < 1 or chute_int > 100:
        print('Você deve digitar um número entre 1 e 100')
        continue

    acertou   = chute_int == numero_secreto
    maior     = chute_int > numero_secreto

    if acertou:
        print('Você acertou!')
        break
    else:
        if maior:
            print('Você errou! Seu chute foi maior que o número secreto.')
        else:
            print('Você errou! Seu chute foi menor que o número secreto.')

print('Fim do jogo!')

