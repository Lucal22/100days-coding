import random

from stages import stages

from words import word_list

end_game = False
errors = 6

word = random.choice(word_list)

print('Bem vindos ao jogo da forca!')

hidden_word = []

for letters in word:
    hidden_word += ['_']


while end_game == False:

    letter = input('Digite uma letra: ')[:1].lower()

    if letter not in word:
        errors -= 1
        print(stages[errors])

    for position in range(len(word)):
        letters = word[position]
        if letter == letters:
            hidden_word[position] = letter

    print(hidden_word)

    if '_' not in hidden_word:
        print('Parabéns!!')
        end_game = True

    if errors == 0:
        print(f'Fim de jogo a palavra era: {word}.')
        end_game = True
