#!/usr/bin/env python3
# Creates dotplot of contig mapped to reference 
# Usage: ./contigDotplot.py <output of lastz>

import sys
import matplotlib.pyplot as plt

dict = {}

for line in open(sys.argv[1]):
    if not line.startswith("#"):
         fields = line.rstrip("\n").split()
         if fields[6] != "-" and fields[0] == "0":
             dict[int(fields[3])] = [fields[3], fields[4], int(fields[-1]) - int(fields[-2])]

valuesStart1 = []
valuesStart2 = []
valuesLength = []             
for value in sorted(dict):
    valuesStart1.append(dict[value][0])
    valuesStart2.append(dict[value][1])
    valuesLength.append(dict[value][2])  


fig, ax = plt.subplots()
xvalue = 0
for i in range(len(valuesStart1)):
    plt.plot([xvalue, xvalue+valuesLength[i]], [valuesStart1[i],valuesStart2[i]], 'k-')
    xvalue += valuesLength[i]
ax.set_title('Contigs assembled to genome') 
ax.set_xlabel('Contigs')
ax.set_ylabel('Genome')  
ax.yaxis.set_major_locator(plt.MaxNLocator(8))
plt.tight_layout()
fig.savefig("Dotplot.png")
plt.close()
     
 