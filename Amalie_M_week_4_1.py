# Write a program that given a list of numbers, multiply all numbers in the list. Bonus for ignoring non-number element.

my_list = [3, 4, "B", 2,"car", "!"]

my_list =  [x for x in my_list if type(x) == int]

product = 1
for number in my_list:
	product = product * number 

print(product)


#import math

#numbers = [3, 5, 6, 8, 2, 1]

#result = math.prod(numbers)
#print(numbers)
#print("the sum of all numbers multiplied is: ", result)
    

