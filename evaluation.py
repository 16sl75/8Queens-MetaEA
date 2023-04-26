"""
Collection of fitness evaluation methods

"""

#imports
import numpy as np

# reference: https://medium.com/nerd-for-tech/genetic-algorithm-8-queens-problem-b01730e673fd
def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin
    fitness =0

    for row in range(len(individual)):
        col = individual[row]


        for other_row in range(len(individual)):

            # queens cannot pair with itself
            if other_row == row:
                continue
            if individual[other_row] == col:
                continue
                # fitness -= 1
            if other_row + individual[other_row] == row + col:
                continue
                # fitness -= 1
            if other_row - individual[other_row] == row - col:
                continue
                # fitness -= 1
            # score++ if every pair of queens are non-attacking.
            fitness += 1

    fitness = fitness/2
    # student code end
    
    return fitness


