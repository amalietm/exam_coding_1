# Given a string of text, print the number of times each letter in the alphabets a-z appear. Hint: “a” != “A”.2.

some_text = "Hello world"


alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets: 
    count = 0
    for i in some_text.lower():
        if i == alphabet: 
            count += 1
			
    print(alphabet + " = " + str(count)) 

