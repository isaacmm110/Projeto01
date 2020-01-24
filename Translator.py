
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "u"
        else:
            translation = translation + letter
    return translation


print(translate(input(" ")))
