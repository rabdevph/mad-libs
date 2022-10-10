import sys
import re

from logo import logo
from text import libs


def replace_keyword(key_word, new_key_word, text):
    """Find and replace keyword with new one."""
    old_keyword = re.compile(fr'{key_word}')
    new_text = old_keyword.sub(new_key_word.upper(), text, count=1)

    return new_text


print(logo['madlibs'])

# Load content from other module
content = libs['laundry']

# Make a regular expression for the keywords
find_keyword = re.compile(
    r'VERB|GERUND VERB|PLURAL NOUN|PLURAL COLOR|NUMBER|ADJECTIVE')

# Store all the matches in a list.
found_keywords = find_keyword.findall(content)

# Loop through found keywords, then ask the user
# for an input to replace the keywords.
for i, keyword in enumerate(found_keywords):
    while True:
        new_keyword = input(f"{keyword}: ")
        # Quit program when user input 'q' or 'Q'.
        if new_keyword.upper() == 'Q':
            sys.exit()
        else:
            # Check keyword for input validation(string or digit).
            if (keyword in found_keywords) and (keyword != 'NUMBER') and (new_keyword.isalpha()):
                content = replace_keyword(keyword, new_keyword, content)
                break
            elif (keyword in found_keywords) and (keyword == 'NUMBER') and (new_keyword.isdigit()):
                content = replace_keyword(keyword, new_keyword, content)
                break
        # Input is invalid.
        print('Invalid input.')


print(logo['title'])
print(content)
