#!/usr/bin/env python3
"""Usage: ./back_to_nucleotides.py <sequence file> <protein alignment> """
import sys
from fasta import FASTAReader
import numpy as np
import matplotlib.pyplot as plt 

sequences = FASTAReader(open(sys.argv[1]))
proteins = FASTAReader(open(sys.argv[2]))
my_sequences = []
protein_alignments = []
dna_with_gaps = []

for ident, sequence in sequences:
   my_sequences.append(sequence)
   
for ident, protein_seqs in proteins:
    protein_alignments.append(protein_seqs)
    
for sequence, protein in zip(my_sequences, protein_alignments):   
    gap_dna = ""
    bp_pos = 0
    for num, a in enumerate(protein):
        if a == "-":
            gap_dna = gap_dna + "---"
        else:
            gap_dna = gap_dna + sequence[bp_pos:bp_pos+3]
            bp_pos += 3
    dna_with_gaps.append(gap_dna)
    
codons = {
     "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
     "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
     "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
     "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
     "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
     "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
     "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
     "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
     "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
     "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
     "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
     "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
     "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
     "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
     "TAC":"Y", "TAT":"Y", "TAA":"", "TAG":"",
     "TGC":"C", "TGT":"C", "TGA":"_", "TGG":"W"}
     
rest_of_dna = dna_with_gaps[1:]
query = dna_with_gaps[0]
dS_vals=[]
dN_vals=[]


    
for i in range(0, (len(query)), 3):
    dS = 0
    dN = 0
    # print(query[i:i+3])
    if query[i:i+3] == '---':
        continue

    for sequence in rest_of_dna:
        if sequence[i:i+3] == '---':
            continue
        if sequence[i:i+3] not in codons:
            continue
        if query[i:i+3] != sequence[i:i+3] and codons[query[i:i+3]] == codons[sequence[i:i+3]]:
            dS += 1
        if query[i:i+3] != sequence[i:i+3] and codons[query[i:i+3]] != codons[sequence[i:i+3]]:
            dN += 1

    dS_vals.append(dS)
    dN_vals.append(dN)
    
D = []
for i in range(len(dS_vals)):
    D_val = dS_vals[i] - dN_vals[i]
    D.append(D_val)

# print(D)

stdev = np.std(D)
# print(stdev)

mean = sum(D)/len(D)
# print(mean)

z_scores = []
for difference in D:
    z_val = difference/stdev
    z_scores.append(z_val)

print(z_scores)

significant = []
for index,z in enumerate(z_scores):
    if z < -1.645 or z > 1.645:
        significant.append(index)

color_list=[]
for count, i in enumerate(dS_vals):
    if count not in significant:
        color_list.append('#4363d8')
    else:
        color_list.append('#e6194b')

print(len(significant))
print(len(dS_vals))

ratios=[]
for dS, dN in zip(dS_vals, dN_vals):
    ratios.append(np.log2(dN/(dS+0.000001)))


xvals=range(0, len(dS_vals))


fig, ax = plt.subplots()
plt.scatter(xvals, ratios, color=color_list, s=2)
plt.xlabel('Codon position')
plt.ylabel('log2(dN/dS)')
fig.savefig('ratios.png')
plt.close()







    
    


            

            
        
    
        
        
    
           
        
       
   

   
