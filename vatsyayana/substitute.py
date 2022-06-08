'''
A Python file that encrypts text using the Vatsyayana cipher
'''

# Define the alphabet
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

# The substitution alphabet is the reverse of the alphabet
SUBSTITUTION_ALPHABET= ALPHABET[::-1]

# Create a dictionary of substituted letters
SUBSTITUTIONS = dict(zip(SUBSTITUTION_ALPHABET, ALPHABET))

# Get the phrase
phrase = input('Enter phrase to encrypt or decrypt: ').lower()

# Define a function to substitute each letter
def substitute(letter: chr) -> chr:
    '''
    Returns the substituted character
    '''
    return SUBSTITUTIONS[letter] if letter in SUBSTITUTIONS else letter

# Loop through the phrase and substitute any letters.
# Leave any characters as they are
substituted = ''.join(map(substitute, phrase))

# Print the result
print('Converted phrase is:')
print(substituted)
