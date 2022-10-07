import sys

from logo import logo
from text import text_libs

print(logo['madlibs'])

# dicitonary for handling data
libs = {
    1: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    2: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    3: {
        'category': 'verb, ending in -ing', 'word': '___', 'validation': str.isalpha
    },
    4: {
        'category': 'verb',  'word': '___', 'validation': str.isalpha
    },
    5: {
        'category': 'plural noun', 'word': '___', 'validation': str.isalpha
    },
    6: {
        'category': 'plural noun', 'word': '___', 'validation': str.isalpha
    },
    7: {
        'category': 'verb, ending in -ing', 'word': '___', 'validation': str.isalpha
    },
    8: {
        'category': 'plural color', 'word': '___', 'validation': str.isalpha
    },
    9: {
        'category': 'plural color', 'word': '___', 'validation': str.isalpha
    },
    10: {
        'category': 'number', 'word': '___', 'validation': str.isdigit
    },
    11: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    12: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    13: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    14: {
        'category': 'number', 'word': '___', 'validation': str.isdigit
    },
    15: {
        'category': 'verb', 'word': '___', 'validation': str.isalpha
    },
    16: {
        'category': 'adjective', 'word': '___', 'validation': str.isalpha
    },
}

print("    (Enter 'q' to quit.)")
for id, details in libs.items():
    # loop through key-value and update the value of word(key)
    # if input is valid(update the dictionary then break out of loop),
    # if not valid then ask the user again for an input
    while True:
        user_input = input(f"    Enter {details['category']}: ")
        if user_input == 'q':
            sys.exit()
        else:
            if details['validation'](user_input):
                libs[id]['word'] = user_input.upper()
                break

        print('    Invalid input.')

print(logo['title'])
print(text_libs(libs))
