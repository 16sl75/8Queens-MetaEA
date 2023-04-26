#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    # student code begin
    # get the random cut point
    point=random.randint(0,len(parent1)-1)
    
    left_off1=parent1[:point]
    right_off1=parent1[point:]
    
    
    left_off2=parent2[:point]
    right_off2=parent2[point:]
    

    #cut_and_crossfill parent2 to parent1
    for val1 in left_off1:
        offspring1.append(val1)
    for val2 in right_off2:
        offspring1.append(val2)

    # cut_and_crossfill parent1 to parent2
    for val3 in left_off2:
        offspring2.append(val3)
    for val4 in right_off1:
        offspring2.append(val4)
    # student code end 
    
    return offspring1, offspring2
