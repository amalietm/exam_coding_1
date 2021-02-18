# Given 3 positive integers, find the sum of all numbers between the first two that are a multiple of the third.

A = 4
B = 8
C = 2

for i in range(A,B):
    if i % C == 0:
        print (i)
