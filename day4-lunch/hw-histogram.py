#!/usr/bin/env python3

"""Usage: ./hw-histogram.py <ctab> <mu> <sigma> <skewness parameter <location> <scale> >

Plot FPKM"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms=[]
for i, line in enumerate(open(sys.argv[1])):
    if i ==0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append(float(fields[11]) )

my_data = np.log2 (fpkms)
mu = float(sys.argv[2])
sigma = float(sys.argv[3])
a = float(sys.argv[4])
location = float(sys.argv[5])
scale = float(sys.argv[6])

x = np.linspace(-15, 15, 100)
y = stats.norm.pdf(x, mu, sigma )

xskew = np.linspace(-15, 15, 100)
yskew = stats.skewnorm.pdf(xskew, a, location, scale)


fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density=True)
ax.set_title("Frequency of fpkm values in ctab file")
plt.xlabel("Log2 of fpkm")
plt.ylabel("Frequency")
ax.plot(x, y, label="Normal distribution, mu is " + str(sys.argv[2]) + ", and sigma is " + str(sys.argv[3]))
ax.plot(xskew, yskew, label="Skewed distribution, skewness factor is " + str(sys.argv[4]) + ", the location is " + str(sys.argv[5] + ", and the scale is " + str(sys.argv[6])))
ax.legend(loc='upper left', prop={'size': 7})
fig.savefig("fpkms.png")
plt.close(fig)