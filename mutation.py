"""
Colleciton of mutation methods

"""

# imports
import numpy as np

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    point1 = np.random.randint(len(individual), size=1)
    point1 = int(point1)

    point2 = np.random.randint(len(individual), size=1)
    point2 = int(point2)

    first_ele = mutant[point1]
    second_ele = mutant[point2]

    mutant[point1] = second_ele
    mutant[point2] = first_ele
   
    # student code ends
    
    return mutant
