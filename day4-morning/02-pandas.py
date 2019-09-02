#!/usr/bin/env python3

"""Usage: ./02-pandas.py <ctab> 

compare num_exons vs length...using numpy/pandas"""

import sys
import matplotlib.pyplot as plt
import pandas as pd

ctab = pd.read_csv(sys.argv[1], sep = "\t")


exons = ctab.loc[:,"num_exons"]
lengths = ctab.loc[:, "length"]

print(ctab.describe())

fig, ax = plt.subplots()
ax.scatter( x=exons, y=lengths)
ax.plot([0,40], [0,20000], color="red")
fig.savefig("exon-v-length.png")
plt.close(fig)