"""
Collection of parent selection methods

"""

# imports
import random
import numpy as np

def MPS_bak(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    fitness_index =[]
    fitness_value = []

    population_size = len(fitness)
    cut_point1 = int(population_size/4)
    cut_point2 = int(population_size*2/4)
    cut_point3 = int(population_size*3/4)
    cut_point4 = int(population_size*4/4)

    for index in range(population_size):
        fitness_index.append(index)
        fitness_value.append(fitness[index])
    c = fitness_index
    d = fitness_value
    zip_c_d = zip(c, d)
    sorted_zip = sorted(zip_c_d, key=lambda x: x[1], reverse=True)
    sorted_c, sorted_d = zip(*sorted_zip)
    sorted_fitness_index = sorted_c
    sorted_fitness_value = sorted_d

    selected_to_mate_1 = random.sample(sorted_fitness_index[0:cut_point1], int(0.4*mating_pool_size))
    selected_to_mate_2 = random.sample(sorted_fitness_index[cut_point1:cut_point2], int(0.3*mating_pool_size))
    selected_to_mate_3 = random.sample(sorted_fitness_index[cut_point2:cut_point3], int(0.2*mating_pool_size))
    selected_to_mate_4 = random.sample(sorted_fitness_index[cut_point3:cut_point4], int(0.1*mating_pool_size))

    selected_to_mate.extend(selected_to_mate_1)
    selected_to_mate.extend(selected_to_mate_2)
    selected_to_mate.extend(selected_to_mate_3)
    selected_to_mate.extend(selected_to_mate_4)

    # student code ends

    return selected_to_mate

def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    selected_to_mate_index = []
    parent_1 = fitness[0:mating_pool_size]
    parent_2 = fitness[mating_pool_size:]
    cut_point_1 = random.randint(0,mating_pool_size)
    cut_point_2 = random.randint(cut_point_1,mating_pool_size)
    number_parent_1_fragment = random.randint(0,2)
    number_parent_2_fragment = 3 - number_parent_1_fragment
    if number_parent_1_fragment == 1:
        part_selected_for_1 = random.randint(1,3)
        if part_selected_for_1 == 1:
            selected_to_mate_index = parent_1[0:cut_point_1] + parent_2[cut_point_1:cut_point_2]+ parent_2[cut_point_2:]
        elif part_selected_for_1 == 2:
            selected_to_mate_index = parent_2[0:cut_point_1] + parent_1[cut_point_1:cut_point_2]+ parent_2[cut_point_2:]
        else:
            selected_to_mate_index = parent_2[0:cut_point_1] + parent_2[cut_point_1:cut_point_2]+ parent_1[cut_point_2:]
    else:
        part_selected_for_2 = random.randint(1,3)
        if part_selected_for_2 == 1:
            selected_to_mate_index = parent_2[0:cut_point_1] + parent_1[cut_point_1:cut_point_2]+ parent_1[cut_point_2:]
        elif part_selected_for_2 == 2:
            selected_to_mate_index = parent_1[0:cut_point_1] + parent_2[cut_point_1:cut_point_2]+ parent_2[cut_point_2:]
        else:
            selected_to_mate_index = parent_1[0:cut_point_1] + parent_1[cut_point_1:cut_point_2]+ parent_2[cut_point_2:]
    # student code ends
    for elem in selected_to_mate_index:
        selected_to_mate.append(selected_to_mate_index.index(elem))
    return selected_to_mate

def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []
    # student code starts
    selected_candidate_fitness =[]
    potential_candidates_group = []
    potential_candidates = []
    fitness_copy = fitness.copy()
    selected_to_mate_index = []
    while len(fitness_copy) != tournament_size:
        j = 0
        while j < tournament_size:
            potential_candidates_group.append(fitness_copy[0])
            fitness_copy.remove(fitness_copy[0])
            j = j + 1
        potential_candidates.append(potential_candidates_group)
        potential_candidates_group = []
    potential_candidates.append(fitness_copy)
    for elem in potential_candidates:
        elem = sorted(elem)
        selected_candidate_fitness.append(elem[len(elem)-2:])

    selected_to_mate_fitness = np.array(selected_candidate_fitness)
    selected_to_mate_fitness = selected_to_mate_fitness.flatten()
    selected_to_mate_fitness = selected_to_mate_fitness.tolist()
    group_number = 0
    i = 0
    visited = False
    # fitness_index = None
    for fitness_value in selected_to_mate_fitness:
        fitness_index = fitness.index(fitness_value)
        for value in fitness:
            if fitness_value == value:
                if fitness_index in selected_to_mate:
                    fitness_index_next = fitness.index(fitness_value) + 1
                    selected_to_mate.append(fitness_index_next)
                    i += 1
                else:
                    # fitness_index = fitness.index(fitness_value)
                    selected_to_mate.append(fitness_index)
                    i += 1
    return selected_to_mate

def random_uniform(population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []
    # student code starts
    selected_to_mate = random.sample(range(population_size), mating_pool_size)
    # student code ends

    return selected_to_mate