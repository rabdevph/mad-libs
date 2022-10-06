# program does not have input validation

from logo import logo
from text import text_libs

print(logo['madlibs'])

libs = {
    'verb_1': '___', 'verb_2': '___', 'verb_3': '___', 'verb_4': '___',
    'plural_noun_1': '___', 'plural_noun_2': '___', 'verb_5': '___', 'plural_color_1': '___',
    'plural_color_2': '___', 'number_1': '___', 'verb_6': '___', 'verb_7': '___',
     'verb_8': '___', 'number_2': '___', 'verb_9': '___', 'adjective_1': '___',
    }

verb_1 = input("    Verb: ")
verb_2 = input("    Verb: ")
verb_3 = input("    Verb(ending with 'ing'): ")
verb_4 = input("    Verb: ")

plural_noun_1 = input("    Plural noun: ")
plural_noun_2 = input("    Plural noun: ")
verb_5 = input("    Verb(ending with 'ing'): ")
plural_color_1 = input("    Plural color: ")

plural_color_2 = input("    Plural color: ")
number_1 = input("    Number: ")
verb_6 = input("    Verb: ")
verb_7 = input("    Verb: ")

verb_8 = input("    Verb: ")
number_2 = input("    Number: ")
verb_9 = input("    Verb: ")
adjective_1 = input("    Adjective: ")

libs['verb_1'] = verb_1.upper()
libs['verb_2'] = verb_2.upper()
libs['verb_3'] = verb_3.upper()
libs['verb_4'] = verb_4.upper()

libs['plural_noun_1'] = plural_noun_1.upper()
libs['plural_noun_2'] = plural_noun_2.upper()
libs['verb_5'] = verb_5.upper()
libs['plural_color_1'] = plural_color_1.upper()

libs['plural_color_2'] = plural_color_2.upper()
libs['number_1'] = number_1.upper()
libs['verb_6'] = verb_6.upper()
libs['verb_7'] = verb_7.upper()

libs['verb_8'] = verb_8.upper()
libs['number_2'] = number_2.upper()
libs['verb_9'] = verb_9.upper()
libs['adjective_1'] = adjective_1.upper()

print(logo['title'])
print(text_libs(libs))
