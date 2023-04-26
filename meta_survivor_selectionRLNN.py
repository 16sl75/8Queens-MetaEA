import random

def meta_mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):   
    population = []
    fitness = []
    temp_pop = current_pop[:]+ offspring[:]
    #print(temp_pop)
    temp_fit = current_fitness[:] + offspring_fitness[:]
    zipped = zip(temp_fit, temp_pop)
    zipped = sorted(zipped)
    zipped.reverse()
    sorted_fit, sorted_pop = zip(*zipped)
    for i in range(0,len(current_pop)):
        population.append(sorted_pop[i])
        fitness.append(sorted_fit[i])
    return population, fitness

def meta_replacement(current_pop, current_fitness, offspring, offspring_fitness):

    population = []
    fitness = []
    popsize = len(current_pop)
    current_fitness_value = [current_fitness[i][0] for i in range(len(current_fitness))]
    parentavr=sum(current_fitness_value)/len(current_fitness_value)
    for i in range(len(current_pop)):
        if current_fitness[i][0]<parentavr:
            population=population
        else:
            population.append(current_pop[i])
            fitness.append(current_fitness[i])

    while len(population)<popsize:
        idx = random.randint(0,len(offspring)-1)
        population.append(offspring[idx])
        fitness.append(offspring_fitness[idx])
    
    return population, fitness

def meta_random_uniform(current_pop, current_fitness, offspring, offspring_fitness):

    population = []
    fitness = []
    popsize=len(current_pop)
    cultipopulation = current_pop+offspring
    cultifitness = current_fitness+offspring_fitness
    for i in range(popsize):
        idx = random.randint(0,len(cultipopulation)-1)
        population.append(cultipopulation[idx])
        fitness.append(cultifitness[idx])
        
    return population, fitness