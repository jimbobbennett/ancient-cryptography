ENCRYPTED_PHRASE = '''Dzerw Kzsm mlgvh rm Tsv Clwvyivzpvih gszg nlwvim xibkgloltb lirtrmzgvw znlmt gsv Aizyh, gsv urihg kvlkov gl hbhgvnzgrxzoob wlxfnvmg xibkgzmzobgrx
nvgslwh. Ao-Kszoro dilgv gsv Bllp lu Cibkgltizksrx Mvhhztvh, dsrxs xlmgzrmh gsv urihg fhv lu kvinfgzgrlmh zmw xlnyrmzgrlmh gl orhg zoo klhhryov Aizyrx
dliwh drgs zmw drgslfg eldvoh.
Tsv rmevmgrlm lu gsv uivjfvmxb zmzobhrh gvxsmrjfv uli yivzprmt nlmlzokszyvgrx hfyhgrgfgrlm xrksvih, yb Ao-Krmwr, zm Aizy nzgsvnzgrxrzm,
hlnvgrnv zilfmw AD 800, kilevw gl yv gsv hrmtov nlhg hrtmrurxzmg xibkgzmzobgrx zwezmxv fmgro Wliow Wzi II. Ao-Krmwr dilgv z yllp lm xibkgltizksb
vmgrgovw Rrhzozs ur Ihgrpsizq zo-Mf'znnz (Mzmfhxirkg uli gsv Dvxrksvirmt Cibkgltizksrx Mvhhztvh), rm dsrxs sv wvhxiryvw gsv urihg xibkgzmzobgrx gvxsmrjfvh,
rmxofwrmt hlnv uli klobzokszyvgrx xrksvih, xrksvi xozhhrurxzgrlm, Aizyrx kslmvgrxh zmw hbmgzc, zmw nlhg rnkligzmgob, tzev gsv urihg wvhxirkgrlmh lm uivjfvmxb
zmzobhrh. Hv zohl xlevivw nvgslwh lu vmxrksvinvmgh, xibkgzmzobhrh lu xvigzrm vmxrksvinvmgh, zmw hgzgrhgrxzo zmzobhrh lu ovggvih zmw ovggvi xlnyrmzgrlmh rm
Aizyrx. Am rnkligzmg xlmgiryfgrlm lu Iym Awozm dzh lm hznkov hrav uli fhv lu uivjfvmxb zmzobhrh.
'''

KNOWN_MAPPINGS = {'v': 'e', 't': 'g', 's': 'h', 'g': 't', 'z': 'a', 'l': 'o', 'h': 's', 'f': 'u', 'i': 'r', 'm': 'n', 'y': 'b', 'k': 'p',
                  'x': 'c', 'n': 'm', 'o': 'l', 'u': 'f', 'b': 'y', 'p': 'k', 'a': 'z', 'c': 'x', 'j': 'q', 'r': 'i', 'w': 'd', 'd': 'w',
                  'e': 'v', 'q': 'j'}

def map_letters(letter: chr) -> chr:
    '''
    Returns the substituted character
    '''
    return KNOWN_MAPPINGS[letter] if letter in KNOWN_MAPPINGS else letter


# Loop through the phrase and substitute any letters.
# Leave any characters as they are
decrypted = ''.join(map(map_letters, ENCRYPTED_PHRASE))

print(decrypted)