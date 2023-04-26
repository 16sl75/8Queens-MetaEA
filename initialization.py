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

def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""
    # student code begin
    population = []
    while len(population) < pop_size:
        chrom = []
        # for i in range (1, chrom_length+1):
        while len(chrom) < chrom_length:
            new = random.randint(1, chrom_length)
            if not(new in chrom):
                chrom.append(new)
            # chrom.append(new)
        population.append(chrom)

    return population                     

