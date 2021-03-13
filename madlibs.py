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
PARTY      = [
    "federalist", "republican", "liberal", "libertarian", "democrat", "separtist",
    "communist", "imperialist", "xenophobe", "republic",
]
BODYPART   = [
    "privates", "arm", "leg", "head", "toe", "hand", "eyeball", "nose", "earlobe",
    "mouse", "nostril", "humorous", "femur", "ankle", "skull", "gallbladder", "liver",
    "tearduct", "elbow", "bicep", "epidermis", "tricep", "quadricep", "gluteus maximum",
    "chest", "stomache", "belly", "bellybutton", "tongue", "teeth", "fingernail",
    "eyelash", "freckle", "cuticle", "clavicle", "mouth", "teeth", "ear",
]

with open(FILE_NAMES,      'r') as f: names      = f.read().split()
with open(FILE_PLACES,     'r') as f: places     = f.read().split()
with open(FILE_NOUNS,      'r') as f: nouns      = f.read().split()
with open(FILE_VERBS,      'r') as f: verbs      = f.read().split()
with open(FILE_ADJECTIVES, 'r') as f: adjectives = f.read().split()
with open(FILE_ADVERBS,    'r') as f: adverbs    = f.read().split()

def get(thelist):
    return random.choice(thelist)

def get_number():
    if random.randint(0, 1) == 0:
        return str(random.uniform(-1e10, 1e10))
    return str(random.randint(-1000000, 1000000))

lookup = {
    "#RACE":       lambda: get(RACE),
    "#NAME":       lambda: get(names),
    "#PLACE":      lambda: get(places),
    "#NOUN":       lambda: get(nouns),
    "#ADJECTIVE":  lambda: get(adjectives),
    "#ADVERB":     lambda: get(adverbs),
    "#NORTHSOUTH": lambda: get(NORTHSOUTH),
    "#EASTWEST":   lambda: get(EASTWEST),
    "#MAGICTYPE":  lambda: get(MAGICTYPE),
    "#ELEMENT":    lambda: get(ELEMENT),
    "#VERB":       lambda: get(verbs),
    '#NUMBER':     lambda: get_number(),
    '#BODYPART':   lambda: get(BODYPART),
}

def conv_chars(string):
    begin = 0
    i = 0
    accumulate = ""
    while i < len(string):
        if string[i] == '#':
            yield string[begin:i]
            accumulate += '#'
            i += 1
            continue
        
        if accumulate:
            accumulate += string[i]
            if accumulate in lookup.keys():
                yield lookup[accumulate]()
                accumulate = ""
                begin = i + 1
        i += 1
    yield string[begin:]

def conv_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    for subtext in conv_chars(text):
        print(subtext, end='')
    print()

def conv(text):
    conv_chars(text)

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
