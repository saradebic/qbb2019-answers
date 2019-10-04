#!/usr/bin/env python3

# Makes manhattan plots for all plink generated files for 40 phenotypes.
# Usage: MAplots.py <file_basename*>

import sys
import matplotlib.pyplot as plt
import numpy as np 

#chr_set = set()
# chr_list = []
chr_list_unique = []
chr_pval_list = []
chr_colors = {}
#chr_length = {}

chr_length_value = 0
for file in sys.argv[1:]:
    for j,line in enumerate(open(file)):
        if j != 0 and 'NA' not in line:
            chromosome=line.rstrip().split()[0]
            p_val = -np.log10(float(line.rstrip().split()[-1]))
            chr_pval_list.append((chromosome, p_val))
            if chromosome not in chr_list_unique:
                chr_list_unique.append(chromosome)
           # chr_length_value = line.rstrip().split()[2]
           # chr_length[chromosome] = chr_length_value
                  
          
    #chr_list = list(chr_set)  
    # for i in range(len(chr_list)):
 #        if chr_list[i] not in chr_list_unique:
 #            chr_list_unique.append(chr_list[i])
            
    colors = ['#42d4f4', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3','#808000']         
    for i in range(len(chr_list_unique)):
        chr_colors[chr_list_unique[i]] = colors[i]
    
    start_point = 1
    #offset = 0
    fig, ax = plt.subplots()
    for chr in chr_list_unique:
        for point in chr_pval_list:
            if point[0] == chr:
                ax.scatter(start_point, point[1], color = chr_colors[point[0]], s = 2)
                if point[1] > 5:
                    ax.scatter(start_point, point[1], color = 'red', s = 2)
                start_point += 1
            # elif point[0] != chr:
#                 offset = chr_length[chr]
    ax.set_title('MA plot for: ' + str(file))    
    ax.set_xlabel('Base position') 
    ax.set_ylabel('-log10(P-value)')      
    plt.tight_layout()
    fig.savefig("MAplot.png")
    plt.close(fig)
    print("SNPs with P-values less than 10^-5 are highlighted in red.")
    break
    

            

            
            
            
            