#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

for pos in range(len(dna)):
	print(pos, end  = ' ')
	if (pos+1) % 2 ==0: print(1, end =' ')
	elif(pos+1) % 3 ==0: print(2, end =' ')
	else: print(0,end=' ')
	print(dna[pos])


"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
