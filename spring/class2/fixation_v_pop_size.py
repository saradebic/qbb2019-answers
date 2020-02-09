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

#test = simulation(200,0.5)

fixation_times_for_changing_population = []
population_list = [100,1000,10000,100000,1000000,10000000]

for j in population_list:
    list = []
    for i in range(5):
        new_time = simulation(2*j, 0.5)
        list.append(new_time)
    
    average = statistics.mean(list)
    fixation_times_for_changing_population.append(average)
    
fig, ax = plt.subplots()
plt.plot(population_list, fixation_times_for_changing_population)
plt.xlabel('Population size')
plt.ylabel('Fixation time')
plt.title('Fixation time v. population size')
fig.savefig('fixation_time_v_pop_size.png')
plt.close()
    

    

    
    

