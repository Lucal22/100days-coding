alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Welcome to the Caesar Cipher')


def newCipher():
    again = input('Do you want to do it again(yes/no)?\n')[:1]
    if again == 'y':
        cipher()


def cipher():

    def cipher_word(message, number, direction):
        new_word = ''

        for letter in message:
            index = alphabet.index(letter)
            if direction == 'decode':
                number *= -1
            new_position = index + number
            new_word += alphabet[new_position]

        print(new_word)

    method = input('Do you want to encode or decode a message?\n')
    message = input('Type the message:\n')
    number = int(input('Type the shift number:\n'))

    if method != 'encode' and method != 'decode':
        print('error')

    cipher_word(message, number, method)

    newCipher()


cipher()
