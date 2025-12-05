

def create_acronym(phrase):
    # 1. Remove leading and trailing spaces
    phrase = phrase.strip()

    # 2. Split phrase into words
    words = phrase.split()

    # 3. Take the first letter of each word, uppercase it
    letters = []
    for w in words:
        letters.append(w[0].upper())

    # 4. Join letters together with no separator
    acronym = "".join(letters)

    return acronym

print(create_acronym("for your information"))
# FYI

print(create_acronym("   national aeronautics and space administration   "))
# NASA

print(create_acronym("laughing out loud"))
# LOL
