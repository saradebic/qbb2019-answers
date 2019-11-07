#!/usr/bin/env python3

'''Creates density plot of the relative position of a motif found using meme-chip in the 100 widest narrowpeak hits.
Usage: ./motif_matches.py <bed_file_narrowPeaks> <meme_chip_fimo_output_file_gff>  '''

import sys
import matplotlib.pyplot as plt
import seaborn as sbrn

input_sequence_lengths = {}
motif_relative_positions_in_seqs = []


for count,line in enumerate(open(sys.argv[1])):
    fields = line.rstrip().split()
    sequence_length = int(fields[2]) - int(fields[1])
    input_sequence_lengths[count] = sequence_length
    
print(input_sequence_lengths)

for count,line in enumerate(open(sys.argv[2])):
    if line.startswith('#'):
        continue
    fields = line.rstrip().split()
    if fields[6] == '+':
        middle_of_motif = (int(fields[4]) + int(fields[3]))/2
        print(middle_of_motif)
        relative_position = middle_of_motif/input_sequence_lengths[int(fields[0])]
        motif_relative_positions_in_seqs.append(relative_position)
    if fields[6] == '-':
         middle_of_motif = (int(fields[4]) + int(fields[3]))/2
         relative_position = 1 - (middle_of_motif/input_sequence_lengths[int(fields[0])])
         motif_relative_positions_in_seqs.append(relative_position)

fig, ax = plt.subplots()
sbrn.distplot(motif_relative_positions_in_seqs, bins=30)
fig.savefig('density_plot.png')
plt.close()
    