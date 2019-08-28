#!/usr/bin/env python3

"""to run ./binarySearch.py <genome annotation file>"""

import sys

protein_coding_gene_locations = []

for i, line in enumerate(open(sys.argv[1])):
    columns =  line.rstrip("\n").split()
    if columns[0] == "3R" and columns[2] == "gene" and "protein_coding" in line:
        protein_coding_gene_locations.append(columns[3])
        protein_coding_gene_locations.append(columns[4])

protein_coding_gene_locations_sorted = sorted(protein_coding_gene_locations)

n = len(protein_coding_gene_locations_sorted)
count = 0
while n > 20:
    if 21378950 > int(protein_coding_gene_locations_sorted[int(n/2)]):
        protein_coding_gene_locations_sorted = protein_coding_gene_locations_sorted[int(n/2):]
    elif 21378950 < int(protein_coding_gene_locations_sorted[int(n/2)]):
        protein_coding_gene_locations_sorted = protein_coding_gene_locations_sorted[:int(n/2)]
    n = int(n/2)
    count += 1
 
locations = []    
locations[:20] = protein_coding_gene_locations_sorted
for i, line in enumerate(open(sys.argv[1])):
    columns =  line.rstrip("\n").split()
    if columns[0] == "3R" and columns[2] == "gene" and "protein_coding" in line:
        for i in locations:
            if i in line:
                distance = abs(21378950-int(i))
                print("A gene close to 3R:21,378,950 is " + str(columns[13]) + " and is " + str(distance) + " nucleotides away from the mutation.")
           
           
print("It took " + str(count) + " iterations to find the nearest genes.")
        
        
    
 
        
        
    