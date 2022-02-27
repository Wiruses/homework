#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix
"""
filename = sys.argv[1]
def read_fasta(filename):
	ids =[]
	seqs = []
	seq = ''
	with open(filename) as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if line[0] == '>':
				words = line.split()
				ids.append(words[0][1:])
				if seq != '': seqs.append(seq)
				seq = ''
			else: seq += line
		seqs.append(seq)
	return ids, seqs
ids,seqs = read_fasta(filename)
for aid,seq in zip(ids, seqs):
	print(aid, seq)

"""
seqs=[]
names=[]
hyd=0

Ic = 4.5
Vc = 4.2
Lc = 3.8
Fc = 2.8
Cc = 2.5
Mc = 1.9
Ac = 1.8
Gc = -0.4
Tc = -0.7
Sc = -0.8
Wc = -0.9
Yc = -1.3
Pc = -1.6
Hc = -3.2
Ec = -3.5
Qc = -3.5
Dc = -3.5
Nc = -3.5
Kc = -3.9
Rc = -4.5


with open(sys.argv[1]) as pp:
	seq = ""
	for line in pp.readlines():
		if line[0] ==">":
			seqs.append(seq)
			names.append(line.rstrip())
			seq = ""
		else:seq += line.rstrip()
seqs= seqs[1:]		
#print(seqs[3],names[3])
for seq, name in zip(seqs,names):
	#print(seq[:30])
	for e in range(0,30 - 8 +1):
		#print(seq[e:e + 8])
		wind = seq[e:e + 8]
		score = 0
		for aa in wind:
			if aa == "M":  score += Mc
			elif aa == "V":  score += Vc
			elif aa == "I":  score += Ic
			elif aa == "F":  score += Fc
			elif aa == "C":  score += Cc
			elif aa == "A":  score += Ac
			elif aa == "G":  score += Gc
			elif aa == "T":  score += Tc
			elif aa == "S":  score += Sc
			elif aa == "W":  score += Wc
			elif aa == "Y":  score += Yc
			elif aa == "P":  score += Pc
			elif aa == "H":  score += Hc
			elif aa == "E":  score += Ec
			elif aa == "Q":  score += Qc
			elif aa == "D":  score += Dc
			elif aa == "N":  score += Nc
			elif aa == "K":  score += Kc
			elif aa == "R":  score += Rc
			elif aa == "L":  score += Lc
			else: 
				score = 0 
				break
		if score == 0: continue
		score /= 8
		if score > 2.5:
			print(name)
			break
	for r in range(30,len(seq) - 11 + 1):
		wind = seq[e:e + 11]
		score = 0
		for aa in wind:
			if aa == "M":  score += Mc
			elif aa == "V":  score += Vc
			elif aa == "I":  score += Ic
			elif aa == "F":  score += Fc
			elif aa == "C":  score += Cc
			elif aa == "A":  score += Ac
			elif aa == "G":  score += Gc
			elif aa == "T":  score += Tc
			elif aa == "S":  score += Sc
			elif aa == "W":  score += Wc
			elif aa == "Y":  score += Yc
			elif aa == "P":  score += Pc
			elif aa == "H":  score += Hc
			elif aa == "E":  score += Ec
			elif aa == "Q":  score += Qc
			elif aa == "D":  score += Dc
			elif aa == "N":  score += Nc
			elif aa == "K":  score += Kc
			elif aa == "R":  score += Rc
			elif aa == "L":  score += Lc
			else: 
				score = 0 
				break
		if score == 0: continue
		score /= 11
		if score > 2.0:
			print(name)
			break
"""
# to make score
	for seq, name in zip(seqs,names):
		print(seq[:30])
		for e in range(0,30 - 8 +1):
			aa = seq[e].count('I')
			print(seq[e:e + 8], aa)
"""
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
