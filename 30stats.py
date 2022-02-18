#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

print(sys.argv)
numeros = []
cont = 0
for num in sys.argv[1:]:
	numeros.append(int(num))
numeros.sort()
print(f'minimum: {numeros[0]}')
for i in numeros:
	cont += 1
print(f'count: {cont}')
print(f'maximum: {numeros[4]}')
n = len(numeros)
mean = sum(numeros) / n
print(f'mean:{mean}')
stdev = [(x - mean) ** 2 for x in numeros]#list comprehension
varab = sum(stdev) / n
sqt = varab**0.5
print(f'Std.dev:{sqt}')
print(numeros)
print(n % 2)
if n % 2 == 0:
	midpoint = int(n/2)
	print(midpoint)
	print(f'median:{numeros[midpoint] + numeros[midpoint + 1] / 2.0}')
else:
	midpoint = int(n/2)
	print(f'median:{numeros[midpoint]}')
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
