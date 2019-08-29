#!/usr/bin/env python3

"""Usage: ./scatterFpkm.py <ctab1> <ctab2> >

Plot FPKM"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
ctab1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")

name2 = sys.argv[2].split(os.sep)[-2]
ctab2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

# fpkm = {"sample1": [1,2,3], "sample2": [4,5,6]}

fpkm = {name1: ctab1.loc[:,"FPKM"], name2: ctab2.loc[:, "FPKM"] }
df = pd.DataFrame(fpkm)
df = np.log(df+0.01)

fig, ax = plt.subplots()
ax.scatter( x=df.loc[:, str(name1)], y=df.loc[:, str(name2)], alpha=0.1, s=4)
polyfit = np.polyfit(x=df.loc[:, str(name1)], y=df.loc[:, str(name2)], deg=1)
xpolyfit = df.loc[:, str(name1)]
ypolyfit = (polyfit[0]*xpolyfit) + polyfit[1]
ax.plot(xpolyfit, ypolyfit, color="red", label="y = " + str(polyfit[0]) + "x + " + str(polyfit[1]))
ax.legend(loc="upper right", prop ={'size': 7})
# ax.scatter(x1, y1, s=100, color="blue", alpha=0.5)
# ax.scatter(x2, y2, s=100, color="red", alpha=0.5)
ax.set_title(str(name1) + " FPKM values versus " + str(name2) + " FPKM values")
plt.xlabel(str(name1))
plt.ylabel(str(name2))
fig.savefig("scatterFpkm.png")
plt.close(fig)