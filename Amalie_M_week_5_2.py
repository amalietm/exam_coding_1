word = input("enter a word: ").lower()
shift = int(input("enter a number: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
def ceasar(plaintxt, key):
    cipher = " "
    for letters in word:
        if letters == " ":
            cipher += " "
        else:
            for i in range(len(alphabet)):
                if alphabet[i] == letters:
                    cipher += alphabet[(i + key) % 26]
    return cipher
print(ceasar(word, shift))
    
