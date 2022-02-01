#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'[:: -1]# splicing  -1 reads it backwards

for i in range (len(dna)):
	if dna[i] == 'A': print('T', end='') # printing out the complement
	elif dna[i] == 'T': print('A', end='')
	elif dna[i] == 'G': print('C', end='')
	else: print('G', end='')
print()#makes new line
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
