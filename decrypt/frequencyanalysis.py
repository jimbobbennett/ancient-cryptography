'''
Makes an attempt to decrypt text encrypted by a substitution cipher
'''

# The encrypted phrase
import string
ENCRYPTED_PHRASE = """gsv vziorvhg pmldm fhv lu xibkgltizksb rh ulfmw rm mlm-hgzmwziw srviltobksh xzievw rmgl gsv dzoo lu z glny uiln gsv low prmtwln lu vtbkg xrixz 1900 yx. 
gsvhv ziv mlg gslftsg gl yv hvirlfh zggvnkgh zg hvxivg xlnnfmrxzgrlmh, sldvevi, yfg izgsvi gl szev yvvm zggvnkgh zg nbhgvib, rmgirtfv, li vevm znfhvnvmg uli orgvizgv lmollpvih.
hlnv xozb gzyovgh uiln nvhlklgznrz hlnvdszg ozgvi ziv xovziob nvzmg gl kilgvxg rmulinzgrlm—lmv wzgvw mvzi 1500 yx dzh ulfmw gl vmxibkg z xizughnzm'h ivxrkv uli klggvib tozav, 
kivhfnzyob xlnnvixrzoob ezofzyov. ufigsvinliv, svyivd hxslozih nzwv fhv lu hrnkov nlmlzokszyvgrx hfyhgrgfgrlm xrksvih (hfxs zh gsv zgyzhs xrksvi) yvtrmmrmt kviszkh zilfmw 600 gl 500 yx.
rm rmwrz zilfmw 400 yx gl 200 zw, novxxsrgz erpzokz li "gsv zig lu fmwvihgzmwrmt dirgrmt rm xbksvi, zmw gsv dirgrmt lu dliwh rm z kvxforzi dzb" dzh wlxfnvmgvw rm gsv pznz hfgiz uli gsv
kfiklhv lu xlnnfmrxzgrlm yvgdvvm olevih. gsrh dzh zohl orpvob z hrnkov hfyhgrgfgrlm xrksvi. kzigh lu gsv vtbkgrzm wvnlgrx tivvp nztrxzo kzkbir dviv dirggvm rm z xbksvi hxirkg.
gsv zmxrvmg tivvph ziv hzrw gl szev pmldm lu xrksvih. gsv hxbgzov gizmhklhrgrlm xrksvi dzh fhvw yb gsv hkzigzm nrorgzib, yfg rg rh mlg wvurmrgrevob pmldm dsvgsvi gsv hxbgzov
dzh uli vmxibkgrlm, zfgsvmgrxzgrlm, li zelrwrmt yzw lnvmh rm hkvvxs. svilwlgfh gvooh fh lu hvxivg nvhhztvh ksbhrxzoob xlmxvzovw yvmvzgs dzc lm dllwvm gzyovgh li zh z gzggll lm
z hozev'h svzw xlmxvzovw yb ivtildm szri, zogslfts gsvhv ziv mlg kilkviob vcznkovh lu xibkgltizksb kvi hv zh gsv nvhhztv, lmxv pmldm, rh wrivxgob ivzwzyov; gsrh rh pmldm zh hgvtzmltizksb.
zmlgsvi tivvp nvgslw dzh wvevolkvw yb klobyrfh (mld xzoovw gsv "klobyrfh hjfziv"). gsv ilnzmh pmvd hlnvgsrmt lu xibkgltizksb (v.t., gsv xzvhzi xrksvi zmw rgh ezirzgrlmh)."""

print(ENCRYPTED_PHRASE)

# The frequency of letters in the English language
LETTER_FREQUENCY = {
    'a': 8.2,
    'b': 1.5,
    'c': 2.8,
    'd': 4.3,
    'e': 13,
    'f': 2.2,
    'g': 2,
    'h': 6.1,
    'i': 7,
    'j': 0.15,
    'k': 0.77,
    'l': 4,
    'm': 2.4,
    'n': 6.7,
    'o': 7.5,
    'p': 1.9,
    'q': 0.095,
    'r': 6,
    's': 6.3,
    't': 9.1,
    'u': 2.8,
    'v': .98,
    'w': 2.4,
    'x': 0.15,
    'y': 2,
    'z': 0.074
}


def get_letter_counts_for_text(text: str) -> dict:
    '''
    Creates a dictionary of letter counts for a given string
    '''

    # Get a dictionary of lower case letters with a 0 value
    letter_counts = dict(zip(string.ascii_letters, [0]*26))

    # Loop through all the characters in the text
    for letter in text:
        # If the letter is a letter, not a space or special character, count it
        if letter in letter_counts:
            # Increase the count of the letter
            letter_counts[letter] = letter_counts[letter] + 1

    # Return the counts
    return letter_counts


# Get the letter counts
phrase_letter_frequency = get_letter_counts_for_text(ENCRYPTED_PHRASE)


def get_digraph_counts(text: str) -> dict:
    '''
    Counts the digraphs in the text
    '''
    digrahps = {}
    for i in range(0, len(text)-1):
        if text[i].isalpha() and text[i+1].isalpha():
            digraph = text[i] + text[i+1]
            if digraph in digrahps:
                digrahps[digraph] = digrahps[digraph] + 1
            else:
                digrahps[digraph] = 1

    return digrahps


digraph_counts = get_digraph_counts(ENCRYPTED_PHRASE)
sorted_digraph_counts = dict(
    sorted(digraph_counts.items(), key=lambda i: i[1], reverse=True))

print(sorted_digraph_counts)

# print(phrase_letter_frequency)

# Sort both the letter counts and frequencies by their values - guess at a equivalent
# frequency order as a first pass
sorted_letter_frequency = dict(
    sorted(LETTER_FREQUENCY.items(), key=lambda i: i[1], reverse=True))
sorted_phrase_letter_frequency = dict(
    sorted(phrase_letter_frequency.items(), key=lambda i: i[1], reverse=True))

mapping = dict(zip(sorted_phrase_letter_frequency.keys(),
               sorted_letter_frequency.keys()))

# print(mapping)

KNOWN_MAPPINGS = {
    'v': 'e',
    't': 'g',
    's': 'h',
    'g': 't',
    'z': 'a',
    'l': 'o',
    'h': 's',
    'f': 'u',
    'i': 'r',
    'm': 'n',
    'y': 'b',
    'k': 'p',
    'x': 'c',
    'n': 'm',
    'o': 'l',
    'u': 'f',
    'b': 'y',
    'p': 'k',
    'a': 'z',
    'c': 'x',
    'j': 'q'
}

for k in KNOWN_MAPPINGS.keys():
    del sorted_phrase_letter_frequency[k]

for k in KNOWN_MAPPINGS.values():
    del sorted_letter_frequency[k]

mapping = KNOWN_MAPPINGS | dict(
    zip(sorted_phrase_letter_frequency.keys(), sorted_letter_frequency.keys()))

print(mapping)

def map_letters(letter: chr) -> chr:
    '''
    Returns the substituted character
    '''
    return mapping[letter] if letter in mapping else letter


# Loop through the phrase and substitute any letters.
# Leave any characters as they are
decrypted = ''.join(map(map_letters, ENCRYPTED_PHRASE))

print(decrypted)
