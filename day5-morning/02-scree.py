#!/usr/bin/env python3

"""Usage: ./02-scree.py <all.csv>  """

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], index_col="t_name")
df = df.drop(columns = "gene_name")

n, p = df.shape

fit = PCA().fit(df.T) #to cluster samples rather than genes

fig, ax = plt.subplots()
ax.bar(range(p), fit.explained_variance_ratio_)
fig.savefig("scree.png")
plt.close(fig)