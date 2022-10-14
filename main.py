import json
from difflib import get_close_matches as gcm

data_base = json.load(open('dictionary_compact.json'))
word = input('Enter a word: ').lower()
matches = gcm(word, data_base.keys())

def main(x):
    if x in data_base:
        return data_base[x]
    elif len(matches) > 0:
        new_word = input(f"Word not found! Try these: {matches} : ").lower()
        return data_base[new_word]
    else:
        return "Word doesn't exist"

print(main(word))      
