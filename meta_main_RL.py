import meta_evaluation_RL; import meta_initialization_RL; import random; import meta_mutation
import meta_parent_selectionRLNN; import meta_recombination; import meta_survivor_selectionRLNN
import json

def meta_main():
    """Meta EA Begins"""
    """INITIALISE population with random candidate solutions"""
    meta_popsize = 12; 
    meta_population = meta_initialization_RL.meta_permutation(meta_popsize)

    """EVALUATE each candidate"""
    meta_fitness_list = []
    for meta_individual in meta_population:
        print("\n\nindividual=", meta_individual)
        meta_fitness = meta_evaluation_RL.meta_evaluation(meta_individual) # you can change the parameters here
        print("meta_fitness[score]=", meta_fitness)
        print(f'gamma:{meta_individual[0]}, learning_rate:{meta_individual[1]}, episodes:{meta_individual[2]}, epsilon:{meta_individual[3]}, buffer_len:{meta_individual[4]},  batch_size:{meta_individual[5]}')
        meta_fitness_list.append(meta_fitness)
    """
    REPEAT UNTIL (TERMINATION CONDITION is satisfied) DO  
        1 SELECT parents; 
        2 RECOMBINE pairs of parents; 
        3 MUTATE the resulting offsprings  
        4 EVALUATE new candidates; 
        5 SELECT individuals for the next generation; 
    """
    
    meta_gen_limit = 50; meta_mating_pool_size = int(meta_popsize/2); meta_xover_rate = 0.5; meta_gen = 0; meta_mut_rate = 0.5
    average_fitness = []
    while meta_gen < meta_gen_limit:

        # 1 SELECT parents;
        # pick parents
        parent_fitness=[meta_fitness_list[i][0] for i in range(len(meta_fitness_list))]
        meta_parents_index = meta_parent_selectionRLNN.meta_tournament(parent_fitness, meta_mating_pool_size, 4)
        # in order to randomly pair up parents
        random.shuffle(meta_parents_index)
        # offspring are generated using selected parents in the mating pool

        # 2 RECOMBINE pairs of parents;
        # 3 MUTATE the resulting offsprings
        # 4 EVALUATE new candidates;
        meta_offspring =[]
        meta_offspring_fitness = []
        ip= 0 # initialize the counter for parents in the mating pool
        while len(meta_offspring) < meta_mating_pool_size:
          
            if random.random() < meta_xover_rate:
                off1,off2 = meta_recombination.permutation_cut_and_crossfill(meta_population[meta_parents_index[ip]], meta_population[meta_parents_index[ip+1]])
            else:
                off1 = meta_population[meta_parents_index[ip]].copy()
                off2 = meta_population[meta_parents_index[ip+1]].copy()
            # 3 MUTATE the resulting offsprings
            # mutation
            if random.random() < meta_mut_rate:
                off1 = meta_mutation.permutation_swap(off1)
            if random.random() < meta_mut_rate:
                off2 = meta_mutation.permutation_swap(off2)
            # 4 EVALUATE new candidates;
            meta_offspring.append(off1)
            meta_offspring_fitness.append(meta_evaluation_RL.meta_evaluation(off1))
            meta_offspring.append(off2)
            meta_offspring_fitness.append(meta_evaluation_RL.meta_evaluation(off2))
            ip += 2
        # 5 SELECT individuals for the next generation;
       
        meta_population, meta_fitness_list = meta_survivor_selectionRLNN.meta_replacement(meta_population, meta_fitness_list, meta_offspring, meta_offspring_fitness)
        print(meta_fitness_list)
        fitness_acc = [meta_fitness_list[i][0] for i in range(len(meta_fitness_list))]
        average_fitness.append(sum(fitness_acc)/len(fitness_acc))
        print("\n******")
        print("The average fitness in this generation is:", average_fitness[-1])
        print("******\n")
        meta_gen = meta_gen + 1

        

    json_object = json.dumps(average_fitness, indent=4)
    with open("result_RL.json", "w") as outfile:
        outfile.write(json_object)


    print("\n\nMeta main summary")
    for i in range(len(meta_fitness_list)):
        print("meta_fitness[score]=", [{meta_fitness_list[i][0]}])
        print(f'gamma:{meta_individual[0]}, learning_rate:{meta_individual[1]}, episodes:{meta_individual[2]}, epsilon:{meta_individual[3]}, buffer_len:{meta_individual[4]}')
    print("\nmeta_fitness[score]=\n",meta_fitness_list)
    print("meta_population = \n", meta_population)

meta_main()