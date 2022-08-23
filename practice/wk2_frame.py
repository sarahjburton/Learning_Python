#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

#single loop

for i in range(0,len(dna)):
	print(i, dna[i])
	
	
#nested loop

for i in range(0,len(dna),3):
	for j in range(0,3):
		c = i + j
		print(c, j, dna[c])
