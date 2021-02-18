# Implement division as a series of subtraction. The program should only deal with integers and report the remainder if there is one.

a = 7
b = 2
count = 0

while a >= b:
    a = a - b
    count += 1

print(count)
print(a) 
