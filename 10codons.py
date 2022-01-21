#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

# your code goes here
#trial2
k = 3
for i in range(0,len(dna) -k+1,3) :
	print(dna[i:i+k])
print( "- end of trial2")
"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
