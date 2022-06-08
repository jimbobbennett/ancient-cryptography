'''
A Python file that encrypts text using the Caesar cipher
'''

# Get the phrase
phrase = input('Enter phrase to encrypt or decrypt: ').lower()

# Get the amount to shift
shift_amount = int(input('How far do you want to shift? '))

def shift(letter: chr) -> chr:
    '''
    Shifts a letter by the given shift, wrapping around where necessary
    '''
    # Convert the letter to ASCII
    letter_number = ord(letter)

    # If the letter is not a letter, return as is
    if letter_number < ord('a') or letter_number > ord('z'):
        return letter

    # Shift the ASCII by the given shift to get the shifted letter
    letter_number += shift_amount

    # If we have shifted past Z, then we need to wrap around
    if letter_number > ord('z'):
        letter_number -= 26
    elif letter_number < ord('a'):
        letter_number += 26

    # Convert the ASCII value back to a character
    return chr(letter_number)

# Loop through the phrase and shift any letters.
# Leave any characters as they are
shifted = ''.join(map(shift, phrase))

# Print the result
print('Converted phrase is:')
print(shifted)
