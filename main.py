"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Zúbková
email: lenka_zubkova@hotmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

username = input("username:")
password = input("password:")

if username in users and users[username] == password:
    print(40 * "-")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(40 * "-")

    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice < 1 or text_choice > 3:
        print("Invalid choice, terminating the program..")
    else:
        print(40 * "-")
        selected_text = TEXTS[text_choice - 1]
        words = selected_text.split()
        num_words = len(words)
        titlecase_words = sum(1 for word in words if word.istitle())
        uppercase_words = sum(1 for word in words if word.isupper())
        lowercase_words = sum(1 for word in words if word.islower())
        numeric_strings = sum(1 for word in words if word.isdigit())
        sum_numbers = sum(int(word) for word in words if word.isdigit())
           
        print(f"There are {num_words} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_strings} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers}")
            
        word_lengths = [len(word) for word in words]
        print(40 * "-")
        print("LEN| OCCURENCES      |NR.")
        print(40 * "-")
        for length in range(1, max(word_lengths) + 1):
            occurrences = word_lengths.count(length)
            if occurrences > 0:
                print(f"{length:3}| {'*' * occurrences:<15} |{occurrences}")
else:
    print("unregistered user, terminating the program..")
