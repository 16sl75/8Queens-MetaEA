import random
import numpy as np
import pandas as pd

def meta_permutation(meta_popsize=8):
    """initialize a population of permutation"""
    
    population = []
    while len(population) < meta_popsize:
        chrom = []
        gamma = random.uniform(0.9, 1)
        learning_rate = random.uniform(0.0001, 0.01)
        
        episodes=10*random.randint(10, 100)
        epsilon = random.uniform(0, 1)
        buffer_len = 100*random.randint(20, 100)
        

        square = random.randint(2, 7)
        batch_size = 2**square

        chrom = [gamma, learning_rate, episodes, epsilon, buffer_len, batch_size]
        population.append(chrom)

    return population