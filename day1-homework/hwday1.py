#!/usr/bin/env python3

import sys

f = open(sys.argv[1])
alignments = 0
perfecthits = 0
perfecthitsNM = 0
onehits = 0
totalMapQ = 0
reads = 0
for i, line in enumerate(f):
    fields = line.split("\t")
    if fields[2] != "*":
        alignments += 1
    if fields[11] == "AS:i:0":
        perfecthits += 1
    if i <= 10:
        print(fields[2])
    totalMapQ += int(fields[4])
    if fields[2] == "2L" and int(fields[3]) > 10000 and int(fields[3]) < 20000:
        reads += 1
    for field in fields:
        if field.startswith('NM'):
            numofdiffs = field.split(':')[2]
            if numofdiffs == '0':
                perfecthitsNM += 1
        if field.startswith('NH'):
            hits = field.split(':')[2]
            if hits == '1\n':
                onehits += 1
        
average = totalMapQ/alignments      
print("The number of alignments is " + str(alignments))
print("The number of perfect hits according to AS is " + str(perfecthits))
print("The number of perfect hits according to NM is " + str(perfecthitsNM))
print("The number of reads that map to one location in the genome are " + str(onehits))
print("The average MAPQ score is " + str(average)) 
print("The number of reads mapping between bases 10000 and 20000 on chromosome 2L is " + str(reads))
    
    