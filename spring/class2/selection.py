#!/usr/bin/bash python3 

import numpy as np
import sys
import matplotlib.pyplot as plt
import statistics

def simulation(n, p, s):
    time_to_fixation = 0
    new_num_of_allele = np.random.binomial(n,p)
    p = new_num_of_allele * (1+s) / (n - new_num_of_allele + (new_num_of_allele * (1+s)))
    
    while new_num_of_allele != 0 and new_num_of_allele != n:
        new_num_of_allele = np.random.binomial(n,p)
        p = new_num_of_allele * (1+s) / (n - new_num_of_allele + (new_num_of_allele * (1+s)))
        time_to_fixation = time_to_fixation + 1

    return time_to_fixation
    
selection_coefficients = [1,10,20,30,40,50,60,70,80,90,100]
fixation_times = []

for i in selection_coefficients:
    short_list = []
    for j in range(100):
        fix_time = simulation(200,0.5,i)
        short_list.append(fix_time)
        
    average = statistics.mean(short_list)
    fixation_times.append(average)
     
fig, ax = plt.subplots()
plt.scatter(selection_coefficients, fixation_times)
plt.xlabel('Selection coefficients')
plt.ylabel('Fixation time')
plt.title('Fixation time v. selection coefficient')
fig.savefig('fix_time_v_selection_coeff.png')
plt.close()     