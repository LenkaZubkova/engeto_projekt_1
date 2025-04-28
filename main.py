"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Zúbková
email: lenka_zubkova@hotmail.com
"""
# Definice textů k analýze
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

# Definice uživatelů a jejich hesel
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Získání uživatelského jména a hesla od uživatele
username = input("username:")
password = input("password:")

# Ověření, zda uživatelské jméno a heslo jsou správné
if username in users and users[username] == password:
    print(40 * "-")
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(40 * "-")

    try:
        # Získání volby textu od uživatele a její převod na celé číslo
        while True:
            # Získání volby textu od uživatele a její převod na celé číslo
            text_choice = input("Enter a number btw. 1 and 3 to select: ")
            if not text_choice.isdigit():
                print("Invalid input, please enter a number between 1 and 3.")
                continue  # Pokračuje na další iteraci smyčky
            text_choice = int(text_choice)
            # Ověření, zda je volba textu v platném rozsahu
            if text_choice < 1 or text_choice > 3:
                print("Invalid choice, please enter a number between 1 and 3.")
            else:
                break  # Platný vstup, ukončí smyčku

        print(40 * "-")
        # Výběr textu na základě volby uživatele
        selected_text = TEXTS[text_choice - 1]
        # Rozdělení textu na jednotlivá slova
        words = selected_text.split()

        # Inicializace statistik
        num_words = 0
        titlecase_words = 0
        uppercase_words = 0
        lowercase_words = 0
        numeric_strings = 0
        sum_numbers = 0
        word_lengths = []

        # Cyklus pro výpočet statistik
        for word in words:
            num_words += 1
            word_lengths.append(len(word))
            if word.istitle():
                titlecase_words += 1
            if word.isupper():
                uppercase_words += 1
            if word.islower():
                lowercase_words += 1
            if word.isdigit():
                numeric_strings += 1
                sum_numbers += int(word)
               
        # Výpis statistik
        print(f"There are {num_words} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_strings} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers}")

        # Výpis tabulky délek slov    
        print(40 * "-")
        print("LEN| OCCURENCES      |NR.")
        print(40 * "-")
        for length in range(1, max(word_lengths) + 1):
            occurrences = word_lengths.count(length)
            if occurrences > 0:
                print(f"{length:3}| {'*' * occurrences:<15} |{occurrences}")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 3.")
else:
    print("unregistered user, terminating the program..")