#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
gcount = 0
for i in range (len(dna)):
	if dna[i] == "C" or dna[i] == "G": gcount += 1
gc = gcount/len(dna)
print(f'{gcount/len(dna):.2f}')
print('%.2f' % (gc))
print('{:.2f}'.format(gc))
	
	
	
"""
python3 21gc.py
0.42
0.42
0.42
"""
