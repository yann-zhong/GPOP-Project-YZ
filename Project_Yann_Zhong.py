import numpy as np
import random
from itertools import groupby
 
foo = ['a', 'a', 'a'] 
# print(random.choice(foo))

population = 5
p = 0.6
q = 1-p

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False) 

# test = all_equal(foo)
# print(test)

def coalescent_model(p,q,population):

    # Populate initial population of 100 with two alles A and B with probability p and q
    allele_pop = list(np.ones(int(p*population)))               # Populate A
    second_allele_pop = list(np.zeros(int(q*population)))       # Populate B
    [allele_pop.append(i) for i in second_allele_pop]           # Join A and B to form whole first generation of population

    whole_allele_pop = []
    whole_allele_pop.append(allele_pop)                         # Append in, to be subsequently filled with every generation
    
    ancestor_indexes = []                                       # Will contain N-1 sublists of ancestors
    
    generation_counter = 0

    while True:
        generation_counter += 1
        current_allele_pop = []                                 

        prev_allele_pop = whole_allele_pop[generation_counter-1].copy()

        for j in range(population):
            allele_choice = random.choice(prev_allele_pop)        # Randomly choose from previous generation, no biases
            current_allele_pop.append(allele_choice)
        
        whole_allele_pop.append(current_allele_pop)

        if all_equal(current_allele_pop) == True:
            print("Identity by descent found at "+str(generation_counter)+" generations")
            break

    return whole_allele_pop,ancestor_indexes

test = coalescent_model(p,q,population)
print(test)