#!/usr/bin/env python3
### To plot differential CTCF binding sites and where CTCF binding sites are found in the genome. 
###Usage: ./CTCFbindingplots.py <diff_binding_G1E> <diff_binding_ER4> <genome_annotationG1E> <genome_annotationER4>

import sys
import matplotlib.pyplot as plt
import numpy as np


counter_lost = 0
counter_gained = 0
feature_counter_ER4 = 0
feature_dic_ER4 = {}
feature_dic_G1E = {}

for i in open(sys.argv[1]):
    counter_lost += 1
    
for i in open(sys.argv[2]):
    counter_gained += 1
    
for i in open(sys.argv[3]):
    feature = i.rstrip().split()[3]
    if feature not in feature_dic_ER4:
        feature_dic_ER4[feature] = 0
    else:
        continue
        
for i in open(sys.argv[4]):
    feature = i.rstrip().split()[3]
    if feature not in feature_dic_G1E:
        feature_dic_G1E[feature] = 0
    else:
        continue
        
for i in open(sys.argv[3]):
    feature = i.rstrip().split()[3]
    feature_dic_ER4[feature] +=1
    
for i in open(sys.argv[4]):
    feature = i.rstrip().split()[3]
    feature_dic_G1E[feature] +=1
    
print(feature_dic_ER4)
print(feature_dic_G1E)
labels = ["Intron", "Exon", "Promoter"]
    
fig, (ax1, ax2) = plt.subplots(ncols=2)
ax1.bar(("Marks lost", "Marks gained"), (counter_lost, counter_gained))
ax1.set_ylabel("Number of sites")
ax1.set_title("CTCF sites lost or gained in erythroid differentiation", size=7, loc='right')
x = np.arange(len(labels))
width = 0.35
ax2.bar(x - width/2, (311, 85, 55), width, label = "ER4")
ax2.bar(x + width/2, (341, 101, 67), width, label = "G1E")
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.set_ylabel("Number of sites")
ax2.set_title("Location of CTCF site comparison ER4 and G1E cells", size = 7)
ax2.legend()
plt.tight_layout()
fig.savefig("CTCFplots.png")
plt.close(fig)
        
    
    

