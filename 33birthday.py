#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is
import sys
import random
stud = 23
days = 365
trials = 10000
mult = 0

#create empty calendar
calendar =[0]* days

# fill calendar with birthdays
for i in range(trials):
	calendar =[0]* days
	for j in range(stud):
		r = random.randint(0,days - 1)
		#print(r)
		calendar[r] += 1
		if calendar[r] > 1:
			mult += 1
			break
print(mult/trials)

# fill calendar with birthdays

# determine if shared bday
	

"""
y = 10
dupes = 0
bday = random.randint(1,y)# produces one number between 1 and y
print(bday)
for i in range(1,6):# each i is one of 5 students,
	for b in range(random.randint(1,y)):
		dupes = i+b
		print(dupes,i)
		

#for i in range(bday):# produces a list of numbers bday length long
	#print(i)
	#for j in range(1,7):
		#if i == j: dupes +=1
		#print(i,j,dupes)

"""
"""
python3 33birthday.py
0.571
"""

