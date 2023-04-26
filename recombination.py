"""
Collection of recombination methods

"""

#imports
import numpy as np
import random
def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    point = random.randint(1,len(parent1))
    point = int(point)
    # point = 8

    C1_1 = parent1[:point]
    C1_2 = parent1[point:]

    C2_1 = parent2[:point]
    C2_2 = parent2[point:]

    C1_tuple = (C1_1, C2_2)
    offspring1 = np.hstack(C1_tuple)

    C2_tuple = (C2_1, C1_2)
    offspring2 = np.hstack(C2_tuple)
    # student code end

    offspring1 = offspring1.tolist()
    offspring2 = offspring2.tolist()
    return offspring1, offspring2
