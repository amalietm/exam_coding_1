#Start with 4 words “comfortable”, “round”, “support”, “machinery”, return a list of all possible 2 word combinations

from itertools import combinations 

comb = combinations(["comfortable", "round", "support", "machinery"], 2)

for i in list(comb):
   print i 

