#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here
x = 0
y = 1
for i in range(1,(n+1)):
	x += i
	y *= i
print(i, x, y)



"""
python3 11sumfac.py
5 15 120

"""
