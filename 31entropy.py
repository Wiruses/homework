#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys


if len(sys.argv) == 1:
	print("numbers only please")
	sys.exit()
	
proba=[]
summ = 0
toler = 0.01
for i in range(1,len(sys.argv)):
	proba.append(float(sys.argv[i]))
	summ += float(sys.argv[i])
if abs(sum-1.0) > toler:
	print("probability does not sum to 1")
	sys.exit()
entropy = 0
for p in proba:
	entropy += -1 *prb*math.log2(prb)
print('{:.3f}'.format(entropy))
"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
