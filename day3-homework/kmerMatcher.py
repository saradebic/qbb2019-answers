#!/usr/bin/env python3

"""to use kmerMatcher.py <target.fa> <query.fa> <k>"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmers_from_target={}

for ident, sequence in target:
    sequence = sequence.upper()
    for position in range(0, len(sequence) - k + 1):
        kmertarget = sequence[position:position+k]
        if kmertarget in kmers_from_target:
            kmers_from_target[kmertarget].append((ident, position))
        if kmertarget not in kmers_from_target:
            kmers_from_target[kmertarget] = [(ident, position)]
            
for identifier, sequence1 in query:
    sequence1 = sequence1.upper()
    for position1 in range(0, len(sequence1) - k + 1):
        kmerquery = sequence1[position1:position1+k]
        if kmerquery in kmers_from_target:
            print(str(kmers_from_target[kmerquery]) + '\t' + str(position1) + '\t' + kmerquery)
    
            
            
                    
        
      
      
        
        
        
        
        
        #for identifier, sequence1 in query:
         #   sequence = sequence.upper()
          #  for j in range(0, len(sequence) - k):
           #     if sequence[j:j+k] in kmers_from_target:
            #        print(ident + "\t" + str(i) + "\t" + str(j))
        
   