#!/usr/bin/env python3

"""Usage: ./hwBoxplot.py <gene_name> <FPKMs.csv>

Boxplot all transcripts for a given gene separately for males and females"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

df = pd.read_csv( fpkm_file, index_col="t_name" )
goi = df.loc[:,"gene_name"] == gene_name
fpkms = df.drop(columns="gene_name")

columns = fpkms.columns
females = []
males = []
for i in columns:
    if i.startswith("f"):
        females.append(True)
    else:
        females.append(False)
        
for i in columns:
    if i.startswith("m"):
        males.append(True)
    else:
        males.append(False)
        
femaleLogs = np.log((fpkms.loc[goi, females])+0.01)
maleLogs = np.log((fpkms.loc[goi, males])+0.01)
#print(fpkms.loc[goi, :])

fig, ax = plt.subplots(2)
ax[0].boxplot(femaleLogs.T)
ax[0].set_title("Female " + str(sys.argv[1]) + " transcript frquencies", fontsize=10)
ax[1].boxplot(maleLogs.T)
ax[1].set_title("Male " + str(sys.argv[1]) + " transcript frequencies", fontsize=8)
fig.savefig("boxplot.png")
plt.close(fig)
