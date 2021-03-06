#!/usr/bin/bash python3 

import numpy as np
import sys
import matplotlib.pyplot as plt

def simulation(n, p):
    time_to_fixation = 0
    new_num_of_allele = np.random.binomial(n,p)
    p = new_num_of_allele/n
    
    while new_num_of_allele != 0 and new_num_of_allele != n:
        new_num_of_allele = np.random.binomial(n,p)
        p = new_num_of_allele/n
        time_to_fixation = time_to_fixation + 1

    return time_to_fixation

#test = simulation(200,0.5)

time_to_fixation_list = []

for i in range(1000):
    new_time = simulation(200,0.5)
    time_to_fixation_list.append(new_time)
    
fig, ax = plt.subplots()
plt.hist(time_to_fixation_list, bins=100)
plt.xlabel('Time to fixation')
plt.ylabel('Frequency')
plt.title('Histogram of time to fixation after 1000 simulations')
fig.savefig('time_to_fixation_histogram.png')
plt.close()

fixation_times_for_changing_population = []
population_list = [100,1000,10000,100000,1000000,10000000]

for j in population_list:
    new_time = simulation(2*j, 0.5)
    fixation_times_for_changing_population.append(new_time)
    

    

    

    
    

