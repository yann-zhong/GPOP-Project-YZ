# Necessary imports
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import statistics
import random 
from itertools import groupby

# import seaborn as sns

p = 0.8
q = 1-p
generations = 750
population = 100
subpopulation_nb = 10

allele_pop = list(np.ones(round(p*population/subpopulation_nb), dtype=int))               # Populate A
second_allele_pop = list(np.zeros(round(q*population/subpopulation_nb), dtype=int))       # Populate B
[allele_pop.append(i) for i in second_allele_pop]   

all_subpops = [allele_pop for i in range(10)]

subpop_allele_count = [0,0]

# for allele in all_subpops[0]:
#     if allele == 1:
#         subpop_allele_count[0]+=1
#     else:
#         subpop_allele_count[1]+=1

subpop_allele_count[0] = all_subpops[0].count(1)
subpop_allele_count[1] = all_subpops[0].count(0)

# for allele in all_subpops[0]:
#     subpop_allele_count[0]+=1 if allele ==1 else subpop_allele_count[1]+=1

current_subpop = []               
current_subpop = [random.choice(all_subpops[0]) for k in range(10)]   

# subpop_allele_count = [0,0]                              # Count alleles from previous subpopulation generation
# subpop_allele_count[0] = all_subpops[m].count(1)         # Nb of p/subpopulation = probability of picking this as parent
# subpop_allele_count[1] = all_subpops[m].count(0)

migration_choice = list(range(0,10)) 
chosen_destination = random.choice(migration_choice)    
                
chosen_allele_index = random.choice(range(len(all_subpops[chosen_destination])))
print(chosen_allele_index) 
print(all_subpops[chosen_destination])
print(all_subpops[chosen_destination][chosen_allele_index])       