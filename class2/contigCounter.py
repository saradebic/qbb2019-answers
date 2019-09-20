#!/usr/bin/env python3
# Counts number of contigs, max/min/average length of contigs, and N50 of input fasta file of contigs
# to use: ./contigCounter.py <fasta_file>


#Parse and print all records from a FASTA file

import sys
class FASTAReader(object):
   def __init__(self, fh):
       self.fh = fh
       self.last_ident = None
       self.eof = False #eof =end of file
   def next(self):
       if self.eof:
           return None, None
       elif self.last_ident is None:
           line = self.fh.readline()
           assert line.startswith(">"), "Not a FASTA file"
           ident = line[1:].rstrip("\n")
       else:
           ident = self.last_ident
           #If we reach here, odent is set correctly
       sequences = []
       while True:
           line = self.fh.readline()
           if line == "":
               self.eof = True
               break
           elif line.startswith(">"):
               self.last_ident = line[1:].rstrip("\n")
               break
           else:
               sequences.append(line.strip())
       sequence = "".join(sequences)
       return ident, sequence
       
#What I want to work:
#code for counting contigs and stuff
num_of_contigs = 0
list_length_of_contigs = []


reader = FASTAReader(open(sys.argv[1]))
while True:
   ident, sequence = reader.next()
   list_length_of_contigs.append(len(str(sequence)))
   num_of_contigs += 1
   #print(num_of_contigs)
   if ident is None:
       break
   #print (ident, sequence)
   
   
print("The number of contigs is: " + str(num_of_contigs))
list_length_of_contigs = sorted(list_length_of_contigs, reverse=True)
#print(list_length_of_contigs)
print("The max contig is length: " + str(list_length_of_contigs[0]))
print("The min contig length is: " + str(list_length_of_contigs[-1]))

average = sum(list_length_of_contigs)/len(list_length_of_contigs)
print("The average contig length is: " + str(average))


num_sum = 0
for num in list_length_of_contigs:
    num_sum += num
    if num_sum >= sum(list_length_of_contigs)/2:
        print("The N50 is: " + str(num))
        break 
        