#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# Use a dictionary to count the letters
# Sorting the amino acids by frequency is optional

totaa = 0

filename= sys.argv[1]
def readfasta(filename):
	records = []
	seq =''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) ==0:continue
			if line[0]== '>':
				if seq != '':
					records.append((id,seq))
				words = line.split()
				id = words [0][1:]
				seq=''
			else:
				seq += line.upper()
		records.append((id,seq))
	return records
	
aacount = [0] * 20
alpha = ["W",'C',"H",'M','Y', 'Q', "F",'N','P','T','R','I','D','G',"A",'K','E',"V",'L','S']
for name,seq in readfasta(filename):
	for aa in seq:
		if aa == 'W': aacount[0] += 1
		elif aa == 'C': aacount[1] += 1
		elif aa == 'H': aacount[2] += 1
		elif aa == 'M': aacount[3] += 1
		elif aa == 'Y': aacount[4] += 1
		elif aa == 'Q': aacount[5] += 1
		elif aa == 'F': aacount[6] += 1
		elif aa == 'N': aacount[7] += 1
		elif aa == 'P': aacount[8] += 1
		elif aa == 'T': aacount[9] += 1
		elif aa == 'R': aacount[10] += 1
		elif aa == 'I': aacount[11] += 1
		elif aa == 'D': aacount[12] += 1
		elif aa == 'G': aacount[13] += 1
		elif aa == 'A': aacount[14] += 1
		elif aa == 'K': aacount[15] += 1
		elif aa == 'E': aacount[16] += 1
		elif aa == 'V': aacount[17] += 1
		elif aa == 'L': aacount[18] += 1
		elif aa == 'S': aacount[19] += 1
		else: continue
		totaa +=1
for aa,count in zip(alpha,aacount):
	print(aa,count, count/totaa)

#print(aacount)
"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

