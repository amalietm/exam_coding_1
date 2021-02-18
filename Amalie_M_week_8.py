from sys import argv
from Levenshtein import distance

args = argv[1:]
inn = ""
out = ""
dictio = ""
wordList = []
words = []
total = 0

for key, value in enumerate(args):
    if value == "-i":
        inn = args[key + 1]
    if value == "-0":
        out = args[key + 1]
    if value == "-d":
        dictio = args[key + 1]
with open(dictio, mode = "r") as dictionary:
    for line in dictionary:
        wordList.append((line).strip())

with open(inn, mode = "r") as input:
    print("changelog: ")
    for line in input:
        if not line.strip():
            words.append("")
        else:
            linewords = line.strip().split(" ")
            linewordsOut = []
            for word in linewords:
                if word.strip():
                    minDist = 100
                    replacer = ""
                for entry in wordList:
                    l_distance = distance(word.lower(), entry.lower())

                    if l_distance == 0:
                        replacer = entry
                        break
                    
                    if l_distance< minDist:
                        minDist = l_distance
                        replacer = entry

                if distance(word, replacer) > 0:
                    print(
                        str(distance(word, replacer)) + ":" + word + "=>" + replacer
                    )
                    total += 1
                linewordsOut.append(replacer)
            words.append(" ".join(linewordsOut))

with open(out, mode = "w") as output:
    output.write("\n".join(words))
print(str(total) + " words corrected")
                    
