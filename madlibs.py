from sys import argv
import random
import re

FILE_NAMES      = 'names.txt'
FILE_PLACES     = 'places.txt'
FILE_NOUNS      = 'SimpleWordlists/Wordlist-Nouns-All.txt'
FILE_VERBS      = 'SimpleWordlists/Wordlist-Verbs-All.txt'
FILE_ADJECTIVES = 'SimpleWordlists/Wordlist-Adjectives-Common-Audited-Len-3-6.txt'
FILE_ADVERBS    = 'SimpleWordlists/Wordlist-Adverbs-All.txt'

RACE       = ['human', 'elf', 'dwarf']
NORTHSOUTH = ['north', 'south']
EASTWEST   = ['east', 'west']
MAGICTYPE  = ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation']
ELEMENT    = ['Air', 'Earth', 'Fire', 'Water', 'Void', 'Ice']
FIGHT      = ['alongside the people', 'alongside the Elite', 'using distance']
PARTY      = ['Loyalist', 'Separatists']
BATTLE     = ['present, and I #VERBED',
              'not present and I #VERBED. During the siege of Martnya I was #VERBED',
              'not present and I #VERBED. During the battle of Pendremic I #VERBED']
SINCE      = ['my troops',
              'my martial skill',
              'culture and Technology',
              'the economy',
              'politics',
              'magic abilities and religion']

with open(FILE_NAMES,      'r') as f: names      = f.read().split()
with open(FILE_PLACES,     'r') as f: places     = f.read().split()
with open(FILE_NOUNS,      'r') as f: nouns      = f.read().split()
with open(FILE_VERBS,      'r') as f: verbs      = f.read().split()
with open(FILE_ADJECTIVES, 'r') as f: adjectives = f.read().split()
with open(FILE_ADVERBS,    'r') as f: adverbs    = f.read().split()
def get(thelist):
    return random.choice(thelist)

lookup = {
    "#RACE":       lambda: get(RACE),
    "#NAME":       lambda: get(names),
    "#PLACE":      lambda: get(places),
    "#NOUN":       lambda: get(nouns),
    "#NOUNS":      lambda: get(nouns) + "s",
    "#ADJECTIVE":  lambda: get(adjectives),
    "#ADVERB":     lambda: get(adverbs),
    "#NORTHSOUTH": lambda: get(NORTHSOUTH),
    "#EASTWEST":   lambda: get(EASTWEST),
    "#MAGICTYPE":  lambda: get(MAGICTYPE),
    "#ELEMENT":    lambda: get(ELEMENT),
    "#PARTY":      lambda: get(PARTY),
    "#FIGHT":      lambda: get(FIGHT),
    "#VERBING":    lambda: get(verbs) + 'ing',
    "#VERB":       lambda: get(verbs),
    "#VERBED":     lambda: get(verbs) + 'ed',
    "#BATTLE":     lambda: get(BATTLE),
    "#SINCE":      lambda: get(SINCE),
}

def conv_split(words, show=False):
    for i, word in enumerate(words):
        cleaned =  '#' + re.sub(r'\W+', '', word)
        if cleaned in lookup.keys():
            words[i] = word.replace(cleaned, lookup[cleaned]())
        if '.' in words[i] or '?' in words[i]:
            words[i] += '\n'

    if show:
        print(" ".join(words))
    else:
        with open('out.txt', 'w') as f:
            f.write(" ".join(words))

def conv_file(filename):
    words = []
    with open(filename, 'r') as f:
        words = f.read().split()
    conv_split(words)

def conv(text):
    conv_split(text.split(), show=True)

if len(argv) != 3:
    print("""
Usage: python madlibs.py [OPTIONS] <input>

OPTIONS:
    f       The text of file 'input' is read,
            otherwise the text itself
            'input' itself is read.
""")
    exit(1)

if argv[1] == 'f':
    conv_file(argv[2])
else:
    conv(argv[2])
