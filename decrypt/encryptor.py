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
phrase = '''David Kahn notes in The Codebreakers that modern cryptology originated among the Arabs, the first people to systematically document cryptanalytic
methods. Al-Khalil wrote the Book of Cryptographic Messages, which contains the first use of permutations and combinations to list all possible Arabic
words with and without vowels.
The invention of the frequency analysis technique for breaking monoalphabetic substitution ciphers, by Al-Kindi, an Arab mathematician,
sometime around AD 800, proved to be the single most significant cryptanalytic advance until World War II. Al-Kindi wrote a book on cryptography
entitled Risalah fi Istikhraj al-Mu'amma (Manuscript for the Deciphering Cryptographic Messages), in which he described the first cryptanalytic techniques,
including some for polyalphabetic ciphers, cipher classification, Arabic phonetics and syntax, and most importantly, gave the first descriptions on frequency
analysis. He also covered methods of encipherments, cryptanalysis of certain encipherments, and statistical analysis of letters and letter combinations in
Arabic. An important contribution of Ibn Adlan was on sample size for use of frequency analysis.
'''

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
