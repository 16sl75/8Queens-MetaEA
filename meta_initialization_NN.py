import random
import numpy as np
import pandas as pd

def meta_permutation(meta_popsize=8):
    """initialize a population of permutation"""
    
    population = []
    optimizer_dict = {'Adam': 0, 'SGD': 1}
    while len(population) < meta_popsize:
        chrom = []
        
        learning_rate = random.uniform(0.0001, 0.01)
        
        epochs=10*random.randint(1, 4)

        square = random.randint(2, 6)
        batch_size = 2**square
        optimizer_method_index = random.randint(0,1)
        optimizer_method = list(optimizer_dict.keys())[list(optimizer_dict.values()).index(optimizer_method_index)]

        chrom = [optimizer_method, learning_rate, epochs, batch_size]
        population.append(chrom)

    return population