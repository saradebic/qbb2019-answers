#!/usr/bin/bash python3 

import numpy as np

sequence1 = 'CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA'
sequence2 = 'GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG'

len1 = len(sequence1)
len2 = len(sequence2)

# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
#              A     C     G     T
sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]
                    
dictionary = { 'A':0, 'C':1, 'G':2, 'T':3 }

gap = 300

matrix_scoring = np.zeros((len1 + 1, len2 + 1))
matrix_traceback = np.zeros((len1 + 1, len2 + 1))


## initialize first row and column
matrix_scoring[0][0] == 0
matrix_traceback[0][0] == 0

for i in range(len1+1):
    for j in range(len2+1):
        if i == 0 and j != 0:
            matrix_scoring[i][j] = matrix_scoring[i][j-1] - gap
            matrix_traceback[i][j] = 2
        if j == 0 and i != 0:
            matrix_scoring[i][j] = matrix_scoring[i-1][j] - gap
            matrix_traceback[i][j] = 1
            
## maximization
for i in range(1,len1+1):
    #print(i)
    for j in range(1,len2+1):
        #print(j)
        v = matrix_scoring[i-1][j] - gap
        h = matrix_scoring[i][j-1] - gap
        if i != len1 and j != len2:
            nucleotide1 = sequence1[i]
            nucleotide2 = sequence2[j]
        alignment_score = sigma[dictionary[nucleotide1]][dictionary[nucleotide2]]
        d = matrix_scoring[i-1][j-1] + alignment_score
        max_score = max(v,h,d)
        matrix_scoring[i][j] = max_score
        if max_score == v:
        	matrix_traceback[i][j] = 1
        if max_score == h:
        	matrix_traceback[i][j] = 2
        if max_score == d:
        	matrix_traceback[i][j] = 3

sequence1_return = ''
sequence2_return = ''
sequence1_index = -1
sequence2_index = -1

i = len1
j = len2


while i != 0 and j != 0:
		if matrix_traceback[i][j] == 3:
			sequence1_return = sequence1_return + sequence1[sequence1_index]
			sequence2_return = sequence2_return + sequence2[sequence2_index]
			sequence1_index = sequence1_index - 1
			sequence2_index = sequence2_index - 1
			i = i -1
			j = j - 1
		if matrix_traceback[i][j] == 2:
			sequence2_return = sequence2_return + sequence2[sequence2_index]
			sequence1_return = sequence1_return + '-'
			sequence2_index = sequence2_index - 1
			j = j -1
		if matrix_traceback[i][j] == 1:
			sequence2_return = sequence2_return + '-'
			sequence1_return = sequence1_return + sequence1[sequence1_index]
			sequence1_index = sequence1_index - 1
			i = i - 1

print(sequence1_return[::-1])
print(sequence2_return[::-1])


        
        



