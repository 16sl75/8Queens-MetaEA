"""
Collection of survivor selection methods

reference: https://blog.csdn.net/zxdd2018/article/details/124714603

"""

#imports
import numpy as np
import random

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu_plus_lambda selection"""
    population = []
    fitness = []

    # student code starts
    survivor_offspring = []
    survivor_offspring_fitness = []
    for fitness_, offspring_ in zip(offspring_fitness, offspring):
        if offspring_ not in current_pop:
            survivor_offspring.append(offspring_)
            survivor_offspring_fitness.append(fitness_)

    survivor_pop = current_pop + survivor_offspring
    survivor_fitness = current_fitness + survivor_offspring_fitness

    #reference: python：根据一个列表对另外一个列表排序: https://blog.csdn.net/zxdd2018/article/details/124714603
    a = survivor_fitness
    b = survivor_pop
    zip_a_b = zip(a,b)
    sorted_zip = sorted(zip_a_b, key= lambda x:x[0],reverse=True)
    sorted_a, sorted_b = zip(*sorted_zip)
    pop_size = len(current_pop)
    sorted_b = list(sorted_b)
    sorted_a = list(sorted_a)
    population = sorted_b[:pop_size]
    fitness = sorted_a[:pop_size]

    # student code ends
    return population, fitness

def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""
    population = []
    fitness = []
    # student code starts

    max_fitness_in_offspring = max(offspring_fitness)
    min_fitness_in_current = min(current_fitness)

    while max_fitness_in_offspring > min_fitness_in_current:
        min_fitness_index_in_current = current_fitness.index(min(current_fitness))
        max_fitness_index_in_offspring = offspring_fitness.index(max(offspring_fitness))
        # current_fitness[min_fitness_index_in_current] = max_fitness_in_offspring
        # offspring_fitness[max_fitness_index_in_offspring] = min_fitness_in_current

        best_chroma_in_offspring = offspring[max_fitness_index_in_offspring]
        worst_chroma_in_current_pop = current_pop[min_fitness_index_in_current]
        if best_chroma_in_offspring not in current_pop:
            current_pop[min_fitness_index_in_current] = best_chroma_in_offspring
            offspring[max_fitness_index_in_offspring]=worst_chroma_in_current_pop
            max_fitness_in_offspring = max(offspring_fitness)
            min_fitness_in_current = min(current_fitness)
            current_fitness[min_fitness_index_in_current] = max_fitness_in_offspring
            offspring_fitness[max_fitness_index_in_offspring] = min_fitness_in_current
        else:
            offspring_fitness.pop(max_fitness_index_in_offspring)
            offspring.pop(max_fitness_index_in_offspring)

        if len(offspring_fitness) == 0:
            break
        else:
            max_fitness_in_offspring = max(offspring_fitness)
            min_fitness_in_current = min(current_fitness)

    population = current_pop
    fitness = current_fitness
    # student code ends
    return population, fitness

def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []
    # student code starts
    total_pop = current_pop + offspring
    total_fitness = current_fitness + offspring_fitness
    selected_to_mate = random.sample(range(len(total_pop)), len(current_pop))

    for index in selected_to_mate:
        fitness_value = total_fitness[index]
        fitness.append(fitness_value)
        population_value = total_pop[index]
        population.append(population_value)
    # student code ends
    return population, fitness