
def translate(phrase):
    letter1 = input("Enter the letter which all the vocals will turn on: ")
    letter2 = input("Enter the letter which all the r will be changed: ")
    translation2 = ""
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + letter1
        else:
            translation = translation + letter
    for letter in translation:
        if letter in "Rr":
            translation2 = translation2 + letter2
        else:
            translation2 = translation2 + letter
    return translation2

print(translate(input("")))
