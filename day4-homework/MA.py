#!/usr/bin/env python3

"""Usage: MA.py"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpkms = pd.read_csv("all.csv")

fpkms_male = list(fpkms.loc[:,"male_10"])
fpkms_female = list(fpkms.loc[:,"female_10"])

M_values = []
A_values = []

fig, ax = plt.subplots()
for i in range(0,len(fpkms_male)):
    M = np.log2(float(fpkms_male[i])+1) - np.log2(float(fpkms_female[i]+1))
    A = (0.5*np.log2(float(fpkms_male[i])+1)) + np.log2(float(fpkms_female[i]+1))
    A_values.append(A)
    M_values.append(M)
   
fig, ax = plt.subplots()   
ax.scatter(A_values, M_values, alpha = 0.5, s = 8)
ax.set_title("MA plot comparing samples males_10 and females_10")
plt.xlabel("A values")
plt.ylabel("M values")
fig.savefig("MA.png")
plt.close(fig)
    