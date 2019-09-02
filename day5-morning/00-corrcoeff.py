#!/usr/bin/env python3


"""Usage: ./00-corrcoeff.py <all.csv>"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1], index_col = "t_name")

spearman_corr = df.corr(method="spearman")

fig, ax = plt.subplots()
im = ax.pcolor(spearman_corr)
fig.colorbar(im, ax = ax)
plt.yticks(range(16), spearman_corr.columns)
plt.xticks(range(16), spearman_corr.columns, rotation=90)
plt.tight_layout()
fig.savefig("spearman_corr.png")
plt.close()

