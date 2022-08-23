#!/usr/bin/env python3

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

aa = 'ARNDCQEGHILKMFPSTWYV'
print(len(aa)) #20 amino acids

"""
for i in aa:
	for j in aa:
		print(i,j) #printed all combinations
"""

num_combos = 0

for i in range(0, len(aa)):
	for j in range(i+1, len(aa)):
		print(aa[i], aa[j])
		num_combos += 1

print(num_combos)
		
