"""
Collection of initialization methods for different representations

"""

#reference
# https://github.com/chengxi600/RLStuff/blob/master/Genetic%20Algorithms/8Queens_GA.ipynb
# https://blog.csdn.net/qq_43530128/article/details/104172835
#imports
import random
import numpy as np
import pandas as pd
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection

def meta_permutation (meta_popsize=4, string_length=8):
    """initialize a population of permutation"""
    
    population = []
    parent_selection_dict = {'MPS': 0, 'tournament': 1, 'random_uniform': 2}
    survivor_selection_dict = {'mu_plus_lambda': 4, 'replacement': 5, 'random_uniform': 6}
    while len(population) < meta_popsize:
        chrom = []
        # for i in range (1, chrom_length+1):
        popsize = random.randint(20,100)
        while popsize % 4 != 0:
            popsize = random.randint(20, 100)
        tournament_size = 4
        xover_rate = random.uniform(0,1)
        mut_rate = random.uniform(0,1)
        gen_limit = 10*random.randint(1, 5)
        parent_selection_method_index = random.randint(0,2)
        survivor_selection_method_index = random.randint(4,6)
        parent_selection_method = list(parent_selection_dict.keys())[list(parent_selection_dict.values()).index(parent_selection_method_index)]
        survivor_selection_method = list(survivor_selection_dict.keys())[list(survivor_selection_dict.values()).index(survivor_selection_method_index)]
        chrom = [popsize, tournament_size, xover_rate, mut_rate, gen_limit, string_length,
                 parent_selection_method, survivor_selection_method]
        population.append(chrom)

    return population