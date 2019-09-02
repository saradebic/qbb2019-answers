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
col_names = df.columns.values.tolist()

n, p = df.shape

fit = PCA().fit_transform(df.T) #to cluster samples rather than genes

sexes = []
stages = []
for name in col_names:
    sex, stage = name.split("_")
    if sex=="female":
        sexes.append("red")
    else:
        sexes.append("blue")
    if "10" in stage:
        stages.append("lightsalmon")
    elif "11" in stage:
        stages.append("tomato")
    elif "12" in stage:
        stages.append("r")
    elif "13" in stage:
        stages.append("brown")
    elif "14" in stage:
        stages.append("black")
    
    
fig, ax = plt.subplots()
ax.scatter(fit[:,0], fit[:,1], c = stages)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
fig.savefig("pca.png")
plt.close()
