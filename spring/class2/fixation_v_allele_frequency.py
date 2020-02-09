#!/usr/bin/bash python3 

import numpy as np
import sys
import matplotlib.pyplot as plt
import statistics

def simulation(n, p):
    time_to_fixation = 0
    new_num_of_allele = np.random.binomial(n,p)
    p = new_num_of_allele/n
    
    while new_num_of_allele != 0 and new_num_of_allele != n:
        new_num_of_allele = np.random.binomial(n,p)
        p = new_num_of_allele/n
        time_to_fixation = time_to_fixation + 1

    return time_to_fixation
    
starting_allele_frequencies = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
list_of_fix_times = []


for i in starting_allele_frequencies:
    short_list = []
    for j in range(100):
        time_to_fix = simulation(200, i) 
        short_list.append(time_to_fix)
    
    list_of_fix_times.append(short_list) 
    
fig, ax = plt.subplots()
plt.boxplot(list_of_fix_times)
ax.set_xticklabels([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
plt.xlabel('Allele frequencies')
plt.ylabel('Fixation time')
plt.title('Fixation time v. starting allele frequency')
fig.savefig('fixation_time_v_allele_frequency.png')
plt.close()