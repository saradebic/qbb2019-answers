#!/usr/bin/env python3

"""Usage: ./residuals.py <t_data.ctab> <H3K4me1_tab> <H3K4me3_tab> <H3K9me3_tab>""" #outtab is a file with histone data

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

ctab = pd.read_csv(sys.argv[1], sep="\t", index_col = "t_name")
H3K4me1_tab = pd.read_csv(sys.argv[2], sep="\t", header=None, names=["t_name", "size", "covered", "sum", "mean0", "mean"],index_col = "t_name")
H3K4me3_tab = pd.read_csv(sys.argv[3], sep="\t", header=None, names=["t_name", "size", "covered", "sum", "mean0", "mean"], index_col = "t_name")
H3K9me3_tab = pd.read_csv(sys.argv[4], sep="\t", header=None, names=["t_name", "size", "covered", "sum", "mean0", "mean"], index_col = "t_name")

df = pd.DataFrame(ctab['FPKM'])
df["H3K4me1"] = H3K4me1_tab["mean"]
df["H3K4me3"] = H3K4me3_tab["mean"]
df["H3K9me3"] = H3K9me3_tab["mean"]

model = sm.formula.ols(formula="FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data= df)
ols_results = model.fit()

print(ols_results.summary())
print(ols_results.resid)

fig, ax = plt.subplots()
ax.hist(ols_results.resid, bins=1000, range=(-100,100))
ax.set_xlim((-100,100))
plt.xlabel("Residual values")
plt.ylabel("Frequency")
fig.savefig("residuals.png")
plt.close(fig)