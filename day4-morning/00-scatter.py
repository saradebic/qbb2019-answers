#!/usr/bin/env python3

"""Usage: ./00-scatter.py <ctab> 

compare num_exons vs length"""

import sys
import matplotlib.pyplot as plt

exons = []
lengths = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    exons.append(int(fields[6]))
    lengths.append(int(fields[7]))
    
fig, ax = plt.subplots()
ax.scatter( x=exons, y=lengths)
ax.plot([0,40], [0,20000], color="red")
fig.savefig("exon-v-length.png")
plt.close(fig)