#!/usr/bin/env python3

"""to use kmerExtender.py <target.fa> <query.fa> <k>"""

from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])

kmers_from_target={}
targets = {}

for ident, sequence in target:
    sequence = sequence.upper()
    targets[ident] = sequence
    for position in range(0, len(sequence) - k + 1):
        kmertarget = sequence[position:position+k]
        if kmertarget in kmers_from_target:
            kmers_from_target[kmertarget].append((ident, position))
        if kmertarget not in kmers_from_target:
            kmers_from_target[kmertarget] = [(ident, position)]
            
extenders_dictionary = {}
            
for identifier, sequence1 in query:
    sequence1 = sequence1.upper()
    for position1 in range(0, len(sequence1) - k + 1):
        kmerquery = sequence1[position1:position1+k]
        if kmerquery in kmers_from_target:
            for tupl in kmers_from_target[kmerquery]:
                start = tupl[1]
                targetID = tupl[0]
                x = 0
                rightextended = kmerquery
                while x+position1+k<len(sequence1) and x+position1+k<len(targets[targetID]): #right extend
                    if sequence1[position1+k+x] == targets[targetID][start+k+x]:
                        x+=1
                        if targetID not in extenders_dictionary:
                            extenders_dictionary[targetID] = []
                        rightextended = rightextended + sequence1[position1+k+x]
                        if rightextended in extenders_dictionary[targetID]:
                            extenders_dictionary[targetID].append(rightextended)
                        if rightextended not in extenders_dictionary[targetID]:
                                extenders_dictionary[targetID].append(rightextended)
                            
                    elif sequence1[position1+k+x] != targets[targetID][start+k+x]:
                        break
                leftextended = kmerquery
                x = -1
                while x+position1>0:
                    if sequence1[position1+x] == targets[targetID][start+x]:
                        x=x-1
                        leftextended = leftextended + sequence1[position1+k+x]
                        if targetID not in extenders_dictionary:
                            extenders_dictionary[targetID] = []
                        if leftextended in extenders_dictionary[targetID]:
                            extenders_dictionary[targetID].append(leftextended)
                        if leftextended not in extenders_dictionary[targetID]:
                                extenders_dictionary[targetID].append(leftextended)
                            
                    elif sequence1[position1+x] != targets[targetID][start+x]:
                        break
                
                

for targetID in extenders_dictionary:
    print(targetID, sorted(extenders_dictionary[targetID], key=len))
                    
                    
                    
                         
    
            
            
        
        
    