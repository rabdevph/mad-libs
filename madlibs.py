import sys

from logo import logo
from text import text_libs

print(logo['madlibs'])

# Madlibs data. Keys are id that represents the number of each keyword to replace.
# Value is dictionary containing details of keyword(such as the word itself) and
# used for validation of user input.
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

def run_madlibs():
    """Run the game."""
    print("    (Enter 'q' to quit.)")
    
    # Loop through id and details of the data.
    for id, details in libs.items():
        while True:
            # Ask the user to enter a required keyword.
            user_input = input(f"    {details['category'].title()}: ")
            # End the game when the user enter the 'q' character. 
            if user_input == 'q':
                sys.exit()
            else:
                # If user input is valid, save it with uppercase characters.q
                if details['validation'](user_input):
                    libs[id]['word'] = user_input.upper()
                    break
            # If user input is invalid, inform the user.
            print('    Invalid input.')

    print(logo['title'])
    print(text_libs(libs))

try:
    run_madlibs()
except KeyboardInterrupt:
    sys.exit()
