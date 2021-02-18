NATO = {
        'A':'Alpha', 'B':'Bravo','C':'Charlie',
        'D':'Delta', 'E':'Echo', 'F':'Foxtrot',
        'G':'Golf',"H":"Hotel", 'I':'India',
        'J':'Juliet', 'K':'Kilo', 'L':'Lima',
        'M':'Mike', 'N':'November', 'O':'Oscar',
        'P':'Papa', 'Q':'Quebec', 'R':'Romeo',
        'S':'Sierra', 'T':'Tango', 'U':'Uniform',
        'V':'Victor', 'W':'Whiskey', 'X':'Xray',
        'Y':'Yankee', 'Z':'Zulu'}

word = input("Enter a word: ").upper()

result = " "
for letter in word: 
	if letter in NATO.keys():
		word = NATO.get(letter)

		result += word + " "

print(result)
