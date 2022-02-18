#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random


size = int(sys.argv[1])
num  = int(sys.argv[2])
rlen = int(sys.argv[3])

chromo = [0] * size
print(size, num, rlen)

for i in range(num):
	r = random.randint(0, size - rlen)
	print(i,r)
	for j in range(r, r + rlen):
		chromo[j] += 1
print(chromo)
sums = 0.0
for n in chromo:
	sums += n
print(sums,float(sums/size))




"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
