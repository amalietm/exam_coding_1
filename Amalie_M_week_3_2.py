ay = "ay"
yay = "yay"
consonant = "bcdfghjklmnpqrstvwxz"
vowel = "aeiouy"

word= input("enter a word")
first_letter = word[0]
first_letter = first_letter.lower()
if first_letter in consonant:
    print("first letter is a consonant")
    length_of_word = len(word)
    remove_first_letter = word[1:length_of_word]
    pig_latin = remove_first_letter + first_letter + ay
    print("the word in pig latin is:", pig_latin)
elif first_letter in vowel:
    print("first letter is a vowel")
    pig_latin = word + yay
    print("the word in pig latin is:", pig_latin)
else:
    print("I don´t understand what you have written...")

