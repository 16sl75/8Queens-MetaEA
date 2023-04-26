import random
import numpy as np

def meta_random_uniform(popsize, mating_pool_size):
    
    selected_to_mate = np.random.randint(0, popsize, mating_pool_size)

    return selected_to_mate

def meta_tournament(fitness, mating_pool_size, tournament_size):
    
 
    selected_to_mate = []
    
    while len(selected_to_mate) < mating_pool_size:
        
        temfitness = np.random.choice(fitness, tournament_size)
        maxfit=np.amax(temfitness)
        maxind=np.where(fitness==maxfit)[0][0]        
        
        selected_to_mate.append(maxind)
    
    return selected_to_mate

def meta_MPS(fitness, mating_pool_size):
    
    fitness_copy = fitness[:]
    fitness_copy.sort()
    fitness_sum = sum(fitness_copy)
    pointdis = fitness_sum/mating_pool_size
    start = random.uniform(0, pointdis)
    pointers= [start+i*pointdis for i in range(mating_pool_size)]
    choice = []
    for i in pointers:
        index = 0
        while sum(fitness_copy[:index+1])<i:
            index=1
        choice.append(fitness_copy[index])
    selected_to_mate = []
    for j in choice:
        selected_to_mate.append(fitness.index(j))

    return selected_to_mate