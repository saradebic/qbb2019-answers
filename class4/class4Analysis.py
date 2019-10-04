#!/usr/bin/env python3

# Program to plot allele frequencies in histogram and genetic relatedness in PCA 
# Usage: class4Analysis.py <.vcf file> <plink PCA eigenvec>

import sys
import matplotlib.pyplot as plt

allele_frequencies = []
pca_xvals = []
pca_yvals = []
family_set = set()
family_colors = {}
color_list = []

for line in open(sys.argv[1]):
    if not line.startswith("#"):
         fields = line.rstrip('\n').split()
         if ',' not in fields[7]:
             allele_frequencies.append(float(fields[7].split('=')[1]))
         elif ',' in fields[7]:
             something = fields[7].split('=')[1]
             allele_frequencies.append(float(something.split(',')[0]))
                         
for line in open(sys.argv[2]):
    pca_xvals_value = float(line.rstrip().split()[2])
    pca_yvals_value = float(line.rstrip().split()[3])  
    family = line.rstrip().split()[0]
    color_list.append((family,pca_xvals_value, pca_yvals_value))
    family_set.add(family)
    
family = list(family_set)
colors = ['#800000', '#9A6324', '#e6194B', '#808000', '#ffe119', '#469990', '#000075', '#000000', '#f032e6', '#aaffc3', '#a9a9a9']
for i in range(len(family)):
    family_colors[family[i]] = colors[i]

# print(pca_xvals)
# print(pca_yvals)

fig, ax = plt.subplots()
ax.hist(allele_frequencies, bins=1000)
ax.set_xlabel('Allele frequencies')
ax.set_ylabel('Frequency')
ax.set_title('Allele frequencies for each SNP variant')
plt.tight_layout()
fig.savefig("class4Analysis.png")
plt.close(fig)

fig1, ax1 = plt.subplots()
for point in color_list:
    ax1.scatter(point[1], point[2], color = family_colors[point[0]])
ax1.set_xlabel('First principal component')
ax1.set_ylabel('Second principle component')
ax1.set_title('PCA of individual variants')
plt.tight_layout()
fig1.savefig("pca.png")
plt.close(fig1)

         