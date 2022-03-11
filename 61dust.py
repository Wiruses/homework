#!/usr/bin/env python3
# 61dust.py
import sys
import argparse
import mcb185
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library
parser = argparse.ArgumentParser(description= 'low entropy regions')
parser.add_argument('--fasta',required = True, type = str,
	metavar = "<str>", help = 'enter fasta file')
parser.add_argument('--ws',required = True, type = int,
	metavar = "<str>", help = 'enter window size')
parser.add_argument('--et',required = True, type = float,
	metavar = "<str>", help = 'enter entropy threshold')
parser.add_argument('--lowercase',action = 'store_true',
	help = "lowercase masking")
arg = parser.parse_args()

for name,seq in mcb185.read_fasta(arg.fasta):
	lowent = list(seq)
	#print(lowent[:25])
	#sys.exit()
	for i in range(len(seq) - arg.ws+1):
		window = seq[i:i + arg.ws]
		if mcb185.hcalc(window) < arg.et:
			if arg.lowercase: lowent[i:i+arg.ws] = list(window.lower())
			else:             lowent[i:i+arg.ws] = ['n'] * arg.ws
		
print(name, "".join(lowent), len(lowent), len(seq))