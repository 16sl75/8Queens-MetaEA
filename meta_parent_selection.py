import random
import numpy as np
from Meta_Utility import indexSort, fitnessSort

def meta_random_uniform(popsize, mating_pool_size):
    
    selected_to_mate = np.random.randint(0, popsize, mating_pool_size)

    return selected_to_mate

def meta_tournament(fitness, mating_pool_size, tournament_size):

    selected_to_mate = []
    
    while len(selected_to_mate) < mating_pool_size:
        temindex = np.random.choice(len(fitness), tournament_size)
        temfitness = []
        for i in temindex:
            temfitness.append(fitness[i])
        indexord= indexSort(temfitness)
        maxind=indexord[0]      
        if maxind not in selected_to_mate:
            selected_to_mate.append(maxind)
    
    return selected_to_mate

def meta_MPS(fitness, mating_pool_size):
    
    fitness_copy = fitness[:]
    fitness_copy = fitnessSort(fitness_copy)
    fitness_sum = sum(fitness_copy[i][2] for i in range(len(fitness_copy)))
    pointdis = fitness_sum/mating_pool_size
    start = random.uniform(0, pointdis)
    pointers= [start+i*pointdis for i in range(mating_pool_size)]
    choice = []
    for i in pointers:
        index = 0
        while sum(fitness_copy[i][2] for i in range(index+1))<i:
            index+=1
        choice.append(fitness_copy[index])
    selected_to_mate = []
    for j in choice:
        selected_to_mate.append(fitness.index(j))

    return selected_to_mate